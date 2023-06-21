[BITS 16]
[ORG 0x7C00]


%macro read_var 6
	%%try_read_var:
	call clear_line

	mov si, %1 ; ptr to string to output
	call print

	cld
	push es
	mov di, %2
	mov cx, %3
	xor ax, ax
	mov es, ax
	rep stosb
	pop es

	mov di, %2 ; ptr to string to read
	mov cx, %3 ; strlen
	mov dl, %6
	call input_string_echo
	test ax, ax
	jz %%skip
	call newln
	mov si, Outstr6
	call print
	call newln
	jmp %%try_read_var
	%%skip:

	mov si, %2
	mov cx, %3
	mov bp, %4 ; result
	call %5 ; parse int or float
; todo check validity and reenter if invalid
	call newln
%endmacro 



xor ax, ax
mov ds, ax
mov es, ax

mov ah, 0x02
mov al, 9 ; 512 * al to read
xor ch, ch
xor dh, dh
mov cl, 2
mov bx, stage2
int 0x13

jmp 0x7e00



times 510 - ($-$$) db 0
dw 0xAA55

stage2:

;mov ax, 0x07E0
;mov fs, ax

;mov eax, cr0
;and eax, 11111111111111111111111111111011b
;or eax,  0000000000100000b
;mov cr0, eax

mov sp, 0xffff
xor ax, ax
mov ss, ax
mov ds, ax

call text_mode_init
finit
call set_fpu_rounding

read_var Outstr0, var_fun_id.string, strlen_var_fun_id, var_fun_id.num, strint_to_int, 0
read_var Outstr1, var_Y0.string, strlen_var_Y0, var_Y0.num, strfl_to_floats, 1
read_var Outstr2, var_X0.string, strlen_var_X0, var_X0.num, strfl_to_floats, 1
read_var Outstr3, var_Xn.string, strlen_var_Xn, var_Xn.num, strfl_to_floats, 1
read_var Outstr4, var_h.string, strlen_var_h, var_h.num, strfl_to_floats, 1
read_var Outstr5, var_eps.string, strlen_var_eps, var_eps.num, strfl_to_floats, 1
read_var Outstr7, var_meth.string, strlen_var_meth, var_meth.num, strint_to_int, 0

call get_n

mov bx, word [var_fun_id.num]
shl bx, 1
mov ax, word [func_meth_arr+bx-2]

mov ebx, dword [var_meth.num]
shl bx, 1
call word [meth_arr+bx]


call graph_prepare
call find_max_diff


call text_mode_init
call print_help_and_inp

	wait_inp:
		xor ah, ah
		int 16h

		cmp al, 'i'
		jz i_pressed
		cmp al, 'g'
		jz g_pressed
		cmp ah, 0x4b
		jz left_pressed
		cmp ah, 0x4d
		jz right_pressed
	jmp wait_inp

	i_pressed:
		cmp byte [showinginfo], 0
		jz show_info
		mov byte [showinginfo], 0
		jmp show_table

	show_info:
		mov byte [showinginfo], 1
		mov byte [showinggraph], 0
		call text_mode_init
		call print_help_and_inp
	jmp wait_inp

	g_pressed:
		cmp byte [showinggraph], 0
		jz show_graph
		mov byte [showinggraph], 0
		jmp show_table

	show_graph:
		mov byte [showinginfo], 0
		mov byte [showinggraph], 1
		call mode_13h_init
		call plotgraph
		call plotdataset
	jmp wait_inp

	left_pressed:
		mov ebx, dword [curn]
		sub ebx, 11
		cmp ebx, 0
		jl wait_inp
		mov dword [curn], ebx
		show_table:
		call text_mode_init
		mov ebx, dword [curn]
		mov bp, answ
		call print_answ_part
	jmp wait_inp

	right_pressed:
		mov ebx, dword [curn]
		add ebx, 11
		cmp ebx, dword [n_var]
		jae wait_inp
		mov dword [curn], ebx
	jmp show_table



curn dd 0
showinggraph db 0
showinginfo db 1


tststr1 db "0x00000000", 0
tststr2 db "0x00000000", 0
tststr3 db "0x0000", 0


func_meth_arr dw f1fpu, f2, f3
meth_arr dw Euler_method, Euler_improved_method, Adams_method


var_Y0:
	.string db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	.num dd 1.0
	.stsh dd 0
	strlen_var_Y0 equ 15


var_fun_id:
	.string db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	.num dd 0
	strlen_var_fun_id equ 15

var_X0:
	.string db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	.num dd 1.0
	.stsh dd 0
	strlen_var_X0 equ 15

var_Xn:
	.string db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	.num dd 1.0
	.stsh dd 0
	strlen_var_Xn equ 15

var_h:
	.string db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	.num dd 1.0
	.stsh dd 0
	strlen_var_h equ 15

var_eps:
	.string db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	.num dd 1.0
	.stsh dd 0
	strlen_var_eps equ 15

var_meth:
	.string db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	.num dd 0
	strlen_var_meth equ 15

var_max_diff:
	.string db "max(|Yn-Yreal|):                   ", 0
	.num dd 0.0
	strlen_var_max_diff equ 35

%include "methods.inc"
%include "input.inc"
%include "func.inc"
%include "graph.inc"

times 512*10 - ($-$$) db 0
