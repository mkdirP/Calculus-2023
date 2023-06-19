[BITS 16]

; puts a pixel in mode 13h
%macro putpixel 5 ; assume %4 = 0xa000 ; %1 - x %2 - y  %3 - color %5 - memory reg
	shl %2, 6
	mov %5, %2   ; calculate the memory address of the beginning of the raw of pixels(raw number or y is in %2)
	shl %5, 2    ; and put it into the effective address combatible register (%5)
	add %5, %2   ; same as %5 = %2 * 320

	add %5, %1   ; add the x coordinate to %5 to get pixel's address
	mov byte [%4:%5], %3

%endmacro ; affects %5, %2 (%2 is shifted left by 6 bits)(can be restored if the value was <= 0000001111111111b)


mode_13h_init:
	cld
	mov ah, 0
	mov al, 0x13
	int 0x10
	mov ax, 0xa000
	mov es, ax ; do not touch es anymore, remember about DF
ret

graph_prepare:
	call getstepx
	call getgraphstep
	call getgraphy
	call get_min_max_all
	call getstepy
ret

plotgraph:
	xor bx, bx
	fld dword [var_X0.num]
	._loop:
		fld st0 
		fsub dword [ds:var_X0.num]
		fdiv dword [ds:graphstepx]
		fmul dword [ds:const320]
		fadd dword [ds:halfconst]
		fistp dword [ds:plotx]

		fadd dword [ds:graphstep]

		shl bx, 2
		fld dword [ds:graphy+bx]
		shr bx, 2
		fsub dword [ds:Ynmin]
		fdiv dword [ds:graphstepy]
		fmul dword [ds:const200]
		fistp word [ds:ploty]

		mov ax, word [ds:plotx]
		mov cx, 199
		sub cx, word [ploty]

		putpixel ax, cx, 120, es, si
		inc bx
		cmp bx, 320
	jnz ._loop
ret



.bxstash dw 0


plotdataset:
	xor ebx, ebx
	fld dword [ds:var_X0.num]
	._loop:
		fld st0
		fsub dword [ds:var_X0.num]
		fdiv dword [ds:graphstepx]
		fmul dword [ds:const320]
		fistp word [ds:plotx]
		fadd dword [ds:var_h.num]

		shl ebx, 2
		fld dword [ds:answ+bx]
		shr ebx, 2
		fsub dword [ds:Ynmin]
		fdiv dword [ds:graphstepy]
		fmul dword [ds:const200]
		fistp word [ds:ploty]

		mov ax, word [ds:plotx]
		mov cx, 199
		sub cx, word [ploty]
	
		cmp cx, 0
		jge .ppxl
		mov cx, 0


		;mov cx, word [ds:ploty]
		.ppxl:
		putpixel ax, cx, 60, es, si
		inc ebx
		cmp ebx, dword [ds:n_var]
	jnz ._loop
ret



plotx dw 0
ploty dw 0


getgraphstep:
	fld dword [ds:graphstepx]
	fdiv dword [ds:const320]
	fstp dword [ds:graphstep]
ret


getstepx:
	fld dword [ds:var_Xn.num]
	fsub dword [ds:var_X0.num]
	fstp dword [ds:graphstepx]
ret

getstepy:
	fld dword [ds:Ynmax]
	fsub dword [ds:Ynmin]
	fstp dword [ds:graphstepy]
ret





getgraphy:
	ffree st0
	ffree st1
	ffree st2
	ffree st3
	ffree st4
	ffree st5
	ffree st6
	ffree st7
	xor bx, bx
	mov ebp, dword [ds:var_fun_id.num]
	shl ebp, 1
	mov ax, word [ds:answ_func_array+bp-2]
	fld dword [var_X0.num]
	._loop:
		call ax
		shl bx, 2
		fstp dword [ds:graphy+bx]
		shr bx, 2
		fadd dword [graphstep]
		inc bx
		cmp bx, 320
	jnz ._loop
	fstp dword [trash]
ret



trash dd 0

get_min_max_all:
	call get_dataset_min_max
	call get_func_min_max
	fld dword [ds:graphymax]
	fwait
	fcom dword [ds:Ynmax]
	fwait
	fstsw word [ds:fpusw]
	fwait
	test word [ds:fpusw], 0000011100000000b
	jnz .nmove
	fstp dword [ds:Ynmax]
	fwait
	.nmove:

	fld dword [ds:graphymin]
	fwait
	fcom dword [ds:Ynmin]
	fwait
	fstsw word [ds:fpusw]
	fwait
	test word [ds:fpusw], 0000000100000000b
	jz .nmove2
	fstp dword [ds:Ynmin]
	fwait
	.nmove2:
ret



get_dataset_min_max:
	mov ebx, 1
	fld dword [ds:answ]
	fstp dword [ds:Ynmax]
	._loop:
		shl ebx, 2
		fld dword [ds:answ+bx]
		;fabs
		shr ebx, 2
		fcom dword [ds:Ynmax]
		fstsw word [ds:fpusw]
		test word [ds:fpusw], 0000011100000000b
		jz .foundnewmax
		fstp dword [trash]
		inc ebx
		cmp ebx, dword [ds:n_var]
	jnz ._loop
	jmp .endmax
	.foundnewmax:
		fstp dword [ds:Ynmax]
		inc ebx
		cmp ebx, dword [ds:n_var]
	jnz ._loop

	.endmax:

	mov ebx, 1
	fld dword [ds:answ]
	fstp dword [ds:Ynmin]
	._loop2:
		shl ebx, 2
		fld dword [ds:answ+bx]
		;fabs
		shr ebx, 2
		fcom dword [ds:Ynmin]
		fstsw word [ds:fpusw]
		test word [ds:fpusw], 0000000100000000b
		jnz .foundnewmin
		fstp dword [trash]
		inc ebx
		cmp ebx, dword [ds:n_var]
	jnz ._loop2
	jmp .endmin
	.foundnewmin:
		fstp dword [ds:Ynmin]
		inc ebx
		cmp ebx, dword [ds:n_var]
	jnz ._loop2
	.endmin:
ret

get_func_min_max:
	mov bx, 1
	fld dword [ds:graphy]
	fstp dword [ds:graphymax]
	._loop:
		shl bx, 2
		fld dword [ds:graphy+bx]
		;fabs
		shr bx, 2
		fcom dword [ds:graphymax]
		fstsw word [ds:fpusw]
		test word [ds:fpusw], 0000011100000000b
		jz .foundnewmax
		fstp dword [trash]
		inc bx
		cmp bx, 320
	jnz ._loop
	jmp .endmax
	.foundnewmax:
		fstp dword [ds:graphymax]
		inc bx
		cmp bx, 320
	jnz ._loop
	.endmax:

	mov bx, 1
	fld dword [ds:graphy]
	fstp dword [ds:graphymin]
	._loop2:
		shl bx, 2
		fld dword [ds:graphy+bx]
		;fabs
		shr bx, 2
		fcom dword [ds:graphymin]
		fstsw word [ds:fpusw]
		test word [ds:fpusw], 0000000100000000b
		jnz .foundnewmin
		fstp dword [trash]		
		inc bx
		cmp bx, 320
	jnz ._loop2
	jmp .endmin
	.foundnewmin:
		fstp dword [ds:graphymin]
		inc bx
		cmp bx, 320
	jnz ._loop2
	.endmin:
ret



fpusw dw 0

const320 dd 320.0
const200 dd 200.0

graphstep dd 0
graphstepx dd 0
graphstepy dd 0

Ynmax dd 0

Ynmin dd 0

graphymax dd 0
graphymin dd 0


graphy: ; array of floats after the executable


; 6 unit
; 7a 9d 10d