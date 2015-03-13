=========
Coreutils
=========

[default_span] code

Concatenating
=============

cat
---

Concatenate files and print on the stdout.

[code]
    cat [OPTION]... [FILE]...       
       
    -A                          show non-printing chars
    -v                          show non-printing chars except line ends and tabs
    
    If one of the options has been specified, read and write in text mode.
    (binary mode by default).
    
tac
---
    
Concatenate, then print lines in reverse.
    
[code]
    tac [OPTION]... [FILE]...
    
    -s, --separator=STRING      specify separator
    -r                          treat separator as regex

tee
---

T-pipe splitter: read stdin and write to files and stdout.

[code]
    tee [OPTION]... [FILE]...

    -a, --append                append to given files, not overwrite
    -i, --ignore-iterrupts      ignore interrupt signals

wc
--

Count words/lines/bytes for each file.

[code]
    wc [OPTION]... [FILE]...
    
    -c, --bytes                 
    -m, --chars                 
    -l, --lines                 
    -w, --words                 
    -L, --max-line-length       
    
    default: --lines --words --chars
    
Formatting
==========

fold
----

Wrap each input line to fit in specified width.

[code]
    fold [OPTION]... [FILE]...
    
    -w, --width=WIDTH           default: 80
    -s, --spaces                break at spaces
    -b, --bytes                 count bytes rather than chars
    
fmt
---

Smart `fold` for texts.

- Blank lines, spaces between words, indentation are preserved (by default);
- Successive lines with different indentation are not joined;
- Tabs are expanded on input and introduced on output;
- Prefers breakng lines at the end of a sentence;
- Avoids breaking line after the first word of a sentence or after the last word of a sentence;

[code]
    fmt [OPTION]... [FILE]...
    
    -w, --width=WIDTH           default: 75 or GOAL+10, if goal is provided
    -g, --goal=GOAL             initially try to make GOAL characters wide;
                                default: 7% shorter than WIDTH
                                
    -s, --split-only            don't join short lines; good eg. for code
    -u, --uniform-spacing       make 1 space between words, 2 spaces between sentences
    -c, --crown-margin          some weird modes, see man
    -t, --tagged-paragraph

pr
--

Another weird utility for paginating texts for printing.

ptx
---

Produce permuted index: put each keyword in context. Weird and complicated utility.

Char translation
================

tr
--

Translate or delete characters.

[code]  
    tr [OPTION]... SET1 [SET2]
    
    <specify two sets>          translate between sets
    -d                          delete chars in SET1
    -s, --squeeze-repeats       squeeze repeated chars in input, if listed in SET1
                                If neither deleting nor translating, uses SET1.
                                Else, uses SET2 and occurs AFTER translation or deletion.
    
    SPECIFYING SETS
        Sets are specified as string of characters. 
        
        \NNN                            octal NNN
        \\                              backslash
        \a, \b, \f, \n, \r, \t, \v      ASCII escapes
        
        CHAR1-CHAR2                     range in ascending order
        [CHAR*]                         in SET2, copies CHAR until length of SET1
        [CHAR*REPEAT]
        [=CHAR=]                        all equivalent to CHAR
        
        [:print:]                       all printable chars, including space
            [:graph:]                   all printable chars, NOT including space
                [:alnum:]
                    [:alpha:]
                        [:lower:]
                        [:upper:]
                    [:digit:]
                    [:xdigit:]          HEX digits
                [:punct:]               punctuation
            [:space:]                   horizontal or vertical whitespace
                [:blank:]               horizontal whitespace
        [:cntrl:]                       control characters
            
        SET2 is extended to length of SET1 by repeating its last char. 
        Excess chars of SET2 are ignored. Also,
    
        -c, -C, --complement            use the complement of SET1
        -t, --truncate-set1             truncate SET1 to length of SET2

expand/unexpand
---------------

Convert tabs to spaces (expand) or spaces to tabs (unexpand).

[code]
    expand [OPTION]... [FILE]...
    unexpand [OPTION]... [FILE]...
    
    EXPAND ONLY
        -i, --initial               do not convert blanks after non-blanks
    
    UNEXPAND ONLY
        -a, --all                   convert all blanks instead of just initial
        --first-only                convert only initial blanks
        
    -t, --tabs=NUMBER           specify tab width
    -t, --tabs=POS1,POS2,...    specify tab positions
     
tofrodos
--------

Convert text files' line endings between DOS and Unix formats.

[code]
    todos [OPTION]... [FILE]...
    fromdos [OPTION]... [FILE]...
    
    -d                          always convert to DOS
    -u                          always convert to Unix
    
    -p                          preserve ownership and mtime
    -v                          verbose
    -b                          make backup (filename.bak)
    
Splitting and merging
=====================
 
head
----

Prints first 10 lines of each file.

[code]
    head [OPTION]... [FILE]...
    
    -c, --bytes=[-]NUM          with the leading '-', print all BUT last NUM bytes
    -n, --lines=[-]NUM
    -q, --quiet                 don't print file headers
    -v, --verbose               print file headers
    
tail
----

Prints last 10 lines of each file.

[code]    
    tail [OPTION]... [FILE]...
    
    FOLLOW METHODS
        -f                          follow by desc
        -F                          follow by name, implies --retry
        
    FOLLOW OPTIONS
        --follow=HOW        loop forever, trying to read more at the end of the file; 
        
        --retry                 without this, when following by name and file doesn't exist, 
                                fact is reported, and tail doesn't poll it anymore
                                
        --sleep-interval=SECS   check for file updates and PID vitals every SECS seconds
        
        --pid=PID               terminate after PID terminates
        
        --max-unchanged-stats=N when following by name, if after N stat's file haven't
                                changed, then update its inode/device pair
        
    FOLLOW METHODS
        descriptor              default
        name                    periodically reopen file; useful when following rotating logs
        
    Also, inherits head options.

split
-----

Split file into several chunks.

[code]
    split [OPTION]... [INPUT [PREFIX]]
    
    CHUNK NAMES
        <default>                       chunks are named PREFIXaa, PREFIXab, ...
        -d, --numeric-suffixes[=FROM]   chunks are named PREFIX00, PREFIX01, ...
        -a, --suffix-length=LENGTH      (default: 2)
        --additional-suffix=SUFFIX      (default: empty)
        
    SIZE
        -l, --lines=LINES               put LINES lines in each chunk
        -b, --bytes=SIZE                put SIZE byptes in each chunk
        -n, --number=CHUNKS             split to CHUNKS chunks; see also MODES
        -C, --line-bytes=SIZE           put as many lines, as possible w/o exceeding SIZE bytes
                                        if line is greater than SIZE, it will be broken
        
    ADDITIONAL MODES
        N                           split into N chunks
        l/N                         generate N files without splitting lines (MAGIC!)
        r/N                         like 'l/...', but use round-robin distribution
        K/N, l/K/N, r/K/N           generate only Kth of N chunks
        
    -e, --elide-empty-files         don't create empty files
    -u, --unbuffered                immediately write output in "r/..." mode
    --filter=COMMAND                don't write chunks: pipe them to COMMAND;
                                    COMMAND may use $FILE var.

csplit
------

Split a file line-wise, where regexp matches.

[code]
    csplit [OPTION]... INPUT PATTERN...
    
    PATTERNS
        N                           take N lines from the input
        /REGEXP/[OFFSET]            take up to (not including) line, matching REGEXP
        %REGEXP%[OFFSET]            same as above, but ignore matched lines: 
                                    don't create out file for this chunk
        {REPEATS}                   repeat previous pattern REPEATS times
        {*}                         repeat previous pattern until input is exhausted
        
    CHUNK NAMES
        -f, --prefix=PREFIX         
        -n, --digits=DIGITS         suffix length
        -b, --suffix=SUFFIX         specify printf-like suffix format, eg. "%i"
        
    Eg. 'split -n5 file.txt' is equivalent to 'csplit file.txt "5" "{*}"'.
    If csplit encounters error (eg. pattern is not matched), it deletes all output files.
    
    -z, --elide-empty-files
    -k, --keep-files                don't delete all output files on error.
    
cut
---

Print selected parts of lines.

[code]
    cut OPTION... [FILE]...

    WHERE TO CUT
        -b, --bytes=RANGE
        -c, --characters=RANGE
        -f, --fields=RANGE
        --complement            print all, BUT ranges, specified with '-bcf'
    
    -d, --delimiter=DELIM       use first byte of DELIM as field separator (default: TAB)
    --output-delimiter=DELIM    between fields with '-f', between ranges with '-bc'
    -n                          don't split multi-byte chars (DOESN'T WORK YET)
    --only-delimited            with '-f', dont print lines w/o field separator
                                such lines normally printed verbatim
                                
    SPECIFYING RANGES
        N                       Nth element (byte, char, or field); 1-based
        N-M                     range, including both ends
        -N                      means 1-N
        N-                      up to the end
        RANGE1, RANGE2          multiple ranges can be specified
        
paste
-----

Compose lines, consisting of corresponding lines of each input file, separated by TAB character.

[code]
    paste [OPTION]... [FILE]...
    
    -d, --delimiters=DELIM-LIST string of delimiter chars; reuse from beginning when exhausted
    -s, --serial                paste lines of one file at a time
    
    EXAMPLES
        $ paste num2 let3
        1   a
        2   b
            c
        
        $ paste -s num2 let3
        1   2
        a   b   c

join
----

Join two tables on a common field.

Default behaviour is the following:

* Join field is the first field.
* Fields separated by blanks; leading blanks ignored.
* Fields in output are separated by space.
* Each output line consists of join field, then remaining fields from 1st file, then remaining fields from 2nd file.

[code]
    join [OPTION]... FILE1 FILE2
    
    JOIN FIELDS
        -1 FIELD                    specify join field in FILE1
        -2 FIELD                    specify join field in FILE2
        -j FIELD                    eqv. to "-1 FIELD -2 FIELD"
        -t CHAR                     specify input and output field separator
                                    each occurrence becomes significant: "a  b" => "a", "", "b"
                                   
    INPUT
        --nocheck-order         normally, FILE1 and FILE2 should be sorted on join field!
        --check-order
        -i, --ignore-case       
        --header                treat first lines as headers
    
    OUTPUT
        -v FILE_NUM             print only unpaired lines from FILE_NUM (either 1 or 2)
        -a FILE_NUM             print unpaired lines from FILE_NUM in addition to output
        -e STRING               replace missing fields with STRING
        -o auto                 infer field format from first line: 
                                missing fields got from -e, extra fields discarded
        -o FIELD1,FIELD2        specify output fields
            1.N                     Nth field of 1st file
            2.N                     Nth field of 2nd file
            0                       join field (useful when printing unmatched lines)
            
Sorting
=======

sort
----

Sort, check sortedness, or merge sorted text lines.

[code]
    sort [OPTION]... [FILE]...

    -o, --output=FILE           it's safe to output inplace, unless merging
    --debug                     highlight keys in lines and more
    
    MODUS OPERANDI
        <default>                   sort
        -c, --check,                check for sortedness; at most 1 file
        -C, --check=quiet           don't print anything
        -m, --merge                 merge sorted files
        
    KEY
        -k, --key=STARTPOS[,ENDPOS][OPTIONS]
            * If ENDPOS is omitted, key spans till the end of line.
            * Each POS is "FIELD[.CHAR]"
                * FIELDs and CHARs indices are 1-based. 0 in ENDPOS' CHAR means "last char".
                * CHAR specifies character from the beginning of the field.
            * OPTIONS are shorthand-letters from "ORDER" and "MORE ORDER".
            * Multiple -k options may be specified at once, resulting in lexicographical sort.
        
        -t, --field-separator=SEP
            * (default): "  foo bar" => "  foo", " bar"
            * (-t " " ): "  foo bar" => "", "foo", "bar"
            * If a range of fields is specified, separators are preserved between fields!
        
    ORDER
        <default>                     key is entire line
        -n, --sort=numeric            exact floating-point. "+" or exp. notation not recognized
        -g, --sort=general-numeric    convert to long double, then sort (slower than numeric)
        -h, --sort=human-numeric      sort by sign, then by SI suffix (KMGTPEZY), then by value
        -M, --sort=month              JAN < FEB < ... < DEC
        -V, --version-sort            sort by name and version number
        -R, --sort=random             choose hash function, sort by it
                                      different from SHUF: keys with same values sorted together
                                    
        General-numeric collating sequence:
            * Lines, that don't start with numbers (all considered equal)
            * NaNs
            * -INF
            * Finite numbers with -0 = +0
            * +INF
                                    
    MORE ORDER
        -r, --reverse                 sort in descending order
        -u, --unique                  output only lines with unique keys / check for uniqueness
        -s, --stable
    
    
        -i, --ignore-nonprinting
        -b, --ignore-leading-blanks   
        -d, --dictionary-order        phone directory order: 
                                      ignore all but letters, digits and blanks
        -f, --ignore-case             fold lowercase into uppercase; 
                                      lowercase are thrown away with --unique
                                      
    PERFORMANCE    
        --compress-program=PROG       use PROG to compress temporary files
                                      from stdin to stdout, zip by default, unzip with -u
                                        
        --temporary-directory=DIR     (default: $TEMPDIR)
        
        --parallel=N                  parallel sorts (default: #processors)
        
        --batch-size=NMERGE           parallel files in one merge (default: 2)
        
        -S, --buffer-size=SIZE        in-memory INITIAL buffer size: it grows anyway
                                      50% means "50% of physical memory"
                                      
shuf
----

Generate random permutation of input lines.

[code]
    shuf [OPTION]... [FILE]...
    shuf [OPTION]... -e [ARG]...
    shuf [OPTION]... -i LO-HI
    
    <default>                   shuffle lines of input files
    -e, --echo                  shuffle arguments, specified on command line
    -i LO-HI                    shuffle integers from LO to HI
    
    -n, --head-count=NUM        output first NUM lines
    -o, --output-file=FILE      inplace shuf is OK

uniq
----

Write unique lines of given input

[code]
    uniq [OPTION]... [INPUT [OUTPUT]]
    
    -c, --count                 print number of times line occured, along with the line
    -u, --unique                print only unique lines
    -d, --repeated              print only repeated lines
    -D, --all-repeated=METHOD   print groups of repeated lines (not only first)
    
    DELIMIT METHODS
        none                don't delimit groups of lines
        prepend             newline before each group
        separate            insert newline between groups
    
    -f, --skip-fields=N         field are separated by whitespace
    -s, --skip-chars=N          fields are skipped first, then chars
    -w, --check-chars=N         check at most N chars
    -i, --ignore-case
    
    The input need not be sorted, but only adjacent repeated lines are detected.

comm
----

Compare two sorted files line-by-line.

[code]
    comm [OPTION]... FILE1 FILE2
    
    -1                          suppress 1'st column (lines, unique to FILE1)
    -2                          suppress 2'nd column (lines, unique to FILE2)
    -3                          suppress 3'rd column (lines, present in both files)
    
    --output-delimiter=STR      output delimiter between columns (default: TAB)
    --check-order
    --nocheck-order

tsort
-----

Topologially sort given file.

[code]
    tsort FILE
    
    In each line, a partial ordeing (a graph edge) is given.
    When tsort detects cycle, it writes to stdout.
    
For example,

[code]
    tsort <<EOF
    > a b c
    > d
    > e f 
    > b c d e
    > EOF
    a
    b
    c
    d
    e
    f

Encoding
========

nl
--

Number lines of files and write to stdout.

[code]    
    nl [OPTION]... [FILE]...
    
    -w, --number-width=NUMBER       specify number width
    -s, --number-separator=SEP      specify string, that will be inserted between number and line 
                                    (default: TAB)
    
    -b, --body-numbering=STYLE      use STYLE for numbering lines
    -n, --number-format=FORMAT      specify number format
    
    STYLE
        a                       number all lines
        t                       number nonempty lines
        n                       number no lines
        pBRE                    number lines, matching basic regexp BRE
    
    FORMAT
        ln                      left-justified, no leading zeros
        rn                      right-justified, no leading zeros
        lz                      left-justified, leading zeros

od
--

Dump files in octal and other formats. 

Each line consists of offset followed by groups of data.

[code]
    od [OPTION]... [FILE]...
    od [OPTION]... [FILE] [OFFSET]
    
    -A, --address-radix=FMT     address format
    -t, --format=FMT            data format
    -N, --read-bytes=BYTES
    -j, --skip-bytes=BYTES
    -w, --width=N               bytes per output line
    -v, --output-duplicates     don't replace adjacent identical lines with asterisk
    
    ADDRESS FORMAT
        o                   octal
        d                   decimal
        x                   hex
        n                   don't print offsets
    
    DATA FORMAT
        o                   octal 
        d                   signed decimal
        u                   unsigned decimal
        x                   hex
        f                   float
        a                   ASCII name, eg. nul, eot, stx... (higher bit ignored)
        c                   ASCII escape, eg. \0, \n, \360
        
            after that - number of bytes in a group:
        NUM                 number of bytes (for integers)
        C                   char
        S                   short
        I                   int
        L                   long
        F                   float
        D                   double
        L                   long double
        
            after that:
        z                   include ASCII column
        
    OFFSET
        +BYTES                  octal offset
        +BYTES.                 dec offset
        +0xBYTES                hex offset
        +<OFFSET>b              offset in blocks (512 bytes)

base64
------

Base64 encode or decode file into stdout.

[code]
    base64 [OPTION]... [FILE]
    
    <default>                   data to base64
    -d, --decode                base64 to data
    -w, --wrap=COLS             wrap encoded base64 (default: 76), use 0 to disable
    -i, --ignore-garbage
    
cksum
-----

Print byte count and CRC32 for each file.
     
[code]
    cksum [FILE]...
     
Cryptographic checksums
-----------------------

Print checksums and file names side-by side.

[code]
    sha1sum [OPTION]... [FILE]...
    
    -c, --check                 read checksums from FILES and check them
                                FILES are previously saved sha1sum output.
    -b, --binary                read in binary/text mode
    -t, --text 
    --status                    don't print anything, status indicates success
    
    OTHER SUMS
        md5sum
        sha224sum 
        sha256sum 
        sha384sum 
        sha512sum 
        
