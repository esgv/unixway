# System utilities #

## File manipulation ##

- [ls](#ls)
- [mv](#mv)
- [cp](#cp)
- [rm](#rm)
- [mkdir](#mkdir)
- [rmdir](#rmdir)

    mv SRC DEST             move SRC to DEST
    rm -r  DIR...           recursively delete directories
    rf -rf DIR...           same, but delete read-only files
    mkdir -pv DIR...        create dirs (with parents) and report
    rmdir DIR...            ensure, that directory is empty before deletion

### ls ###

### mv ###

Move (rename) files.


    mv [OPTION]... SRC DEST
    mv [OPTION]... SRC... DIR
    mv [OPTION]... -t DIR SRC...

    -f, --force        don't prompt before overwriting
    -i, --interactive  prompt before overwriting
    -n, --no-clobber   don't overwrite existing file

    -v, --verbose
    -T, --no-target-directory   treat DEST as normal file
    -t, --target-directory=DIR  move all SRC arguments into DIR

    * Can backup existing files.

### cp ###

### rm ###

Delete files and folders.

    rm [OPTION]... FILE...

    -f, --force            ignore nonexisting files
    -r, -R, --recursive    recursively delete directories
    -v, --verbose          print name of each file before removing it
    --one-file-system      stay within file system, that each argument is on

    * Scripting

      -I, --interactive=once      prompt once before deleting all files
      -i, --interactive=always    prompt before deleting each file
      --interactive=never         this is default
      --preserve-root             protect from "rm -rf /"; default
      --no-preserve-root          bad idea possibly

### mkdir ###

Create empty directory.

    mkdir [OPTION]... DIR...

    -m, --mode=MODE       set mode bits of new directory
    -p, --parents         create parents
    -v, --verbose         print message for each created dir; useful with "-p"

### rmdir ###

Remove empty directory.

    rmdir [OPTION]... DIR...

    -p, --parents               delete empty parents
    -v, --verbose
    --ignore-fail-on-non-empty


## Special file utilities ##

### file ###

### Manipulating links ###

### link/unlink/ln/readlink ###

### touch ###

### dd ###

### mkfifo ###

Create FIFO.

    mkfifo [OPTION]... FILE...

    -m, --mode=MODE              new FIFO permissions

### mknod ###

Make FIFO, char or block special file.

**Special file** is somethig that can generate or recieve data.

    mknod [OPTION]... NAME TYPE [MAJOR MINOR]

    -m, --mode=MODE             guess what this does


    * MAJOR or MINOR might be hex.
    * MAJOR and MINOR are mandatory for block and char files.
    * Types

      p   FIFO
      b   block special file
      c   character special file

### truncate ###

Shrink or extend the size of a file.

Extended bytes are filled with zeros.

[code]
    truncate [OPTION]... [FILE]...

    -s, --size=SIZE             size to truncate or extend to
    -c, --no-create             don't create nonexistent files
    -o, --io-blocks             treat SIZE as # of IO blocks, not bytes
    -r, --reference=RFILE       truncate to size of RFILE

    Also, SIZE may be prepended by
        +                       extend by
        -                       reduce by
        <                       at most
        >                       at least
        /                       round DOWN to multiple of
        %                       round UP to multiple of

sync
----

Write out in-memory disk cache.

[code]
    sync

shred
-----

Users and groups
================

chmod
-----

su
--

who
---

chgrp
-----

chown
-----

id
--

logname
-------

Print the calling user's name, as found in a system-maintained file (often
`/var/run/utmp` or `/etc/utmp`).

[code]
    logname

whoami
------

groups
------

users
-----

System information
==================

Summary
-------

[code]
    hostname [NAME]     print or set current host name
    hostid              print HEX host identifier (usually, bound to IP address)
    uptime              print current time, uptime, #logged-in users and load average
    arch                print machine hardware name (equivalent to `uname -m`)
    tty                 print the filename of terminal connected to stdin
    pwd                 print the name of current directory
    env                 print all envorinment variables
    nproc               print number of available processors

    df -h               report disk usage for every mounted volume (with human-readable prefixes)
    du -sh FILE...      summarize disk usage (non-recursively, with human-readable prefixes)
    uname -a            print all system information

df
--

Report disk usage.

[code]
    df [OPTION]... [FILE]...

    By default, report on each mounted volume.
    If FILEs are given, report on each filesystem, any of FILEs is on.
    Reported in kB.

    -h, --human-readable        use 1024-prefixes: K, M, G, ...
        --total                 print totals (across all drives)
    -i, --inodes                report inode usage instead of byte usage
    -T, --print-types           print filesystem types

    SELECTING FILESYSTEMS
            --all                   also report dummy filesystems
        -l, --local                 list only local filesystems
        -t, --type=FSTYPE           include only FSTYPE (many -t options can be given)
        -x, --exclude-type=FSTYPE   exclude FSTYPE

    --sync                      invoke sync before gathering data
    --no-sync                   this is the default

du
--

Summarize disk usage of each FILE, recursively for directories.

[code]
    du [OPTION]... [FILE]...

    -s, --summarize                              display only a total for each argument
    -h, --human-readable                         print sizes in human-readable format
        --apparent-size                          print apparent sizes rather than disk usages
    -x, --one-file-system                        skip directories on different file systems
        --exclude=PATTERN                        exclude files that match PATTERN
    -d, --max-depth=N                            don't show size of directories below N levels
        --time[=atime|access|use|ctime|status]   show modification time along with size
    -S, --separate-dirs                          do not include size of subdirectories
    -c, --total                                  produce a grand total
    -X, --exclude-from=FILE

uname
-----

Print system information.

[code]
    uname [OPTION]...

    -a, --all
    -i, --hardware-platform     "unknown" on Linux          unknown
    -m, --machine               same as arch, eg.           i686
    -n, --nodename              print hostname              melchior-main
    -p, --processor             "unknown" on Linux          unknown
    -o, --operating-system      print the OS name           GNU/Linux
    -r, --kernel-release                                    2.6.32-5-686
    -s, --kernel-name                                       Linux
    -v, --kernel-version                                    #1 SMP Sun May 6 04:01:19 UTC 2012

printenv
--------

Print environment variables.

If variable names are given, print only values for defined vars, and nothing for undefined.

[code]
    printenv [VARIABLE] ...

stat
----

date
----

nproc
-----

Print number of processors, AVAILABLE to current process.

[code]
    nproc [OPTION]

    AVAILABLE processors < ONLINE processors < INSTALLED processors
    $OMP_NUM_THREADS overrides AVAILABLE and ONLINE

    <default>                   print #AVAILABLE, or #INSTALLED, if info inaccessible
    --all                       print number of INSTALLED processors

fuser
-----

lsof
----

Finding stuff
=============

find
----

which
-----

Locate a command. `which` returns the pathnames of the files (or links) which
would be executed in the current environment, had its arguments been given as
commands in a strictly POSIX-conformant shell. It does this by searching the
`PATH` for executable files matching the names of the arguments. It does not
follow symbolic links.

[code]
    which [-a] FILENAME...

    -a             print all matching pathnames of each argument

Invocation
==========

xargs
-----

chroot
------

Invoke command with root directory changed.

On many systems, only superuser can do that.

[code]
    chroot [OPTION]... NEWROOT [COMMAND [ARGS]...]

    --userspec=USER[:GROUP]     specify user and group of new process
    --groups=GRP1,GRP2,...      specify supplementary groups

    When invoking dynamically linked binaries, don't forget to
    add shared libraries to new root.

env
---

Run command with modified environment.

[code]
    env [OPTION]... [NAME=VALUE]... [CMD [ARGS]...]

    With no CMD specified, print resulting environment.
    Env. var's name can contain ANY chars, except =.

    -, -i, --ignore-environment     begin with an empty environment
    -u, --unset=NAME                unset a variable

nice
----

Run process with modified niceness (+10 by default).

Only root can decrease niceness.

[code]
    nice [OPTION]... [CMD [ARG]...]

    <no command>                print current niceness
    -n, --adjustment=[+-]NUM    number to add to current niceness

    Niceness ranges from -20 to +19 (or wider).
    If resulting niceness is larger than supported, max value is used:

            $ nice -n 10000 nice
            19

nohup
-----

Run a command, immune to HUP (user logout) signals.

[code]
    nohup CMD [ARG]...

    If STDOUT is console, append output to $HOME/nohup.out.
    If STDIN is console, automatically redirect input from /dev/null.

timeout
-------

Run a command with a time limit. Send a signal, when time limit exceeds.

[code]
    timeout [OPTION]... DURATIeON CMD [ARG]...

    -s, --signal=SIG            signal to send
    -k, --kill-after=DURATION   in addition, send KILL after DURATION

    --foreground                don't create background program group, which results in:
        * Ability to use console.
        * Ability to kill program via Ctrl-C (other key combos also available).
        * Child processes not being killed (controlled/timed out).

stdbuf
------

Run a command with modified IO buffering.

[code]
    stdbuf [OPTION]... CMD [ARG]...

    * Program must use C FILE streams for IO (dd and cat don't do that).
    * Program shouldn't adjust buffering by itself (tee doesn't comply).

    -i, --input=MODE            STDIN
    -o, --output=MODE           STDOUT
    -e, --error=MODE            STDERR

    MODE
        L                       line buffering
        0                       disable buffering (write/read as soon as data available)
        SIZE                    set buffer size to SIZE

Manipulating processes
======================

kill
----

Send a signal to a process (`SIGKILL` by default).

[code]
    kill -SIG PID
    kill -l [SIG]...

    -s, --signal=SIG, -SIG      specify signal to send
    -l, --list                  translate signal names to numbers;
                                if no signal given, list available signals

killall
-------

pgrep, pkill
------------

pidof
-----

Find the PID of a running program by executable name.

[code]
    pidof [OPTION]... PROGRAM...

    -s                          single-shot; print only one PID (one for all args)
    -x                          scripts also
    -o OMITPID, ...             exclude OMITPID from search; %PPID can be used for pidof invoker
    -c                          include only processes with same root (requires root access)

ps, top
-------
