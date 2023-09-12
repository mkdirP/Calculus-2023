text_mode_init:
	mov ah, 0x00
	mov al, 0x03  ; text mode VGA 80x25 16 colours
	int 10h
ret	



; si - string, bp - res {int}, cx - length
strint_to_int:
	cld
	push es
	xor ax, ax
	mov es, ax
	mov di, si
	xor al, al
	mov dx, cx
	repne scasb 
	lea si, [di-2]
	sub dx, cx
	dec dx
	mov cx, dx

	std
	xor bx, bx
	.int_loop:
		xor eax, eax
		lodsb
		sub al, '0'
		xor edx, edx
		mul dword [jtbl10i+bx]
		add dword [bp], eax
		add bx, 4
		dec cx
	jnz .int_loop
	cld
	pop es
ret


jtbl10i dd 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000

;si - string, bp - res {float}, cx - length
strfl_to_floats:
	cld
	push es
	xor ax, ax
	mov es, ax

	cmp byte [si], '-'
	jnz .nminus
	or dword [bp], 0x80000000
	inc si
	dec cx
	.nminus:
	push cx
	mov di, si
	mov al, '.'
	mov dx, cx		
	repne scasb ; si-> ___._ 
				;		   ^
	lea si, [di-2] 
	sub dx, cx
	mov cx, dx
	dec cx  ; ? for later
	std
	xor bx, bx
	xor eax, eax
	;finit
	fldz
	.loop_whole:
		lodsb
		sub al, '0'
		mov dword [bp+4], eax
		fild dword [bp+4]
		fld dword [jtbl10+bx]
		fmulp st1, st0
		faddp st1, st0
		add bx, 4
		dec cx
	jnz .loop_whole
	pop cx

	lea di, [si+1]
	cld
	mov al, '.'
	repne scasb
	mov si, di
	xor bx, bx
	.loop_frac:
		lodsb 
		test al, al
		jz .end_frac
		sub al, '0'
		mov dword [bp+4], eax
		fild dword [bp+4]
		fld dword [jtblm10+bx]
		fmulp st1, st0
		faddp st1, st0
		add bx, 4
	jmp .loop_frac
	.end_frac:
	fld dword [bp]
	fmulp st1, st0
	fstp dword [bp]
	pop es
	mov dword [bp+4], 0
ret




jtbl10 dd 1.0, 10.0, 100.0, 1000.0, 10000.0, 100000.0, 1000000.0, 10000000.0, 100000000.0, 1000000000.0, 10000000000.0, 100000000000.0
jtblm10 dd 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001


; di - buf, cx - length(without zero)
input_string_echo:
	mov word [.iaddr], di
	mov byte [.havedot], 0
	mov byte [.intfl], dl
	cld
	inc cx
	._loop:
		push di
		push cx
		xor ah, ah
		int 16h
		pop cx
		pop di
		cmp ah, 0x1c
		je .newln

		cmp al, '0'
		jb .less_zero
		cmp al, '9'
		ja .error

		.putchar:
			stosb
			mov ah, 0x0e
			push di
			push cx
			int 10h
			pop cx
			pop di
			dec cx
			;cmp cx, 0
			jz .error
		jmp ._loop

		.newln:
		xor ax, ax
ret
		.less_zero:
		cmp al, '.'
		je .handledot
		cmp al, '-'
		je .handleminus
		.error:
		mov ax, 1
ret

.handledot:
	cmp byte [.intfl], 0
	jz .error
	cmp di, word [.iaddr]
	jz .error
	cmp byte [.havedot], 0
	jnz .error
	mov byte [.havedot], 1
	jmp .putchar
.handleminus:
	cmp byte [.intfl], 0
	jz .error
	cmp di, word [.iaddr]
	jnz .error
	jmp .putchar

.intfl db 0
.havedot db 0
.iaddr dw 0




clear_line:
	mov ah, 0x3
	int 10h
	test dl, dl
	jz .end
	._loop:
		mov al, ' '
		mov ah, 0x0e
		int 10h

		mov ah, 0x3
		int 10h
		test dl, dl
		je .end		
		dec dl


		mov ah, 0x2
		int 10h

		dec dl
		mov ah, 0x2
		int 10h
	jmp ._loop
	.end:
ret


; a print function, made using BIOS 10h interrupt.
print: ; si - address of a string to output
	cld
	mov ah, 0x0e

	._loop:
		lodsb
		or al, al
		jz ._end
		int 10h
		jmp ._loop
	._end:
ret


; a function, that puts the cursor at the beginnig of the next string
newln:
	xor bh, bh

	xor ax, ax
	mov ah, 0x03
	int 10h

	mov ah, 0x02
	xor dl, dl
	add dh, 1
	int 10h
ret



; converts an unsigned 32-bit integer into a hexadecimal string. 
cvt2hex_32: ; number in eax, pointer to the end of string in di
	std
	._loop:
		push eax
		and eax, 0x0000000f
		mov bx, jtbl
		xlat 
		stosb
		pop eax
		shr eax, 4
		jnz ._loop
	mov al, '0'
	._loop2:
		cmp byte [di], 'x'
		je ._end
		stosb
		jmp ._loop2

._end:
	cld
ret

jtbl db '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'

clearframe:
	push es
	xor ax, ax
	mov es, ax
	mov al, ' '
	cld
	mov cx, 5
	mov di, tblfram+1
	rep stosb
	inc di
	mov cx, 33
	rep stosb
	inc di
	mov cx, 38
	rep stosb
	pop es
ret


; bp - answ array, bx - index
extr_fl_int_int:
	shl bx, 2
	add bp, bx
	mov eax, dword [bp]
	shr eax, 31
	mov byte [extracted_sign], al
	fld dword [bp]
	fabs
	sub bp, bx
	shr bx, 2

	fist dword [extracted_whole]
	fild dword [extracted_whole]
	fsubp st1, st0
	fmul dword [four_digits_num]
	fistp dword [extracted_fract]
ret

extr_fpu_fl_int_int:
	fist dword [extracted_whole]
	mov eax, dword [extracted_whole]
	shr eax, 31
	mov byte [extracted_sign], al
	fld st0
	fabs
	fist dword [extracted_whole]
	fild dword [extracted_whole]
	fsubp st1, st0
	fmul dword [four_digits_num]
	fistp dword [extracted_fract]
ret


extracted_sign  db 0
extracted_whole dd 0
extracted_fract dd 0
four_digits_num dd 10000.0


;bp - answ array, bx - n_start
print_answ_part:
	ffree st0
	ffree st1
	ffree st2
	ffree st3
	ffree st4
	ffree st5
	ffree st6
	ffree st7

	mov si, tbltop1
	call print 
	mov si, tbltop2
	call print 
	mov si, tblsepr
	call print

	add ebx, 11
	mov dword [check_n], ebx
	sub ebx, 11

	mov dword [stsh_n], ebx
	fld dword [var_h.num]
	fwait
	fild dword [stsh_n]
	fwait
	fmulp st1, st0
	fwait
	;fld dword [var_X0.num]
	fadd dword [var_X0.num]

	._loop:
		call clearframe

		mov di, tblfram+5
		mov eax, ebx
		mov cx, 10
		._loop_div:
			xor dx, dx
			div cx
			add dl, '0'
			mov byte [di], dl
			dec di
			test ax, ax
		jnz ._loop_div

		call extr_fl_int_int
		mov di, tblfram+61
		mov eax, dword [extracted_fract]
		mov ecx, 10
		mov si, 4
		._loop_div_frac:	
			xor edx, edx
			div ecx
			add dl, '0'
			mov byte [di], dl
			dec di
			dec si
		jnz ._loop_div_frac

		mov byte [di], '.'
		dec di

		mov eax, dword [extracted_whole]
		._loop_div_whole:
			xor edx, edx
			div ecx
			add dl, '0'
			mov byte [ds:di], dl
			dec di
			test eax, eax
		jnz ._loop_div_whole

		shl bx, 2
		test dword [answ+bx], 10000000000000000000000000000000b
		jz .skip
		mov byte [ds:di], '-'
		.skip:
		shr bx, 2

		call extr_fpu_fl_int_int
		mov di, tblfram+25
		mov eax, dword [extracted_fract]
		mov ecx, 10
		mov si, 4
		._loop_div_frac_2:
			xor edx, edx
			div ecx
			add dl, '0'
			mov byte [di], dl
			dec di
			dec si
		jnz ._loop_div_frac_2

		mov byte [di], '.'
		dec di

		mov eax, dword [ds:extracted_whole]
		._loop_div_whole_2:
			xor edx, edx
			div ecx
			add dl, '0'
			mov byte [di], dl
			dec di
			test eax, eax
		jnz ._loop_div_whole_2

		fst dword [ds:stsh_sgn]
		test dword [ds:stsh_sgn], 10000000000000000000000000000000b		
		jz .skip2
		mov byte [di], '-'
		.skip2:

		mov si, tblfram
		call print

		inc ebx
		cmp ebx, dword [ds:check_n]
		jae .end_loop
		cmp ebx, dword [ds:n_var]
		jae .end_loop

		mov si, tblsepr
		call print

		fwait
		fadd dword [ds:var_h.num]

	jmp ._loop
	.end_loop:

	mov si, tblbot
	call print
	mov ah, 0x0a
	mov al, byte [ds:tblbot_lst]
	mov cx, 1
	int 10h
ret

stsh_sgn dd 0
check_n dd 0
stsh_n dd 0


print_help_and_inp:
	mov ah, 0x02
	xor dx, dx
	int 10h 

	mov si, Outstr8
	call print
	mov si, var_fun_id.string
	call print
	call newln

	mov si, Outstr9
	call print
	mov si, var_Y0.string
	call print
	call newln	

	mov si, OutstrA
	call print
	mov si, var_X0.string
	call print
	call newln

	mov si, OutstrB
	call print
	mov si, var_Xn.string
	call print
	call newln

	mov si, OutstrC
	call print
	mov si, var_h.string
	call print
	call newln

	mov si, OutstrE
	call print
	mov si, var_eps.string
	call print
	call newln

	mov si, OutstrF
	call print
	mov si, var_meth.string
	call print
	call newln

	mov bp, graphstep
	xor bx, bx
	call extr_fl_int_int
	mov eax, dword [extracted_fract]
	mov ecx, 10
	mov di, OutstrD+22
	mov bx, 4
	._loop:
		xor edx, edx
		div cx
		add dl, '0'
		mov byte [di], dl
		dec di
		dec bx
	jnz ._loop
	mov byte [di], '.'
	dec di
	mov eax, dword [extracted_whole]
	._loop2:
		xor edx, edx
		div cx
		add dl, '0'
		mov byte [di], dl
		dec di
		test eax, eax
	jnz ._loop2

	fld dword [graphstepy]
	fdiv dword [const200]
	xor bx, bx
	call extr_fpu_fl_int_int
	mov eax, dword [extracted_fract]
	mov ecx, 10
	mov di, OutstrD+37
	mov bx, 4
	._loop3:
		xor edx, edx
		div cx
		add dl, '0'
		mov byte [di], dl
		dec di
		dec bx
	jnz ._loop3
	mov byte [di], '.'
	dec di
	mov eax, dword [extracted_whole]
	._loop4:
		xor edx, edx
		div cx
		add dl, '0'
		mov byte [di], dl
		dec di
		test eax, eax
	jnz ._loop4
	mov si, OutstrD
	call print
	call newln

	mov di, var_max_diff.string+strlen_var_max_diff-1
	mov bp, var_max_diff.num
	call cvtfltostr
	mov si, var_max_diff.string
	call print
	call newln
ret

; di - str end, bp - number
cvtfltostr:
	xor bx, bx
	call extr_fl_int_int
	mov eax, dword [extracted_fract]
	mov bp, 4
	mov ecx, 10
	._loop1:
		xor edx, edx
		div ecx
		add dl, '0'
		mov byte [di], dl
		dec di
		dec bp
	jnz ._loop1
	mov byte [di], '.'
	dec di
	mov eax, dword [extracted_whole]
	._loop2:
		xor edx, edx
		div ecx
		add dl, '0'
		mov byte [di], dl
		dec di
		test eax, eax
	jnz ._loop2
	cmp byte [extracted_sign], 0
	jnz .pminus
ret
	.pminus:
	mov byte [di], '-'
ret




Outstr0 db "Enter function id(1-3): ", 0
Outstr1 db "Enter Y0: ", 0
Outstr2 db "Enter X0: ", 0
Outstr3 db "Enter Xn: ", 0
Outstr4 db "Enter h: ", 0
Outstr5 db "Enter ", 0xEE ,": ", 0
Outstr6 db "Bad input!", 0
Outstr7 db "Enter method(Euler, Euler_improved, Adams)(0-2): "

Outstr8 db "function id: ", 0
Outstr9 db "Y0: ", 0
OutstrA db "X0: ", 0
OutstrB db "Xn: ", 0
OutstrC db "h: ", 0
OutstrE db 0xEE, ": ", 0
OutstrF db "Method(Euler, Euler_improved, Adams)(0-2): ", 0
OutstrD db "Graph scale X:          Y:            ", 0
OutstrG db "|real Yn - Yn|:          ", 0

tbltop1 db 0xDA, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC2, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC2, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xBF, 0
tbltop2 db 0xB3, "  n  ", 0xB3, "             Xn                  ", 0xB3, "                   Yn                 ", 0xB3, 0
tblsepr db 0xC3, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC5, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC5, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xB4, 0
tblfram db 0xB3, "     ", 0xB3, "                                 ", 0xB3, "                                      ", 0xB3, 0
tblbot  db 0xC0, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC1, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC1, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0xC4, 0 
tblbot_lst db 0xD9