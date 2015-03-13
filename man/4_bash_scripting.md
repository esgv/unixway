==================
Bash and scripting
==================

[default_span] code

When not to use shell scripts
=============================

- Resource-intensive tasks, especially where speed is a factor (sorting, hashing, recursion [2] ...)
- Procedures involving heavy-duty math operations, especially floating point arithmetic, arbitrary precision calculations, or complex numbers (use C++ or FORTRAN instead)
- Cross-platform portability required (use C or Java instead)
- Complex applications, where structured programming is a necessity (type-checking of variables, function prototypes, etc.)
- Mission-critical applications upon which you are betting the future of the company
- Situations where security is important, where you need to guarantee the integrity of your system and protect against intrusion, cracking, and vandalism
- Project consists of subcomponents with interlocking dependencies
- Extensive file operations required (Bash is limited to serial file access, and that only in a particularly clumsy and inefficient line-by-line fashion.)
- Need native support for multi-dimensional arrays
- Need data structures, such as linked lists or trees
- Need to generate / manipulate graphics or GUIs
- Need direct access to system hardware or external peripherals
- Need port or socket I/O
- Need to use libraries or interface with legacy code
- Proprietary, closed-source applications (Shell scripts put the source code right out in the open for all the world to see.)

Basics
======

- `#!/usr/bin/env bash`;
- `exit` at the end returns exit code of last program invoked.


Variables
=========

Basics
------

Simple assignments:

[sh]
    a=375
    hello=$a

[remark]
    No space permitted on either side of `=` sign when initializing variables. What happens if there is a space?

    [sh]
        VARIABLE =value
               
    Script tries to run `VARIABLE` command with one argument, `=value`.

    [sh]
        VARIABLE= value

    Script tries to run `value` command with the environmental variable `VARIABLE` set to `""`.

[sh]
    echo hello    # Not a variable reference, just the string "hello"
    echo $hello   # This *is* a variable reference.
    echo ${hello} # Likewise a variable reference, as above.

    echo "$hello"    # double quotes allow variable expansion
    echo "${hello}"  # likewise

Difference between quoted and unquoted: quoting a variable preserves whitespace.

[sh]
    hello="A B  C   D"
    echo $hello   # A B C D
    echo "$hello" # A B  C   D

If there is whitespace embedded within a variable, then quotes are necessary.

[sh]
    numbers="one two three 
    other_numbers="1 2 3"
    other_numbers=1 2 3          # Gives an error message.
    mixed_bag=2\ ---\ Whatever   # Escaping the whitespace also works

Single quotes don't allow variable expansion:

[sh]
    echo '$hello'  # $hello

Null variables (variables with null value) are not the same thing as undefined (undeclared) variables.

[st]
    hello=                 # Setting variable to a null value.
    echo "hello = $hello"  # Null variable
    echo "world = $world"  # Undeclared variable; also has null value
    unset hello            # Now 'hello' is also undeclared

Type system
-----------

Bash variables are untyped with all following consequences: all bash variables are strings, but, depending on context, Bash permits arithmetic operations and comparisons on variables.

[sh]
    a=2334                   # Integer.
    let "a += 1"
    echo "a = $a "           # a = 2335
    echo                     # Integer, still.


    b=${a/23/BB}             # Substitute "BB" for "23".
                             # This transforms $b into a string.
    echo "b = $b"            # b = BB35
    declare -i b             # Declaring it an integer doesn't help.
    echo "b = $b"            # b = BB35

    c=BB34
    echo "c = $c"            # c = BB34
    d=${c/BB/23}             # Substitute "23" for "BB".
                             # This makes $d an integer.
    echo "d = $d"            # d = 2334
    let "d += 1"             # 2334 + 1
    echo "d = $d"            # d = 2335

Integer values of strings, undefined and null variables is equal to zero:

[sh]
    let "b += 1"             # BB35 + 1
    echo "b = $b"            # b = 1
    echo                     # Bash sets the "integer value" of a string to 0.

    # What about null variables?
    e=''                     # ... Or e="" ... Or e=
    echo "e = $e"            # e =
    let "e += 1"             # Arithmetic operations allowed on a null variable?
    echo "e = $e"            # e = 1
    echo                     # Null variable transformed into an integer.

    # What about undeclared variables?
    echo "f = $f"            # f =
    let "f += 1"             # Arithmetic operations allowed?
    echo "f = $f"            # f = 1
    echo                     # Undeclared variable transformed into an integer.

However, don't rely on undefined or null variable being zero in any expression:

[sh]
    let "f /= $undecl_var"   # Divide by zero?
    #   let: f /= : syntax error: operand expected (error token is " ")
    # Syntax error! Variable $undecl_var is not set to zero here!

    let "f /= 0"
    #   let: f /= 0: division by 0 (error token is "0")
    # Expected behavior.

Scope
-----

All Bash variables are *local* by default, i.e. visible only in local function.

An `export` makes local variable an *environmental* variable, i.e. it becomes visible in the environment of current interpreter process.

A script can export variables only to child processes, that is, only to commands or processes which that particular script initiates. A script invoked from the command-line cannot export variables back to the command-line environment. *Child processes cannot export variables back to the parent processes that spawned them.*

Special variables
-----------------

- Positional parameters `$1`, ..., `$9`, `${10}` (not `$10`!) and their count, array and IFS representations `$#`, `$@` and `$*`;
- Script name (as was invoked from command line) or shell name `$0`;
- Most recent foreground pipeline exit status `$?`;

`shift [n]` shifts positional parameters by n positions.

Less frequently used:

- `$!` PID of the most recent background command;
- `$$` PID of the current shell (not subshell);
- `$-` current options set for the shell;
- `$IFS` input field separator;
- `$_` -- ? 















- `:` is builtin placeholder for `true` program.
































Bash
====

Disambiguating
--------------

"--" separator

sh -c (sudo, env, ...)

running built-in routines as commands (nice, env, ...)

Delaying
========

sleep
-----

Print utilities
===============
    
echo
----

printf
------

yes
---

Conditions
==========

true
----

false
-----

test
----

expr
----

Filename manipulation
=====================

basename
--------

dirname
-------

pathchk
-------

mktemp
------

realpath
--------

Numeric utilities
=================

factor
------

Print prime factors of each specified integer.

[code]
    factor [NUMBER]...

seq
---

Print a sequence of numbers.

[code]
    seq [OPTION]... LAST
    seq [OPTION]... FIRST LAST
    seq [OPTION]... FIRST INCREMENT LAST
    
    -s, --separator=STRING      default: \n
    -f, --format=FORMAT         use printf-like floating-point format
    -w, --equal-width           pad with zeros to equalize width
