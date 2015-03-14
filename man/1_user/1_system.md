# System utilities #

- [File manipulation](#file-manipulation)
- [Special file utilities](#special-file-utilities)
- [Users and groups](#users-and-groups)
- [System information](#system-information)
- [Finding stuff](#finding-stuff)
- [Invocation](#invocation)
- [Manipulating processes](#manipulating-processes)

<!--===========================================================================
                              File manipulation
-->

## File manipulation ##

- [ls](#ls)
- [mv](#mv)
- [cp](#cp)
- [rm](#rm)
- [mkdir](#mkdir)
- [rmdir](#rmdir)

Some recipes:

    ls                      list files
    ls -lah                 list all files verbosely
    ls -la                  same, but don't round sizes to MB, GB, etc.

    mv SRC DEST             move SRC to DEST

    cp -r SRC DEST          copy recursively SRC to DEST
    cp -pr SRC DEST         copy and preserve mtime

    rm -r  DIR...           recursively delete directories
    rm -rf DIR...           same, but delete read-only files

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

    * Can backup existing files (see man).

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

<!---==========================================================================
                             Special file utilities
-->

## Special file utilities ##

- [file](#file)
- [ln, link, unlink, readlink](#ln-link-unlink-readlink)
- [dd](#dd)
- [mkfifo](#mkfifo)
- [mknod](#mknod)
- [truncate](#truncate)
- [sync](#sync)
- [shred](#shred)

### file ###

### ln, link, unlink, readlink ##

### touch ###

### dd ###

### mkfifo ###

Create FIFO.

    mkfifo [OPTION]... FILE...

    -m, --mode=MODE              new FIFO permissions

### mknod ###

Make FIFO, char or block special file.

**Special file** is something that can generate or recieve data.

    mknod [OPTION]... NAME TYPE [MAJOR MINOR]

    -m, --mode=MODE             guess what this does

    * MAJOR or MINOR might be hex.
    * MAJOR and MINOR are mandatory for block and char files.
    * Types

      p   FIFO
      b   block special file
      c   character special file

### truncate ###

Shrink or extend the size of a file. Extended bytes are filled with zeros.

    truncate [OPTION]... [FILE]...

    -s, --size=SIZE             size to truncate or extend to
    -c, --no-create             don't create nonexistent files
    -o, --io-blocks             treat SIZE as # of IO blocks, not bytes
    -r, --reference=RFILE       truncate to size of RFILE

    * Also, SIZE may be prepended by

      +     extend by
      -     reduce by
      <     at most
      >     at least
      /     round DOWN to multiple of
      %     round UP to multiple of

### sync ###

Write out in-memory disk cache.

    sync

### shred ###

<!---==========================================================================
                               Users and groups
-->

## Users and groups ##

- [chmod](#chmod)
- [su](#su)
- [who](#who)
- [chgrp](#chgrp)
- [chown](#chown)
- [id](#id)
- [logname](#logname)
- [whoami](#whoami)
- [groups](#groups)
- [users](#users)

### chmod ###

### su ###

### who ###

### chgrp ###

### chown ###

### id ###

### logname ###

Print the calling user's name, as found in a system-maintained file (often
``/var/run/utmp`` or ``/etc/utmp``).

    logname

### whoami ###

### groups ###

### users ###

<!---==========================================================================
                              System information
-->

## System information ##

- [df](#df)
- [du](#du)
- [uname](#uname)
- [printenv](#printenv)
- [stat](#stat)
- [date](#date)
- [nproc](#nproc)
- [fuser](#fuser)
- [lsof](#lsof)

Summary:

    hostname [NAME]     print or set current host name
    hostid              HEX host identifier (usually bound to IP address)
    uptime              current time, uptime, #logged-in users and load average
    arch                machine hardware name (equivalent to `uname -m`)
    tty                 filename of terminal connected to stdin
    pwd                 the name of current directory
    env                 all envorinment variables
    nproc               number of available processors

    df -h               report disk usage for every mounted volume
    df -h .             report disk usage for the volume current folder is on
    du -csh FILE...     summarize disk usage (non-recursively)
    uname -a            print all system information

### df ###

Report disk usage.

    df [OPTION]... [FILE]...

    * By default, report on each mounted volume. If FILEs are given, report on
      each filesystem, any of FILEs is on.
    * Reported in kB.

    -h, --human-readable        use 1024-prefixes: K, M, G, ...
        --total                 print totals (across all drives)
    -i, --inodes                report inode usage instead of byte usage
    -T, --print-types           print filesystem types
    --sync                      invoke sync before gathering data
    --no-sync                   this is the default

    * Selecting filesystems

          --all                   also report dummy filesystems
      -l, --local                 list only local filesystems
      -t, --type=FSTYPE           include only FSTYPE (can be repeated)
      -x, --exclude-type=FSTYPE   exclude FSTYPE

### du ###

Summarize disk usage of each FILE, recursively for directories.

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

### uname ###

Print system information.

    uname [OPTION]...

    -a, --all
    -i, --hardware-platform     "unknown" on Linux          unknown
    -m, --machine               same as arch, eg.           i686
    -n, --nodename              print hostname              myhost
    -p, --processor             "unknown" on Linux          unknown
    -o, --operating-system      print the OS name           GNU/Linux
    -r, --kernel-release                                    2.6.32-5-686
    -s, --kernel-name                                       Linux
    -v, --kernel-version                                    #1 SMP Sun May 6 04:01:19 UTC 2012

### printenv ###

Print environment variables.

    printenv [VARIABLE] ...

    * If variable names are given, print only values for defined vars, and
      nothing for undefined.

### stat ###

### date ###

### nproc ###

Print number of processors *available to current process*.

    nproc [OPTION]

    <default>           print #AVAILABLE, or #INSTALLED, if info inaccessible
    --all               print number of INSTALLED processors

    * AVAILABLE processors < ONLINE processors < INSTALLED processors
    * $OMP_NUM_THREADS overrides AVAILABLE and ONLINE

### fuser ###

### lsof ###

<!---==========================================================================
                                Finding stuff
-->

## Finding stuff ##

- [find](#find)
- [which](#which)

### find ###

### which ###

Locate a command. `which` returns the pathnames of the files (or links) which
would be executed in the current environment, had its arguments been given as
commands in a strictly POSIX-conformant shell. It does this by searching the
`PATH` for executable files matching the names of the arguments. It does not
follow symbolic links.

    which [-a] FILENAME...

    -a             print all matching pathnames of each argument

<!---==========================================================================
                                  Invocation
-->

## Invocation ##

### xargs ###

### chroot ###

Invoke command with root directory changed.

On many systems, only superuser can do that.

    chroot [OPTION]... NEWROOT [COMMAND [ARGS]...]

    --userspec=USER[:GROUP]     specify user and group of new process
    --groups=GRP1,GRP2,...      specify supplementary groups

    When invoking dynamically linked binaries, don't forget to
    add shared libraries to new root.

### env ###

Run command with modified environment.

    env [OPTION]... [NAME=VALUE]... [CMD [ARGS]...]

    With no CMD specified, print resulting environment.
    Env. var's name can contain ANY chars, except =.

    -, -i, --ignore-environment     begin with an empty environment
    -u, --unset=NAME                unset a variable

### nice ###

Run process with modified niceness (+10 by default).

Only root can decrease niceness.

    nice [OPTION]... [CMD [ARG]...]

    <no command>                print current niceness
    -n, --adjustment=[+-]NUM    number to add to current niceness

    Niceness ranges from -20 to +19 (or wider).
    If resulting niceness is larger than supported, max value is used:

            $ nice -n 10000 nice
            19

### nohup ###

Run a command, immune to HUP (user logout) signals.

    nohup CMD [ARG]...

    If STDOUT is console, append output to $HOME/nohup.out.
    If STDIN is console, automatically redirect input from /dev/null.

### timeout ###

Run a command with a time limit. Send a signal, when time limit exceeds.

    timeout [OPTION]... DURATIeON CMD [ARG]...

    -s, --signal=SIG            signal to send
    -k, --kill-after=DURATION   in addition, send KILL after DURATION

    --foreground                don't create background program group, which results in:
        * Ability to use console.
        * Ability to kill program via Ctrl-C (other key combos also available).
        * Child processes not being killed (controlled/timed out).

### stdbuf ###

Run a command with modified IO buffering.

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

<!---==========================================================================
                             Manipulating processes
-->

## Manipulating processes ##

### kill ###

Send a signal to a process (`SIGKILL` by default).

    kill -SIG PID
    kill -l [SIG]...

    -s, --signal=SIG, -SIG      specify signal to send
    -l, --list                  translate signal names to numbers;
                                if no signal given, list available signals

### killall ###

### pgrep, pkill ###

### pidof ###

Find the PID of a running program by executable name.

    pidof [OPTION]... PROGRAM...

    -s                          single-shot; print only one PID (one for all args)
    -x                          scripts also
    -o OMITPID, ...             exclude OMITPID from search; %PPID can be used for pidof invoker
    -c                          include only processes with same root (requires root access)

### ps, top ###
