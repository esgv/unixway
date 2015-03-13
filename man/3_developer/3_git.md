===
Git
===

Difference from other VCS's
===========================

Git treats revisions as FS snapshots rather than snapshots of distinct files.

Other VCS:

[image] images/git/other_rev.png

Git:
  
[image] images/git/git_rev.png

Git has local database (repository), checkout'd files, and staging area (index):

[image] images/git/stages.png

First, file is *modified*, then it is added to index, *staged*, then a commit copies 
files as they are in the index, to the local repository.

Configuration
=============

Checking settings:

[sh]
    $ git config --list
    user.name=Scott Chacon
    user.email=schacon@gmail.com
    color.status=auto
    color.branch=auto
    color.interactive=auto
    color.diff=auto
    ...
    
    $ git config user.name
    Scott Chacon
    
Name and email:

[sh]
    $ git config --global user.name "John Doe"
    $ git config --global user.email johndoe@example.com
    
Editor and diff tool:

[sh]
    $ git config --global core.editor emacs
    $ git config --global merge.tool vimdiff
    
Command aliases:

[sh]
    $ git config --global alias.co checkout
    $ git config --global alias.br branch
    $ git config --global alias.ci commit
    $ git config --global alias.st status
    
    $ git config --global alias.unstage 'reset HEAD --'     # when this is done...
    $ git unstage fileA                                     # ... the following two are equivalent
    $ git reset HEAD fileA
    
Repo setup
==========

General setup:

[sh]
    $ git config --global user.name "John Doe"
    $ git config --global user.email johndoe@example.com

    $ mkdir repo
    $ cd repo
    
Creating new repo:

[sh]
    $ git init
    $ git add *.c
    $ git commit -m 'initial project version'
    
Cloning existing repo:

[sh]
    # create a directory named 'grit' and clone there
    $ git clone git://github.com/schacon/grit.git
    
    # create a directory named 'mygrit' and clone there
    $ git clone git://github.com/schacon/grit.git mygrit
    
File workflow
=============

[image] images/git/lifecycle.png

(Index) Status
--------------

[sh]
    $ git status
    
    
Add (to index)
--------------

[sh]
    $ git add README

Remove
------

To remove a file from Git, you have to remove it from your tracked files 
(more accurately, remove it from your staging area) and then commit.
The `git rm` command does that and also removes the file from your working 
directory so you don’t see it as an untracked file next time around.

Removing both from index and working directory:
    
[sh]
    $ git rm grit.gemspec
    
Removing only from working directory:

[sh]
    $ rm grit.gemspec
    
Removing only from index:
    
[sh]
    $ git rm --cached readme.txt
    
`git rm` also accepts globs:

[sh]
    $ git rm log/\*.log
    $ git rm \*~
    
Note the backslash (`\\`) in front of the `*`. This is necessary because Git 
does its own filename expansion in addition to your shell’s filename expansion.
        
Move
----
    
Unlike many other VCS systems, Git doesn’t explicitly track file movement.

Move in the index:

[sh]
    $ git mv README.txt README
    
Equivalent action:

[sh]
    $ mv README.txt README
    $ git rm README.txt
    $ git add README
    
Index workflow
==============
    
Staging changes
---------------

[sh]
    $ touch  benchmarks.rb
    $ git add benchmarks.rb
    
Ignoring files
--------------

`.gitignore` file contains patterns to ignore.

- Blank lines or lines starting with # are ignored.
- Standard glob patterns work.
    
  - An asterisk (`*`) matches zero or more characters;
  - `[abc]` matches any character inside the brackets (in this case a, b, or c); 
  - a question mark (`?`) matches a single character; 
  - brackets enclosing characters separated by a hyphen(`[0-9]`) matches any character between them (in this case 0 through 9) .
  
- You can end patterns with a forward slash (/) to specify a directory.
- You can negate a pattern by starting it with an exclamation point (!).

Exapmle:

[sh]
    # a comment - this is ignored
    *.a       # no .a files
    !lib.a    # but do track lib.a, even though you're ignoring .a files above
    /TODO     # only ignore the root TODO file, not subdir/TODO
    build/    # ignore all files in the build/ directory
    doc/*.txt # ignore doc/notes.txt, but not doc/server/arch.txt    
    
Viewing changes
---------------

[sh]
    $ git status

Changed but not staged:

[sh]
    $ git diff
    
Staged but not committed:

[sh]
    $ git diff --cached
    $ git diff --staged     # since git 1.6.1
    
Undoing changes
---------------

Repo to index:

[sh]
    $ git reset HEAD benchmarks.rb
    
Copy file from repo to filesystem (therefore, removing it from index):

[sh]
    $ git checkout benchmarks.rb
    
Committing
----------

Launches your editor of choice:

[sh]
    $ git commit
    
Message explicitly specified:

[sh]
    $ git commit -m "Story 182: Fix benchmarks for speed"
    
Commit, skipping staging area:

[sh]
    $ git commit -a -m 'added new benchmarks'

There's one more try if you did last commit wrong:

[sh]
    $ git commit --amend
    
[sh]

    $ git commit -m 'initial commit'
    $ git add forgotten_file
    $ git commit --amend
     
History
=======

To show any object (commit, tag, branch, etc.):

[sh]
    $ git show <name>
    $ git show <hash>

Basic commands
--------------

Show commit history from current branch to past:

[sh]
    $ git log
    
[code]

    commit ca82a6dff817ec66f44342007202690a93763949
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Mon Mar 17 21:52:11 2008 -0700

        changed the version number

    commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 16:40:33 2008 -0700

        removed unnecessary test code

    commit a11bef06a3f659402fe7563abf99ad00de2209e6
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 10:31:28 2008 -0700

        first commit
       
Show diff with every commit and limit output with 2 entries:

[sh]
    $ git log -p -2
    
[code]

    commit ca82a6dff817ec66f44342007202690a93763949
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Mon Mar 17 21:52:11 2008 -0700

        changed the version number

    diff --git a/Rakefile b/Rakefile
    index a874b73..8f94139 100644
    --- a/Rakefile
    +++ b/Rakefile
    @@ -5,7 +5,7 @@ require 'rake/gempackagetask'
     spec = Gem::Specification.new do |s|
    -    s.version   =   "0.1.0"
    +    s.version   =   "0.1.1"
         s.author    =   "Scott Chacon"

    commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 16:40:33 2008 -0700

        removed unnecessary test code

    diff --git a/lib/simplegit.rb b/lib/simplegit.rb
    index a0a60ae..47c6340 100644
    --- a/lib/simplegit.rb
    +++ b/lib/simplegit.rb
    @@ -18,8 +18,3 @@ class SimpleGit
         end

     end
    -
    -if $0 == __FILE__
    -  git = SimpleGit.new
    -  puts git.show
    -end
    \ No newline at end of file
    
Some abbreviated stats:

[sh]
    
    $ git log --stat
    
[code]

    commit ca82a6dff817ec66f44342007202690a93763949
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Mon Mar 17 21:52:11 2008 -0700

        changed the version number

     Rakefile |    2 +-
     1 files changed, 1 insertions(+), 1 deletions(-)

    commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 16:40:33 2008 -0700

        removed unnecessary test code

     lib/simplegit.rb |    5 -----
     1 files changed, 0 insertions(+), 5 deletions(-)

    commit a11bef06a3f659402fe7563abf99ad00de2209e6
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 10:31:28 2008 -0700

        first commit

     README           |    6 ++++++
     Rakefile         |   23 +++++++++++++++++++++++
     lib/simplegit.rb |   25 +++++++++++++++++++++++++
     3 files changed, 54 insertions(+), 0 deletions(-)
        
One-liners:

[sh]
    
    $ git log --pretty=oneline
    
[code]
    
    ca82a6dff817ec66f44342007202690a93763949 changed the version number
    085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7 removed unnecessary test code
    a11bef06a3f659402fe7563abf99ad00de2209e6 first commit
    
Formatted output
----------------

Invocation:

[sh]
    $ git log --pretty=format:"%h - %an, %ar : %s"
    
[code]
    ca82a6d - Scott Chacon, 11 months ago : changed the version number
    085bb3b - Scott Chacon, 11 months ago : removed unnecessary test code
    a11bef0 - Scott Chacon, 11 months ago : first commit

Format options:

[code]
    Option  Description of Output
    %H      Commit hash
    %h      Abbreviated commit hash
    %T      Tree hash
    %t      Abbreviated tree hash
    %P      Parent hashes
    %p      Abbreviated parent hashes
    %an     Author name
    %ae     Author e-mail
    %ad     Author date (format respects the –date= option)
    %ar     Author date, relative
    %cn     Committer name
    %ce     Committer email
    %cd     Committer date
    %cr     Committer date, relative
    %s      Subject
    
Some options:

[code]
    Option                  Description
    -p                      Show the patch introduced with each commit.
    --stat                  Show statistics for files modified in each commit.
    --shortstat             Display only the changed/insertions/deletions line from the --stat command.
    --name-only             Show the list of files modified after the commit information.
    --name-status           Show the list of files affected with added/modified/deleted information as well.
    --abbrev-commit         Show only the first few characters of the SHA-1 checksum instead of all 40.
    --relative-date         Display the date in a relative format (for example, “2 weeks ago”) instead of using the full date format.
    --graph                 Display an ASCII graph of the branch and merge history beside the log output.
    --pretty                Show commits in an alternate format. Options include oneline, short, full, fuller, and format (where you specify your own format).
        
Branching and merging
=====================

Tags
----

Tags just point to specific commit.

Listing tags
~~~~~~~~~~~~

List tags:

[sh]
    $ git tag
    
Filter and list:

[sh]
    $ git tag -l 'v1.4.2.*'
    
Creating and deleting tags
~~~~~~~~~~~~~~~~~~~~~~~~~~
    
Tag command tags last (not pending) commit.
  
Git uses two main types of tags: lightweight and annotated. 
A lightweight tag is very much like a branch that doesn’t change -- it’s just a pointer 
to a specific commit. 
Annotated tags, however, are stored as full objects in the Git database. 
They’re checksummed; contain the tagger name, e-mail, and date; have a tagging message; 
and can be signed and verified with GNU Privacy Guard (GPG). 

Annotated tag:
    
[sh]
    $ git tag -a v1.4 -m 'my version 1.4'
    
Lightweight tag:

[sh]
    $ git tag v1.4-lw
   
Tag on specific commit:

[sh]
    $ git tag -a v1.2 9fceb02
    
Delete tag:

[sh]
    $git tag -d v1.2
    
Signed tags
~~~~~~~~~~~
    
GPG-signed tag (passphrase needed):
    
[sh]
    $ git tag -s v1.5 -m 'my signed 1.5 tag'
    
Verifying signature (you need author's public key in the keyring):

[sh]
    $ git tag -v v1.4.2.1

If you don't have author's pubkic key in the keyring, Git will show error message.



Branches
--------

Basic branching
~~~~~~~~~~~~~~~

[sh]

    $ git add README test.rb LICENSE
    $ git commit -m 'initial commit of my project'
    
Commit is represented like this:

[image] images/git/br1.png

Multiple commits:

[image] images/git/br2.png

Branch pointing to the commit data's history:

[image] images/git/br3.png

Create a new branch:

[sh]
    $ git branch testing
    
Could also be done like this:

[sh]
    $ git checkout -b 'testing'
    
[image] images/git/br4.png


HEAD is a pointer to current branch:

[image] images/git/br5.png    

Let's checkout testing branch:

[sh]
    $ git checkout testing
    
[image] images/git/br6.png

Then advance it:

[sh]
    $ vim test.rb
    $ git commit -a -m 'made a change'

[image] images/git/br7.png

Checkout master:

[sh]
    $ git checkout master
    
[image] images/git/br8.png

Advance master:

[sh]
    $ vim test.rb
    $ git commit -a -m 'made other changes'
    
[image] images/git/br9.png

It's easier to think of branches as of silos:

[image] images/git/br10.png

[image] images/git/br11.png

Branch management
~~~~~~~~~~~~~~~~~

List branches:

[sh]
    $ git branch -v
            
Branches currently merged into HEAD:

[sh]
    $ git branch --merged
    
Not merged with HEAD:

[sh]
    $ git branch --no-merged
        
Delete branch:

[sh]
    $ git branch -d testing
        
Deletion is successfull, if branch to be deleted is an ancestor of current branch.

Force delete branch:

[sh]
    $ git branch -D testing

Detached head
~~~~~~~~~~~~~

If you checkout tag, remote branch, or any arbitrary commit, that is, not a 
branch head, `HEAD` will point to that commit, and it will be considered 
*detached*. 

You are able to commit while on detached head, but that commit will be untracked.

Also, when you check out, it only affects the `HEAD` variable.

Merging
-------

Fast forward
~~~~~~~~~~~~

If one branch is a parent of another,  Git can just move pointer forward to merge 
those two branches:

[image] images/git/mr1.png

[code]
    $ git checkout master
    $ git merge hotfix
    
[image] images/git/mr2.png

Normal merge
~~~~~~~~~~~~

[image] images/git/mr3.png

[sh]
    $ git checkout master
    $ git merge iss53
    $ git commit
 
[image] images/git/mr4.png
 
Merge conflicts
~~~~~~~~~~~~~~~

An error message is shown if merge is unsuccessful.
    
File contents:

[code]
    <<<<<<< HEAD:index.html
    <div id="footer">contact : email.support@github.com</div>
    =======
    <div id="footer">
      please contact us at support@github.com
    </div>
    >>>>>>> iss53:index.html    
    
Manual resolution:

[sh]
    $ git add index.html
    
Graphical resolution tool:

[sh]
    $ git mergetool
    
If merge tool returns 'no error', conflict is resolved 
    
Commit:

[sh]
    $ git commit
        
Remote branches and repos
=========================

Remote branches are references to the state of branches on your remote repositories. They're local branches
that you can't move; they're moved automatically whenever you do any network communication.

They take the form `(remote)/(branch)`. 

Setup
-----

Add remote repo:

[sh]
    $ git remote add pb git://github.com/paulboone/ticgit.git
    
When you clone repository, `origin` remote repo is automatically added.

List remote hosts:

[sh]
    $ git remote [-v]

Removing and renaming:

[sh]
    $ git remote rename pb paul
    $ git remote rm paul
    
List remote branches:

[sh]
    $ git branch -r
    
Fetch
-----

[image] images/git/rb1.png

[image] images/git/rb2.png

[image] images/git/rb3.png

[image] images/git/rb4.png

Push
----

Push is a serverside pull, except it won't merge non-FF cases.

Transfer local `serverfix` merge it with server `serverfix`:

[sh]
    $ git push origin serverfix
    
Explicit version:

[sh]
    $ git push <remote> <local branch>:<remote branch>
    
Deleting remote branch, 'take nothing on my side and make it a remote branch':

[sh]
    $ git push <remote> :<remote branch>
    
By default, only current head is pushed. To push all `refs/heads`:
    
[sh]
    $ git push --all <remote>
    
To push tags:

[sh]
    
    $ git push --tags <remote>
    
Tracking branches
-----------------

Checking out a local branch from a remote branch automatically creates what is 
called a tracking branch. 
Tracking branches are local branches that have a direct relationship to a remote branch. 
If you’re on a tracking branch and type git push, 
Git automatically knows which server and branch to push to. 
Also, running git pull while on one of these branches fetches all the remote references 
and then automatically merges in the corresponding remote branch.

Syntax one:

[sh]
    $ git checkout -b sf origin/serverfix
    
Syntax two:

[sh]
    $ git checkout --track origin/serverfix
    
Rebasing
========

In Git, there are two main ways to integrate changes from one branch into another: 
the merge and the rebase. 
    
Basic rebase
------------

If you go back to an earlier example from the Merge section, 
you can see that you diverged your work and made commits on two different branches.

[image] images/git/re1.png

The easiest way to integrate the branches, as we’ve already covered, is the merge command. 
It performs a three-way merge between the two latest branch snapshots (C3 and C4) 
and the most recent common ancestor of the two (C2), creating a new snapshot (and commit).

[image] images/git/re2.png

However, there is another way: you can take the patch of the change that was 
introduced in C3 and reapply it on top of C4. In Git, this is called *rebasing*. 
With the `rebase` command, you can take all the changes that were committed 
on one branch and replay them on another one.

Syntax:

[sh]
    $ git checkout experiment
    $ git rebase master
    
[image] images/git/re3.png
    
Than, you can do FF:

[image] images/git/re4.png
 
Complex rebase
--------------

Situation:

[image] images/git/re5.png

Syntax:

[sh]
    $ git rebase --onto master server client
    
This basically says, "Check out the `client` branch, figure out the patches 
from the common ancestor of the `client` and `server` branches, and then 
replay them onto master."

Result:

[image] images/git/re6.png


Rebase perils
-------------

**Do not rebase commits that you have pushed to a public repository.**

Situation:

[image] images/git/re7.png

Now, someone else does more work that includes a merge, and pushes that work to 
the central server. You fetch them and merge the new remote branch into your work, 
making your history look something like this:

[image] images/git/re8.png

Next, the person who pushed the merged work decides to go back and rebase their
work instead; they do a git push --force to overwrite the history on the server. 
You then fetch from that server, bringing down the new commits.

[image] images/git/re9.png

At this point, you have to merge this work in again, even though you’ve already 
done so. Rebasing changes the SHA-1 hashes of these commits so to Git they look 
like new commits, when in fact you already have the C4 work in your history.
    
[image] images/git/re10.png