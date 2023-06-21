.PHONY: wrt

main.img: main.asm
	nasm -f bin main.asm -o main.img


wrt:
	sudo dd if=main.img of=/dev/sda && sync