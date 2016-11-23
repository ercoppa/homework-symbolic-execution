# Homework on Symbolic Execution

Course: Data and Network Security (Sapienza University of Rome, Computer Science Department)
Year: 2016/2017

Lecture materials: [[slides](slides.pdf)]

Additional materials: 
 - initial example: [source](initial-example/main.c) [ELF 64-bit binary](initial-example/main) [angr script](initial-example/run.py) [makefile](initial-example/makefile)
 - bomb: [ELF 64-bit binary](bomb/bomb) [angr script phase 1](bomb/phase-1.py) [makefile](bomb/makefile)
 - Flare ON 2016 - challenge 1: [PE32 executable binary](flare-on/challenge1.exe)

## Preliminaries

- Install [angr]. Although angr can run in both Mac OS and Microsoft Windows, it is suggested to run angr under Linux.
- Check its [documentation]
- Install a dissambler. This is needed for analyzing the binaries. Some dissamblers:
    - [Linux / Mac OS]: [`objdump`](https://linux.die.net/man/1/objdump) (open source, only ELF binaries, easy to use, basic features)
    - [Linux / Mac OS / Windows]: [radare2](http://www.radare.org/r/) (open source, ELF and PE binaries, command line interface, advanced features)
    - [Windows / Linux / Mac OS]: [IDA Pro](https://www.hex-rays.com/products/ida/) (proprietary, ELF and PE binaries, user-friendly, advanced features) *Note:* you can use the [demo](https://www.hex-rays.com/products/ida/support/download_freeware.shtml) version of IDA Pro. Under Linux, you can use `wine` to run it under Linux.

## Homework

This homework requires to write an angr script for solving phase 5 (function `phase_5` at `0x401062`) of the binary [bomb](bomb/bomb). This binary contains 6 phases (plus one secret phase). Each phase requires to type in a string. If the string is valid, the binary proceeds running the next phase, otherwise the bomb explodes and the execution is terminated.

Requirements:
- the script should print out a single (string) solution for phase 5
- the solution should be composed by printable characters (i.e., a user can easily type in the generated string when running the binary)
- the script should find a solution within a reasonable amount of time (e.g., less than 30 seconds) and using a limited amount of memory (e.g., less than 500MB).

To test if a solution is valid, you can run the binary (under Linux 64bit):

    ./bomb

And type in the following solutions:

1. "Border relations with Canada have never been better."
2. "1 2 4 8 16 32"
3. "7 327"
4. "7 0"

Send the angr script for solving phase 5 to coppa [at] dis.uniroma1.it

## Bonus (optional)

[FLARE ON 2016] was the third annual reverse engineering contest hosted by the [FireEye] Labs Advanced Reverse Engineering team. 
The first challenge can be solved using a symbolic execution engine like angr. The student should analyze the [binary](flare-on/challenge1.exe) using a dissambler and write an angr script that is able to find a valid input string. The found string solves the challenge. To test a solution, you can run the binary under Windows.

Send the angr script for solving the challenge to coppa [at] dis.uniroma1.it




