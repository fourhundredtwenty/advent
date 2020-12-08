# Git Basics

## Clone someone else's code

i made a git repo to hold all my advent stuff so we can use it for doing a git thing
try running `git clone https://github.com/fourhundredtwenty/advent.git`

### Where'd it go?

High Temp Hydrogen Attack:turtle:  14:01
it did stuff
It counted and received nine objects

sekiro enthusiast  14:01
you should have a folder now called "advent" with all my shit in it
14:01
wherever that shell was
14:01
if it was on your desktop, then hooray, there

High Temp Hydrogen Attack:turtle:  14:03
i have a folder called "advent" on my desktop but only because I made it

sekiro enthusiast  14:03
i guess in that git shell you can do pwd and see where it put your stuff (edited)

High Temp Hydrogen Attack:turtle:  14:04
/c/users/adam
14:05
well what do you know
14:05
a folder named advent
:joy:
1

### Look around

If you cd into my folder in your shell and run git status or git log you should get some more interesting output now. It'll just say that i made one commit and there's no new changes and some other stuff

also the git docs are some of the worst out there to the point that there is a whole industry out there around better git docs

High Temp Hydrogen Attack:turtle:  14:08
in my git or my powershell?

sekiro enthusiast  14:08
well you ought to be able to run git in powershell
but if you can't
then your special git shell

High Temp Hydrogen Attack:turtle:  14:08
wait so should I close the git shell?

sekiro enthusiast  14:08
omg there's
14:09
https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-PowerShell

High Temp Hydrogen Attack:turtle:  14:09
does that matter anymore

sekiro enthusiast  14:09
is it really that hard??

High Temp Hydrogen Attack:turtle:  14:09
wow computers are the worst

sekiro enthusiast  14:09
agreed
14:09
i guess keep your git shell open, friend

High Temp Hydrogen Attack:turtle:  14:09
kk

sekiro enthusiast  14:09
you might not need powershell though? lol what happens if you run python in your git shell?
14:10
maybe you can cut down on windows that way

High Temp Hydrogen Attack:turtle:  14:10
a bunch of shit, permission denied

sekiro enthusiast  14:10
llloooooollll windows

High Temp Hydrogen Attack:turtle:  14:10
I think I broke it

sekiro enthusiast  14:11
check out this enormous flex http://d34db33f.s3.amazonaws.com/2020-12-04T14%3A10%3A56%2C521136587-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607713862&Signature=BsFnb8qUfbC7KsRBkIiGvp%2Fr3Gc%3D

(273 kB)
http://d34db33f.s3.amazonaws.com/2020-12-04T14%3A10%3A56%2C521136587-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607713862&Signature=BsFnb8qUfbC7KsRBkIiGvp%2Fr3Gc%3D

High Temp Hydrogen Attack:turtle:  14:11
I don't have the $ anymore
:cool:
1


sekiro enthusiast  14:11
kill the window open a new one? :eyes-looking:

High Temp Hydrogen Attack:turtle:  14:11
okay how about fuck you

sekiro enthusiast  14:11
https://coupleslack.slack.com/archives/C01GGJ4A4BT/p1607108966071100
leeeaaan innnn

High Temp Hydrogen Attack
wow computers are the worst
Posted in #advent | Dec 4th | View message

High Temp Hydrogen Attack:turtle:  14:11
and your fish
:aboutme:
1

14:12
do I open git bash or git cmd

sekiro enthusiast  14:12
i'd go for git bash, it'll be more like a linux shell

High Temp Hydrogen Attack:turtle:  14:12
or git gui, but I'm assuming not git gui

sekiro enthusiast  14:12
git cmd will be more like the windows cmd prompt which is worse
14:12
you're free to explore the gui, please! i just don't know how to use it

High Temp Hydrogen Attack:turtle:  14:12
okay

sekiro enthusiast  14:12
plenty of great developers use git GUIs every day

High Temp Hydrogen Attack:turtle:  14:13
I still don't understand what I'm doing with git or why
14:13
just....you know....so you know

sekiro enthusiast  14:13
yeah and thank you for coming along anyway
14:14
it's the way of sharing code for most programmers today. all this copying and pasting back and forth we do is totally cool at our scale but this is a baseline tool like an editor or the programming language itself
14:15
it gives you
a) an easy way to shuffle code back and forth between people
and
b) a way to track your changes and easily go back
14:15
right now i'm just worrying about (a) because why try to do two things at once

High Temp Hydrogen Attack:turtle:  14:15
okay cool
14:15
that helps

sekiro enthusiast  14:15
i'd love for you to make a github account and create your own git repository with your code in it so that i can clone yours
14:15
but i didn't wanna rush in
14:16
in a sec i'll write my 4.py and then you can get a demo of how easy it is to get updates to my code

High Temp Hydrogen Attack:turtle:  14:16
I mean that sounds easy enough
:nod:
1

14:16
I'll make an account while you work

sekiro enthusiast  14:17
this is so much better than job
:heart:
1


High Temp Hydrogen Attack:turtle:  14:17
agreed
14:20
I have an account

sekiro enthusiast  14:20
you'll wanna create a new repository in the web UI and at the end of that it will give you instructions for doing stuff in your shell
14:21
it'll be like "if you already have existing code do this and it'll show up here on our website"
14:21
git remote add origin farrrtttt

High Temp Hydrogen Attack:turtle:  14:22
okay. Would a repository generally be project based, or does lots of stuff go in it
14:22
if I name it advent, is that fine?
:thumbsupdonut:
1

14:23
and I assume public access is fine because who cares
14:26
is my repository a file system? Can I put folders into it, or just files?

sekiro enthusiast  14:27
yeah it's files and folders whatever you want
14:27
and there's a lot of debate about how a reo should be used!

High Temp Hydrogen Attack:turtle:  14:27
cool because I've been organizing by day

sekiro enthusiast  14:27
google uses a huge monorepo
14:28
ALL of the code from everyone in the company, billions of lines is in one repo :open_mouth:
14:28
i like smaller project-based repos myself

High Temp Hydrogen Attack:turtle:  14:28
wowowowow that sounds literally the worst

sekiro enthusiast  14:28
it's pretty nutso. There's some arguments for it and i get it
14:28
but basically don't worry about it like you can't get it wrong
14:28
it's only wrong once you realize you have a problem

High Temp Hydrogen Attack:turtle:  14:30
cool
14:30
all my stuff is in my repo

sekiro enthusiast  14:32
sick, send me a link sometime!

High Temp Hydrogen Attack:turtle:  14:33
https://github.com/Trainpants/Advent2020

GitHubGitHub
Trainpants/Advent2020
Contribute to Trainpants/Advent2020 development by creating an account on GitHub.
14:33
like that?
14:35
can you do a range of the alphabet?
14:36
eh, neverminds

sekiro enthusiast  14:36
huh idk that's a good question

High Temp Hydrogen Attack:turtle:  14:37
can just do in "abcdef"

sekiro enthusiast  14:38
i thought i was being clever
14:38
but my code is getting more and more, uh, troubling
14:38
you'll see
14:38
:toria-grimace:

High Temp Hydrogen Attack:turtle:  14:39
well mine's in the above link if you need it Kappa
:black_heart:
1

14:41
my part 2 is getting :toria-grimace:

sekiro enthusiast  14:49
That's not the right answer; your answer is too low oops
14:49
whut
14:49
what i do

High Temp Hydrogen Attack:turtle:  14:49
answer + 1
:joy:
1

14:49
:nokappa:

sekiro enthusiast  14:49
Surely, nobody would mind if you made the system temporarily ignore missing cid
14:49
ooooo
14:49
i missed that

High Temp Hydrogen Attack:turtle:  14:50
loool yeah that's an important bit
14:50
read the card > understand the card
:thinking-nothanks:
2


sekiro enthusiast  14:50
i got a different number
14:50
and it's still wrong
14:50
rude!!!

High Temp Hydrogen Attack:turtle:  14:50
answer + 1

sekiro enthusiast  14:51
i pushed my (not working) code up to github
14:51
if you go into my repo and run git pull you should get my changes
14:52
uuuugh now i have to actually look at my results
14:53
the last 3 days i got the right answer first try and i was like "computers r fun yey"
14:53
heya print()

High Temp Hydrogen Attack:turtle:  14:53
umm how do i do that

sekiro enthusiast  14:53
let's go bro
14:53
in git-bash cd into my advent folder on your desktop
14:53
and run git pull

High Temp Hydrogen Attack:turtle:  14:54
fatal not a git repo

sekiro enthusiast  14:54
:pikachu-stunned:
14:55
okay well there are like, debugging ways to fix this -- my guess is something windows-related having to do with hidden files not being copied when you moved the folder
14:55
but the solution i'd do at work is 100% just to delete the folder and clone it again
14:55
it's not precious - that's the whole point of git

High Temp Hydrogen Attack:turtle:  14:55
:nod:

sekiro enthusiast  14:56
but since we have folders with the same name
14:56
you'll have to run git clone MY_REPO_URL advent-alex so that it creates a new folder named advent-alex
14:56
that holds all my code
14:57
you can find a repo's clone URL on github here
http://d34db33f.s3.amazonaws.com/2020-12-04T14%3A57%3A06%2C401619646-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607716629&Signature=ZjIrb5Gl0u7m8g9bICzIbsE4JUs%3D

(80 kB)
http://d34db33f.s3.amazonaws.com/2020-12-04T14%3A57%3A06%2C401619646-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607716629&Signature=ZjIrb5Gl0u7m8g9bICzIbsE4JUs%3D
14:57
they haven't changed the location of this button in as long as the website has existed

High Temp Hydrogen Attack:turtle:  14:58
can you give me the url to that page?

sekiro enthusiast  14:58
oh lol oops
14:59
yes
14:59
https://github.com/fourhundredtwenty/advent

GitHubGitHub
fourhundredtwenty/advent
Contribute to fourhundredtwenty/advent development by creating an account on GitHub.
14:59
http://d34db33f.s3.amazonaws.com/2020-12-04T14%3A59%3A30%2C567841329-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607716773&Signature=eri0L41qAEuT9EJeIEHWOihfc5Y%3D
:double-thinking-face:

(14 kB)
http://d34db33f.s3.amazonaws.com/2020-12-04T14%3A59%3A30%2C567841329-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607716773&Signature=eri0L41qAEuT9EJeIEHWOihfc5Y%3D

High Temp Hydrogen Attack:turtle:  15:00
lol 41 minute old account clearly a bot

sekiro enthusiast  15:00
ban ban ban
15:00
more like trainbants

High Temp Hydrogen Attack:turtle:  15:00
like when you said "cunt" in my twitch stream

sekiro enthusiast  15:00
hahahahahah

High Temp Hydrogen Attack:turtle:  15:00
I still laugh about that

sekiro enthusiast  15:00
i love that
15:00
i forgot about it already
15:00
ty
15:00
will i use your code to double-check mine?
15:00
absolutely i will

High Temp Hydrogen Attack:turtle:  15:01
I don't think we get the same input dat
15:01
a

sekiro enthusiast  15:02
no but i'm just gonna change youre code to point at my data file
15:02
242

High Temp Hydrogen Attack:turtle:  15:02
oh, duh

sekiro enthusiast  15:02
WHAMPST
:question:
1

15:02
i'm off by half
15:02
lmaaaoo what have i done wrong
15:04
ohhh i figured it out
15:04
even though i removed the cid i didn't change my comparison in validate
15:04
i'm still saying "HEY these HAVE to equal"
15:04
so any of them that do have cid are now wrong

High Temp Hydrogen Attack:turtle:  15:04
that'll do it
15:04
I'm reading your code now

sekiro enthusiast  15:05
i added comments because of the mess

High Temp Hydrogen Attack:turtle:  15:05
it's incomprehensible

sekiro enthusiast  15:05
thankx

High Temp Hydrogen Attack:turtle:  15:05
but only because I don't know how anything works

sekiro enthusiast  15:05
i'm really going all out on this shit

High Temp Hydrogen Attack:turtle:  15:05
so now that I have this repo

sekiro enthusiast  15:05
i don't wanna just dump my brain on you but if you wanna know why anything looks the way it does in there i think i can explain everything in there
15:05
yeah

High Temp Hydrogen Attack:turtle:  15:06
do I open my code from there?

THREAD_START

71 replies
Last reply 4 days agoView thread

High Temp Hydrogen Attack:turtle: Dec 4th at 15:06
do I open my code from there?
71 replies

sekiro enthusiast  4 days ago
yeah, the copy of your code on your laptop is still your active development space

High Temp Hydrogen Attack:turtle:  4 days ago
aka, saved locally

sekiro enthusiast  4 days ago
but any time you want to save your changes more permanently you can use git to go into that folder and say
git commit -am "message describing what you did"

sekiro enthusiast  4 days ago
which will create a new checkpoint, aka commit

sekiro enthusiast  4 days ago
and then you can do git push origin master to push your changes up to github.com

sekiro enthusiast  4 days ago
you can do as much shit as you want locally however you want to but no one else will see it until you commit and push

High Temp Hydrogen Attack:turtle:  4 days ago
okay

sekiro enthusiast  4 days ago
just like repo size everyone has their own opinion on how often you should commit and what you should say in your commit messages

High Temp Hydrogen Attack:turtle:  4 days ago
so a commit is a checkpoint, push is an upload
:thumbsupparrot:
1


sekiro enthusiast  4 days ago
but it's really up to you what you do, not them

sekiro enthusiast  4 days ago
absolutely right yeah

High Temp Hydrogen Attack:turtle:  4 days ago
what if I fuck up my code royally on my aCtIvE DeVeLoPmEnT sPaCe

High Temp Hydrogen Attack:turtle:  4 days ago
and want to grab my checkpoint

High Temp Hydrogen Attack:turtle:  4 days ago
Start > Restart at checkpoint
:igetit:
1


sekiro enthusiast  4 days ago
you can reset your code to any existing commit using git reset COMMIT_ID

sekiro enthusiast  4 days ago
but instead of exlaining that entirely

sekiro enthusiast  4 days ago
check out my amazing coworker's site https://ohshitgit.com/

sekiro enthusiast  4 days ago
So here are some bad situations I've gotten myself into, and how I eventually got myself out of them in plain english.

High Temp Hydrogen Attack:turtle:  4 days ago
cooooooool

High Temp Hydrogen Attack:turtle:  4 days ago
I remember you sharing this ages ago when they made it

sekiro enthusiast  4 days ago
it's a really nice resource because the official git docs are like no

sekiro enthusiast  4 days ago
https://git-scm.com/docs/git-push

sekiro enthusiast  4 days ago
:what:

High Temp Hydrogen Attack:turtle:  4 days ago
so to commit

High Temp Hydrogen Attack:turtle:  4 days ago
nevermind I type in that shit you types above

High Temp Hydrogen Attack:turtle:  4 days ago
okokokokok

sekiro enthusiast  4 days ago
that git command has the flags -a -m on it

High Temp Hydrogen Attack:turtle:  4 days ago
what does that mean

sekiro enthusiast  4 days ago
-a tells git "commit ALL uncomitted files in this repo"

sekiro enthusiast  4 days ago
if you don't say -a you need to manually specify what files you wanna commit

sekiro enthusiast  4 days ago
it's worth doing that as your projects get bigger but i don't think it's worth worrying about for advent...yet?

High Temp Hydrogen Attack:turtle:  4 days ago
okay

sekiro enthusiast  4 days ago
and -m just means "add a commit message which i will write after this"

sekiro enthusiast  4 days ago
git commits cannot have an empty message

High Temp Hydrogen Attack:turtle:  4 days ago
cool

sekiro enthusiast  4 days ago
so you need to add -m or it'll get angry

High Temp Hydrogen Attack:turtle:  4 days ago
okay and so I have folders for each day

High Temp Hydrogen Attack:turtle:  4 days ago
do I commit the folder of folders, or the individual day folder?

High Temp Hydrogen Attack:turtle:  4 days ago
will the latter add it to the appropriate folder on github?

sekiro enthusiast  4 days ago
:nod: whatever you create inside of your advent folder and then add to git will show up on github

sekiro enthusiast  4 days ago
but it can never go up outside of your repo and reach higher level folders

sekiro enthusiast  4 days ago
the repo folder is the highest extent git can care or know about, it can only track things deeper inside

sekiro enthusiast  4 days ago
lemme check something - git commit -am might not automatically add new folders

sekiro enthusiast  4 days ago
you may need a second step tomorrow -- also vscode may have an interface for all of this

High Temp Hydrogen Attack:turtle:  4 days ago
it's fine I'll just commit every file over and over again

sekiro enthusiast  4 days ago
i bet it's one of the most common plugins or it's built in

sekiro enthusiast  4 days ago
ach yeah check out this error if you try to use git commit -am to add a new file
~/d/advent ❯❯❯ mkdir test_folder
~/d/advent ❯❯❯ touch test_folder/test_file
~/d/advent ❯❯❯ git status
On branch main
Your branch is up to date with 'origin/main'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test_folder/
nothing added to commit but untracked files present (use "git add" to track)
~/d/advent ❯❯❯ git commit -am "make a new folder for testing"
On branch main
Your branch is up to date with 'origin/main'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test_folder/
nothing added to commit but untracked files present (use "git add" to track)

sekiro enthusiast  4 days ago
specifically the error message nothing added to commit but untracked files present (use "git add" to track) is clear

High Temp Hydrogen Attack:turtle:  4 days ago
"theres stuff here but we don't know what to do with it so we're doing nothing"
:this:
1


sekiro enthusiast  4 days ago
you just have to tell git about it the very first time it sees a new file

sekiro enthusiast  4 days ago
git add is how you answer "yes" to the question "do you want me to track this?"

High Temp Hydrogen Attack:turtle:  4 days ago
okay

sekiro enthusiast  4 days ago
~/d/advent ❯❯❯ git add test_folder/
~/d/advent ❯❯❯ git status
On branch main
Your branch is up to date with 'origin/main'.
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   test_folder/test_file
~/d/advent ❯❯❯ git commit -am "make a new folder for testing"
[main 32a5c94] make a new folder for testing
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test_folder/test_file

High Temp Hydrogen Attack:turtle:  4 days ago
this is all very confusing

High Temp Hydrogen Attack:turtle:  4 days ago
in case you were wondering

High Temp Hydrogen Attack:turtle:  4 days ago
do the files not show up on the site until I push?
:nod:
1


High Temp Hydrogen Attack:turtle:  4 days ago
like you can pull my stuff now, it'll only get what's been pushed
:nod_fast:
1


sekiro enthusiast  4 days ago
git's user interface is trash. the fact that you've pushed and pulled code is a big achievement for a day

High Temp Hydrogen Attack:turtle:  4 days ago
so where's the stuff that's been committed

sekiro enthusiast  4 days ago
just on your computer

High Temp Hydrogen Attack:turtle:  4 days ago
okay

High Temp Hydrogen Attack:turtle:  4 days ago
is it a file somewhere?

sekiro enthusiast  4 days ago
git makes a special folder caller .git in your repo which stores all the differences

High Temp Hydrogen Attack:turtle:  4 days ago
k

sekiro enthusiast  4 days ago
every time you commit it stores the difference between now and last commit

sekiro enthusiast  4 days ago
and git stores those diffs in its little hidden folder

High Temp Hydrogen Attack:turtle:  4 days ago
k

sekiro enthusiast  4 days ago
so whenever you ask for a commit it just churns all the diffs together and changes the files in your repo to match

sekiro enthusiast  4 days ago
idk if that explains anything you were asking?

High Temp Hydrogen Attack:turtle:  4 days ago
yes

sekiro enthusiast  4 days ago
i use git without ever using github sometimes - when i wanna get checkpoints but i don't care about collaborating

THREAD_END


High Temp Hydrogen Attack:turtle:  15:06
I still have it all in my folder on the desktop
15:06
how does it update

