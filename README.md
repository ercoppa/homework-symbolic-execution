# Homework on Symbolic Execution

Course: Data and Network Security (Sapienza University of Rome, Computer Science Department)

Year: 2016/2017

Lecture materials: [[slides](slides.pdf)]

Additional materials: 
 - initial example: [[source](initial-example/main.c)] [[ELF 64-bit binary](initial-example/main)] [[angr script](initial-example/run.py)] [[makefile](initial-example/makefile)]
 - bomb: [[ELF 64-bit binary](bomb/bomb)] [[angr script phase 1](bomb/phase-1.py)] [[makefile](bomb/makefile)]
 - Flare ON 2016 - challenge 1: [[PE32 executable binary](flare-on/challenge1.exe)]

## Preliminaries

- Install [angr](http://angr.io/install.html). Although angr can run in both Mac OS and Microsoft Windows, it is suggested to run it under Linux.
- Check its [documentation](https://docs.angr.io/)
- Install a dissambler. This is needed for analyzing the binaries. Some dissamblers:
    - [Linux / Mac OS]: [`objdump`](https://linux.die.net/man/1/objdump) (open source, only ELF binaries, easy to use, basic features)
    - [Linux / Mac OS / Windows]: [radare2](http://www.radare.org/r/) (open source, ELF and PE binaries, command line interface, advanced features)
    - [Windows / Linux / Mac OS]: [IDA Pro](https://www.hex-rays.com/products/ida/) (proprietary, ELF and PE binaries, user-friendly, advanced features) **Note:** for our goals, you can use the [demo](https://www.hex-rays.com/products/ida/support/download_freeware.shtml) version of IDA Pro. Under Linux, you can use `wine` to run it.

## Homework

This homework requires to write an angr script for solving phase 5 (function `phase_5` at `0x401062`) of the binary [bomb](bomb/bomb). This binary contains 6 phases (plus one secret phase). Each phase requires to type in a string. If the string is valid, the binary proceeds the execution towards the next phase, otherwise the bomb explodes and the execution is terminated.

Requirements:
- the script should find and print out a single (string) solution for phase 5
- the string solution should be composed by printable characters (i.e., a user can easily type in the generated string when running the binary)
- the script should find a solution within a reasonable amount of time (e.g., less than 30 seconds) and using a limited amount of memory (e.g., less than 500MB)
- the script should take benefit of the features offered by angr
- the script should NOT perform a brute force attack or other similar techniques
- the student should not exploit the knowledge of the string length when writing the script.

To test if a solution is valid, you can run the binary (under Linux 64bit):

    ./bomb

And type in the following solutions:

1. `Border relations with Canada have never been better.`
2. `1 2 4 8 16 32`
3. `7 327`
4. `7 0`


## Bonus (optional)

[FLARE ON 2016](https://2016.flare-on.com) was the third annual reverse engineering contest hosted by the [FireEye](https://www.fireeye.com/) Labs Advanced Reverse Engineering team. 
The first challenge can be solved using a symbolic execution engine like angr. The student should analyze the [binary](flare-on/challenge1.exe) using a dissambler and write an angr script that is able to find a valid input string. To test a solution, you can run the binary under Windows.


## Homework report

**[UPDATE]**
In order to pass the homework, the student must write a report. The report should have the following structure:

- header: student name/surname/_matricola_
- abstract: briefly explain the goal of the homework, what methodologies and which tools have been used by the student
- introduction: explain the problem faced in this homework, how you have approached it, why you have used a specific tool, pros and cons of your appach, what are the alternatives appeached/tools that could have been used, etc.
- technical description: a step by step description of what you have done to solve the homework, commenting the most relevant parts of your script. The student should discuss what features of angr have been used, why they are useful and so on. E.g., how do you have chosen start/find/avoid addresses and why? Disassembler? What are the benefits of avoid addresses? What are the benefits of input constraints? What is a PathGroup? What is the difference between a Path and a PathGroup? How do you start the symbolic execution? How the different paths of program are explored by angr when using your script? BFS? DFS? etc.

The report should be no longer than 4 pages. The report should be written in english. The report should be easy to read even for non-expert user (explain any technical term or technical step!).

Please, create an archive file containing:
- the report (PDF)
- angr script(s) (with comments)
- a README file that explain the purpose of each file in the archive and how to run your scripts

Send the archive to coppa [at] dis.uniroma1.it


