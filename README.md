# Homework on Symbolic Execution

Course: Data and Network Security (Sapienza University of Rome, Computer Science Department)
Year: 2016/2017
Lecture materials: [slides]
Additional materials: 
 - initial example: [source] [ELF 64-bit binary] [angr script] [makefile]
 - bomb: [ELF 64-bit binary] [angr script phase 1] [makefile]
 - Flare ON 2016 - challenge 1: [PE32 executable binary]

## Preliminaries

- Install [angr]. Although angr can run in both Mac OS and Microsoft Windows, it is suggested to run angr under Linux.
- Check its [documentation]
- Install a dissambler. This is needed for analyzing the binaries. Some dissamblers:
    - [Linux / Mac OS]: `objdump` (open source, only ELF binaries, easy to use, basic features)
    - [Windows]: IDA Pro (proprietary, ELF and PE binaries, user-friendly, advanced features)
    - [Linux]: radare2 (open source, ELF and PE binaries, command line interface, advanced features)

## Homework

This homework requires to write an angr script for solving phase 5 (``) of the binary [bomb]. This binary contains 6 phases (plus one secret phase). Each phase requires to type in a string. If the string is valid, the binary proceeds running the next phase, otherwise the bomb explodes and the execution is terminated.

Requirements:
- the script should print out a single (string) solution for phase 5
- the solution should be composed by printable characters (i.e., a user can easily type in the generated string when running the binary)
- the script should find a solution within a reasonable amount of time (e.g., less than 30 seconds) and using a limited amount of memory (e.g., less than 500MB).

To test if a solution is valid, you can run the binary:

    ./bomb

And type in the following solutions:

1) "Border relations with Canada have never been better."
2) "1 2 4 8 16 32"
3) "7 327"
4) "7 0"

Send the angr script for solving phase 5 to coppa [at] dis.uniroma1.it

## Bonus (optional)

[FLARE ON 2016] was the third annual reverse engineering contest hosted by the [FireEye] Labs Advanced Reverse Engineering team. 
The first challenge can be solved using a symbolic execution engine like angr. The student should analyze the [binary] using a dissambler and write and angr script that is able to find a valid input string that solves the challenge. To test a solution, you can run the binary under Windows.

Send the angr script for solving the challenge to coppa [at] dis.uniroma1.it




