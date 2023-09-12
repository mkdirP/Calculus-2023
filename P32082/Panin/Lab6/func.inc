;f'(x, y) = x^2 + y
; st1 - x, st0 - y
f1fpu:
	fld st1 ; st0 - x, st1 - x, st2 - y
	fmul st0, st2
	fadd st0, st1
ret

; e^x - x^2 - 2x - 2
f1answ:
	fld st0
	fldl2e
	fmulp st1, st0
	fld st0
	frndint
	fsub st1, st0
	fxch                         ; pairable with FSUB on Pentium (P5)
	f2xm1
	fld1
	faddp st1, st0
	fscale
	fstp st1
	fld st1
	fmul st0, st2
	fsubp st1, st0
	fsub st0, st1
	fsub st0, st1
	fsub dword [const2]
ret



f2: ; sqrt(y*x)
	fld st0
	fmul st0, st2
	fsqrt 
ret 


; sqrt(xy)
; 1/36*(12x^(3/2) + 9 + 4x^3) st0 - x
f2answ:
	fld st0
	fmul st0, st0
	fmul st0, st1 ; x^3, x

	fld st0 ; x^3, x^3, x
	fsqrt
	fmul dword [const12]
	fadd dword [const9]
	fxch st0, st1
	fmul dword [const4]
	faddp st1, st0
	fdiv dword [constdiv36]
ret


f3: ; y*cos(x)
	fld st1
	fcos 
	fmul st0, st1
ret 


; e^sin(x)
f3answ:
	fld st0
	fsin
	fldl2e
	fmulp st1, st0
	fld st0
	frndint
	fsub st1, st0
	fxch                         ; pairable with FSUB on Pentium (P5)
	f2xm1
	fld1
	faddp st1, st0
	fscale
	fstp st1
ret

const4 dd 4.0
const9 dd 9.0
const12 dd 12.0
constdiv36 dd 36.0


answ_func_array dw f1answ, f2answ, f3answ

