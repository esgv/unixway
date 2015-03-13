========
Difftils
========

[default_span] code

General information
===================

diff notes
----------

- Groups of differing lines are called **hunks**;
- `diff` compares files line-by-line;
- First, `diff` throws away common prefix and common suffix. Then, it searches
  for LCS in remaining lines. Left are the hunks;
- "Ignore blank lines" option means "ignore all hunks, where all additions and 
  deletions are blank lines". "Ignore lines, matching regexp" option means 
  "ignore all hunks, where all additions and deletions match rexexp", and so on;
- Before the first and after the last change in each hunk, diff displays 3 
  **context** unchanged lines by default;
- Line with no newline on the end is called **incomplete**. `diff` prints 
  `\ No newline at end of file` in these cases;
- There are multiple formats of diff output, but only unified diff is 
  interesting, since it's used for distributing source code patches.

patch notes
-----------

- Usually, `patch` recognizes diff format, but explicit `-u` may be given to 
  specify unified format;
- Patch skips leading trash. So, eg. one can apply diff, recieved by email by 
  feeding `patch` the raw email message;
- `patch` can detect reverse diffs. First, it tries to apply first hunk: if 
  failed, it tries to apply it in reverse, and if succeeded, asks user if diff 
  is reversed;
- More of that: when applying same patch two times, second application cancels 
  first, since it will be reversed;
- Patch tries to take lines, mentioned in the hunk, and then do the match. 
  If the match cannot be made, `patch` scans forwards and backwards, trying to 
  match context lines. If that also failed, it makes another scan, ignoring 
  first and last lines of the context; then first and last two lines of the 
  context, and so on, until the maximum **fuzz factor**;
- If all lines of the file are deleted in diff, file won't be removed (unless 
  `--remove-empty-files`). File will be removed only when new file will be 
  `/dev/null` or empty and dated the Epoch (1970-01-01 00:00:00 UTC);
- When `patch` updates a file, it sets its mtime to `now`.

Unified diff format
-------------------

Here's example of unified diff:

[diff]
     --- lao   2002-02-21 23:30:39.942229878 -0800
     +++ tzu   2002-02-21 23:30:50.442260588 -0800
     @@ -1,7 +1,6 @@
     -The Way that can be told of is not the eternal Way;
     -The name that can be named is not the eternal name.
      The Nameless is the origin of Heaven and Earth;
     -The Named is the mother of all things.
     +The named is the mother of all things.
     +
      Therefore let there always be non-being,
      so we may see their subtlety,
      And let there always be being,
     @@ -9,3 +8,6 @@
      The two are the same,
      But after they are produced,
      they have different names.
     +They both may be called deep and profound.
     +Deeper and more profound,
     +The door of all subtleties!

Specifically,

[diff]
    --- OLD_FILE TIMESTAMP
    +++ NEW_FILE TIMESTAMP
    @@ -HUNK_START_OLD,HUNK_END_OLD +HUNK_START_NEW,HUNK_END_NEW
    -Deleted line,
    -I.e. present only in OLD_FILE.
    +Added line,
    +I.e. present only in NEW_FILE.
    Common line,
    I.e. present in both files.

diff
====

Invocation
----------

Compare two files line-by-line.

[code]
    diff [OPTION]... OLD_FILE NEW_FILE
    diff [OPTION]... OLD_FILE NEW_DIR       (and vice versa)
    diff [OPTION]... OLD_DIR NEW_DIR

    Second finds OLD_FILE in NEW_DIR and compares two versions.
    Third compares all immediate children, but not goes deeper.
    For generating patches, use:

                    diff -Naur OLD_DIR NEW_DIR            (linux)
                    diff -Naur --binary OLD_DIR NEW_DIR   (others)

    MAIN
        -u, --unified[=LINES]       use unified format, select #lines of context (3)
        -r, --recursive             recurse into subdirectories
        -N, --new-file              show full diff for files, that are in one directory,
                                    but not the other; otherwise diff just reports absence
        -x, --exclude=PATTERN       don't scan these files; can be used multiple times
        -X, --exclude-from=FILE     exclude from eg. gitignore
        -a, --text                  treat all files as text and compare line-by-line
        --binary                    read and write files in binary mode (keeps newlines)
                                    except stdout and /dev/tty
        --strip-trailing-cr         convert newlines to UNIX

    IGNORING CHANGES
        -E, --ignore-tab-expansion          TAB = #spaces to next tab stop
        -Z, --ignore-trailing-space
        -b, --ignore-space-change           stronger than -EZ: all blank sequences are eqv.
        -w, --ignore-all-space              "experts exchange" = "expert sex change"
        -B, --ignore-blank-lines            
        -I, --ignore-matching-lines=REGEXP  regexp is GREP-style
        -i, --ignore-case

    HUMANS
        -F, --show-function-line=REGEXP     show nearest preceding, unchanged line
                                            matching REGEXP with each hunk
                                            eg. "^[[:alpha]_]" for C++ or Python
        -p, --show-c-function
        -s, --report-identical-files
        --label=OLLABEL --label=NULABEL     use labels for files instead of filenames 
        -y, --side-by-side                  print diff in 2 columns
        -W, --width-columns=WIDTH           specify width of those columns (default: 130)
        --left-column, --right-column       print only one column
        
    MISC
        -q, --brief                 print whether files differ, don't print WHERE they do           
        -s, --quiet                 status code indicates differences
        -t, --expand-tabs           needs "--ignore-white-space"
        --tabsize=COLS              (default: 8)

        -T, --initial-tab           use TAB instead of space in unchanged lines
                                    TAB won't shift tabstops, space might do that
        --suppress-blank-empty      when line is empty and unchanged (common to both files);
                                    don't print space at the start of the output line

        -S, --starting-file=FILE    resume stopped diff on FILE
        -d, --minimal               try to find minimal set of changes
        --speed-large-files         use algorithm, fast for small density of changes within 
                                    single file
        --horizon-lines=LINES       leave LINES lines from common suffix and prefix;
                                    helps to find minimal diff                                    
            
Merging with if-then-else
-------------------------

Didn't need this yet.
                                              
patch
=====

Apply a diff file to an original.

[code]
    patch <PATCHFILE
    patch [OPTION]... [ORIGFILE [PATCHFILE]]

    MAIN
        -d, --directory=DIR             apply in DIR, not cwd
        -p, --strip=NUM                 strip NUM slashes (and dirs between) from paths in diff
                                        eg. "/mnt/data" -> "mnt/data" with -p1
        --binary                        read and write in binary mode
        --dry-run
        -Z, --set-utc                   update timestamps to ones, specified in diff
        -i, --input=PATCHFILE           use file instead of stdin
        -o, --output=FILE               use FILE as output filename

    IMPERFECT PATCHES
        -l, --ignore-white-space        ignore whitespace when trying to match context in hunks        
        -T, --set-time                  assume timestamps are in local time
        -E, --remove-empty-files        remove files when they become empty 
                                        (BAD for python __init__.py files)
        -F, --fuzz=LINES                set fuzz factor (default: 3)
        -R, --reverse                   assume diff is reversed
        -N, --forward                   assume diff is not reversed
        -t, --batch                     like force, but check for reverseness
        -f, --force                     * diff not checked for being reversed
                                        * timestamp is updated when using fuzz factor
                                        * timestamp is updated when actual timestamp
                                          and diff's OLD timespamp are different
                                        * skip patches with no file names

        -quoting-style=STYLE            filename quoting style within diagnostic messages
            literal                         as-is
            shell                           quote for shell when needed
            shell-always                    quote for shell always
            c                               quote as c string (with double quotes)
            escape                          quote as c string (without double quotes)
                   
    BACKUP
        -b, --backup                    always make backup
        --backup-if-mismatch            backup fuzzy files        
        --no-backup-if-mismatch         don't backup even fuzzy files
        -B, --prefix=PREFIX             prefix for all backups; can be directory
        -Y, --basename-prefix=PREFIX    "dir/file.c" -> "dir/~file.c" with "-Y~"
        -z, --suffix=SUFFIX             suffix for simple backups (default: ".orig" or "~")

        -V, --version-control=STYLE     numbered backup style
            t, numbered                 ".~1~", ".~2~", ...
            nil, existing               numbered for existing backups, simple for non-exising
            never, simple               always make simple backups
        
        -r, --reject-file=FILE          use FILE instead of filename.rej for rejected hunks
        <by default, when patching 'filename', place rejected hunks into 'filename.rej'>

cmp
===

Compare two files byte-by-byte.

[code]
    cmp [OPTION]... FROM_FILE [TO_FILE [FROM_SKIP [TO_SKIP]]]

    --ignore-initial=FROM_SKIP:TO_SKIP      skip some prefix bytes
    --ignore-initial=BOTH_SKIP
    -n, --bytes=COUNT                       compare at most COUNT bytes
    
    <default>                               print only position of first differing byte
    -l, --verbose                           output all differing bytes instead of first
    -b, --print-bytes                       print differing byte values, not only positions

diff3
=====

Compare three files (common base and two separately derived versions) 
line-by-line. RTFM if you ever need this.

sdiff
=====

Interactively merge files. See manual if you ever need this.

