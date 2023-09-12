set_fpu_rounding:
	fstcw [fpu_cw]
	;and word [fpu_cw], 1111111111111111b
	or word [fpu_cw], 0000111100111111b
	;and word [fpu_cw], 1111111111111111b

	fldcw word [fpu_cw]
ret

fpu_cw dw 0x073E
;0x0300
;0x0400
;0x0002
;0x0004
;0x0008
;0x0010
;0x0020

get_n:
	fld dword [var_Xn.num]
	;fld dword [var_X0.num]
	;fsubp st1, st0
	;fld dword [var_h.num]
	;fdivp st1, st0
	;fistp dword [n_var]
	fsub dword [var_X0.num]
	fdiv dword [var_h.num]
	fist dword [n_var]

	fild dword [n_var]
	fsubp st1, st0
	fadd dword [halfconst]
	fiadd dword [n_var]
	fistp dword [n_var]

	inc dword [n_var]
ret

halfconst dd 0.5
n_var dd 0



Euler_method:
	fld dword [var_X0.num]
	fld dword [var_Y0.num]
	fst dword [answ]
	mov ebx, 1
	._loop:
		call ax
		fmul dword [var_h.num]
		faddp st1, st0
		shl bx, 2
		fst dword [answ+bx]
		shr bx, 2
		fxch st0, st1
		fadd dword [var_h.num]
		fxch st0, st1
		inc bx
		cmp ebx, dword [n_var]
	jnz ._loop
	fstp dword [trash]
	fstp dword [trash]
ret



;answ dd 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
answ equ graphy+(320*4)


Euler_improved_method: ; ax - function ptr
	;fld dword [var_h.num]
	fld dword [var_X0.num]
	fld dword [var_Y0.num]
	fst dword [ds:answ]
	call ax  ; st0 - f(x0, y0), st1 - y0, st2 - x0
	mov bx, 1
	._loop:
		fld st2
		fadd dword [var_h.num]
		fld st1
		fmul dword [var_h.num]
		fadd st0, st3 ; st0 - yi+hf(xi, yi), st1 - xi+1, st2 - f(xi, yi), st3 - yi, st4 - xi
		call ax ; st0 - f(...), st1 - yi+hf(xi, yi), st2 - xi+1, st3 - f(xi, yi), st4 - yi, st5 - xi
		faddp st3, st0 ;st0 - yi+hf(xi, yi), st1 - xi+1, st2 - f(xi, yi)+f(...), st3 - yi, st4 - xi
		fxch st0, st2
		fmul dword [var_h.num]
		;fmul dword [const2]
		fdiv dword [const2]
		faddp st3, st0 ; st0 - xi+1, st1 - f(xi, yi)+f(...), st2 - yi+1, st3 - xi
		fxch st0, st1
		fstp dword [trash]
		fxch st0, st2
		fstp dword [trash]

		shl bx, 2
		fst dword [answ+bx]
		shr bx, 2

		call ax
		inc bx
		cmp ebx, dword [n_var]
	jnz ._loop
ret



Adams_method: ; ax - function ptr
	cmp dword [n_var], 4
	jae .appiable
	call Euler_method
	mov ax, 1
ret
	.appiable:
	fld dword [var_h.num]
	fmul st0, st0
	fdiv dword [const2]
	fstp dword [powh2div2]
	fld dword [var_h.num]
	fmul st0, st0
	fld dword [var_h.num]
	fmulp st1, st0
	fmul dword [const5div12]
	fstp dword [powh3mul5div12]
	fld dword [var_h.num]
	fmul st0, st0
	fmul st0, st0
	fmul dword [const3div8]
	fstp dword [powh4muk3div8]

	fld dword [var_X0.num]
	fld dword [var_Y0.num]
	fst dword [answ]
	mov bx, 1
	._loop:
		call ax ; st0 - f(x, y), st1 - y, st2 - x
		shl bx, 2
		fst dword [Adams_f+bx-4]
		fmul dword [var_h.num]
		faddp st1, st0
		fld dword [var_h.num] ; st0 - h, st1 - yi+1, st2 - xi
		faddp st2, st0
		fst dword [answ+bx]
		shr bx, 2
		inc bx
		cmp bx, 4 ; st0 - yi+1, st1 - xi+1
	jnz ._loop

	._loop2:
		call ax
		call calc_delta
		mov esi, dword [Adams_f2]
		mov dword [Adams_f3], esi
		mov esi, dword [Adams_f1]
		mov dword [Adams_f2], esi
		fst dword [Adams_f1] ; update memorized functions
		fmul dword [var_h.num] ; st0 - fi*h, st1 - yi, st2 - xi
		fld dword [Adams_delta_1]
		fmul dword [powh2div2]
		faddp st1, st0 ; st0 - fi*h + h^2/2*delta1
		fld dword [Adams_delta_2]
		fmul dword [powh3mul5div12]
		faddp st1, st0; st0 - fi*h + h^2/2*delta1 + 5*h^3/12*delta2
		fld dword [Adams_delta_3]
		fmul dword [const3div8]
		faddp st1, st0 ; st0 - fi*h + h^2/2*delta1 + 5*h^3/12*delta2 + 3*h^4/8*delta3
		faddp st1, st0 ; st0 - yi+1
		fld dword [var_h.num]
		faddp st2, st0 ; st0 - yi+1, st1 - xi+1
		shl bx, 2
		fst dword [answ+bx]
		shr bx, 2
		inc bx
		cmp ebx, dword [n_var]
	jnz ._loop2
ret


calc_delta: ; st0 - fi
	fld st0
	fsub dword [Adams_f1]
	fst dword [Adams_delta_1] ; fi - fi-1
	fsub dword [Adams_f1]
	fadd dword [Adams_f2]
	fst dword [Adams_delta_2] ; fi - 2fi-1 + fi-2
	fsub dword [Adams_f1]
	fadd dword [Adams_f2]
	fadd dword [Adams_f2]
	fsub dword [Adams_f3]
	fstp dword [Adams_delta_3]
ret



find_max_diff:
	mov ebx, dword [var_fun_id.num]
	shl ebx, 1
	mov ax, word [answ_func_array+bx-2]
	xor ebx, ebx
	fld dword [var_X0.num]
	._loop:
		call ax
		shl bx, 2
		fld dword [answ+bx]
		shr bx, 2
		fsubp st1, st0
		fabs
		fcom dword [var_max_diff.num]
		fstsw word [fpusw]
		test word [fpusw], 0000011100000000b
		jz .newmax
		fstp dword [trash]
		fadd dword [var_h.num]
		inc ebx
		cmp ebx, dword [n_var]
	jnz ._loop
	fstp dword [trash]
ret
	.newmax:
		fstp dword [var_max_diff.num]
		fadd dword [var_h.num]
		inc ebx
		cmp ebx, dword [n_var]
	jnz ._loop
	fstp dword [trash]	
ret


Adams_f:
Adams_f3 dd 0
Adams_f2 dd 0
Adams_f1 dd 0
Adams_delta_1 dd 0
Adams_delta_2 dd 0
Adams_delta_3 dd 0
powh2div2 dd 0
powh3mul5div12 dd 0
powh4muk3div8 dd 0


const3div8 dd 0.375
const5div12 dd 0.416666667
const2 dd 2.0



