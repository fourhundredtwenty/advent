so far you've only been using one branch in git. that branch is called `main`.  You can see that in the shell by running `git branch`
```
~/d/advent ❯❯❯ git branch
* main
```

the asterisk means that's the branch you're currently on. You can also see your repos branches on github dotcom - https://github.com/Trainpants/Advent2020/branches or on the branch picker in the top left-ish of the repo's homepage http://d34db33f.s3.amazonaws.com/2020-12-06T13%3A07%3A17%2C078266106-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607882844&Signature=XmUQ162We0KOEkowQobSU3SsO1s%3D

You've also had to use the branch name when pushing, like `git push origin main` and probably you've seen it when you've run `git status`

```
~/d/advent ❯❯❯ git status
On branch main
Your branch is up to date with 'origin/main'.
```

So whether or not we care about branches we can tell from all the places that this word shows up that git *really* cares about branches. What the fuck is a branch.

A branch is an independent working copy of your code. You can create an unlimited number of branches (using `git branch`) and switch between the branches for free (using `git checkout`). When you are "on a branch", aka "checked out to a branch" all of your commits are appended to the history of *only that branch. But you can integrate branches back together using `git merge`

  21:59
okay all of that was very interesting and well written
21:59
It makes very good sense

High Temp Hydrogen Attack:turtle:  22:07
so I think my biggest issue is a linguistic one
22:08
"commit" is very much a verb to me
22:08
as is push
22:10
so in my mind, I think I was thinking that "committing" (which is to say, using the 'commit' command) was sort of staging the code to push, and "pushing" (ditto, but 'push' command) was making a push noun thing on github
22:11
which is essentially the same thing just misnamed, makes a node on the graph
22:14
so really I was asking the wrong questions
22:14
I'm confused about commits that haven't been pushed.
22:14
you said there's some hidden git file somewhere locally that has that
22:17
what happens if before I push that commit, I make a new commit
22:17
why is it a two step process, I guess is my biggest question?
22:18
why commit then push?
22:18
is it just a "are you sure you want to quit?" type of thing?
22:22
yeah this is my biggest confusion
22:23
but learning about the graph theory has def helped my thinking about all this in general

High Temp Hydrogen Attack:turtle:  00:17
woooooooooooooooooooooooooooooooooooooooow I just looked at day 7 (edited)
00:21
and I hate it
00:23
wow yeah I really hate this

sekiro enthusiast  10:16
I think every follow-up question you asked can be addressed by talking about the distinction between local and remote repositories. I’m out grabbing coffee so here’s my short no examples version and I’ll were more later.
If you ctrl-f through the doc I wrote yesterday you’ll notice that I didn’t say the word “push”. All this graph theory stuff is completely correct and true and usable without ever pushing or pulling or talking about GitHub.com
Push and pull are like git DLC. They’re an expansion pack on top of managing the graph.  You could call them “upload” and “download”. Their purpose is to synchronize the state between two copies of a repository.  So when you create a new commit on your laptop using the “git commit” command you’re only creating a new node in the graph on your laptop. Git commit does nothing to manage the differences between remote and local state.
10:21
Git doesn’t have a concept of hierarchy between repos. Repos don’t have parents or children. When you go to GitHub and “git clone” a repository you end up with a fully fledged 100% functionally identical copy of the code that’s on GitHub. Every copy of a repository is absolutely equal to every other copy. This is Good Actually for political, organizational and computational reasons. And ethical reasons if you ask me but toot toot here comes the anarchy train to gush about how bad unitary authority is.

sekiro enthusiast  10:30
There is a copy of your repository on your laptop. There is a copy on my laptop. There is a copy on GitHub. All of these are “equal” - technically you can push or pull to or from any of these. Me to you, GitHub to me, you to GitHub. These push and pull operations are synchronization operations between your local copy of your repo and any other copy of the same repo.
When you do a “git commit” two things happen
A) add a node to the graph
B) move your current branch pointer to the new node

When you do a git push you’re asking git to synchronize the new state of the graph on your laptop with the now-out-of-date state of the repo on GitHub. So two things happen
A) your new graph node (including its place in the graph) is uploaded to github
B) the branch pointers in the copy of the repo are updated

High Temp Hydrogen Attack:turtle:  10:30
okay that is insanely helpful
:heart:
1


sekiro enthusiast  10:31
There’s some really cool examples I can show you that illustrate how this is true but I’m on my phone atm

High Temp Hydrogen Attack:turtle:  10:31
the visualization of what I have been doing is suddenly a lot clearer

sekiro enthusiast  10:31
You’re maintaining a copy of a graph locally and periodically backing it up to a GitHub

High Temp Hydrogen Attack:turtle:  10:31
yes

sekiro enthusiast  10:32
:+1::skin-tone-2::+1::skin-tone-2::+1::skin-tone-2:
10:32
Any copy (aka clone) of a git repo can have 0 or more “remote” repositories

High Temp Hydrogen Attack:turtle:  10:33
it's a good thing we've been talking about graphs and trees because that is entirely what today's advent is
:oh-no:
2


sekiro enthusiast  10:38
A “remote repository” is the name another copy of the repo somewhere else that YOUR copy of the repo knows about. Usually it’s on a separate server. If you go into your repo and run “git remote -v” it should show you that you have one remote named “origin”, and it is the default remote for both push and pull operations (that’s why there’s two lines with the same gel).

Fun example: like I said ALL copies of a git repo are equal. So we know you can say “git clone https://some_git_url” in order to create a copy of your repo. But you can also make a clone of your local copy. That is, a clone of a clone.
I’m still not on my laptop but try running “git clone /path/to/your/advent_repo” and git should happily create another clone of your clone!
10:39
If you go into that clone and run “git remote -v” you should see a single remote repository, also named “origin” but the url will be different!
10:39
And if you make changes to your original clone and then “git pull” in your clone of a clone you should see see a normal successful synchronization of code.

High Temp Hydrogen Attack:turtle:  10:40
iiiiiiiinteresting

sekiro enthusiast  10:40
Okay that’s what I’ve got on remote repos right now but only because I have to poop and I’m gonna run home. I don’t k is if I even close to answered all your questions so hmu with follow ups if you’ve got em
10:40
This is all pretty intense git internals btw. This is like 200, 300-level shit.
10:41
Most people learn “git commit -am git push git pray I didn’t break shit”

High Temp Hydrogen Attack:turtle:  10:41
Honestly I feel a lot more confident now, can't think of any follow ups
:heart:
1

10:42
knowing that commit is a noun, and that we're constructing a graph, and that github is backup dlc all has helped immensely
10:43
you're a very good teacher

over seeing so many feet on the tl  10:43
you’re a very good learner tbh
:very-much-this:
1


High Temp Hydrogen Attack:turtle:  10:43
yay compliment party!

sekiro enthusiast  10:50
I wanna be sure I copy and paste all these things I’ve been writing for you Adam. I don’t wanna lose these to slack retention and at this point I’ve literally written hours of work that
A) I’m just generally proud of
B) may be useful to @over seeing so many feet on the tl sometime
:heart:
1


sekiro enthusiast  10:57
what stuff have we talked about, Adam?
- git graph theory
- git remotes
- list comprehensions
- basic git usage

sekiro enthusiast  10:57
is that all?


2 replies
Last reply 22 hours agoView thread

sekiro enthusiast  11:09
and i should go save any screenshots too since they'll expire
11:09
i love my expiring screenshots but it does leave a wake of damaged documents if i'm not careful (edited)
11:11
i haven't read today's advent and i have a meeting in 20 minutes i should prepare for
11:11
ugh this feeling sucks
11:12
i'd rather be doing so many things, or, even better, nothing
:nod_crying:
1


sekiro enthusiast  11:19
also ugh back to the real world where git is also just a fucking tool of bureaucracy and not a weird toy
:heart:
1


sekiro enthusiast  11:25
bags must be color-coded and must contain specific quantities of other color-coded bags
11:25
love this
11:25
it's so contrived today :chefs-kiss:

High Temp Hydrogen Attack:turtle:  11:25
yeah not like those other days

sekiro enthusiast  11:25
lolol

High Temp Hydrogen Attack:turtle:  11:25
which weren't contrived in the slightest

sekiro enthusiast  11:26
okay but we can compare these things
11:26
and i think this is sillier than "trees in a forest but you move like a chess horsey"
11:26
which was obviously silly

High Temp Hydrogen Attack:turtle:  11:26
hahaha :thats_fair:
11:28
I'm not quite sure how to start this problem
11:28
I feel like you could make an absolute mess of nested lists

sekiro enthusiast  11:28
here's my suggestion: use classes and inheritance
11:28
that's what i'm gonna do
11:28
but like in 6 hours

High Temp Hydrogen Attack:turtle:  11:28
okay gonna google what both those things mean
:heavy_plus_sign:
1


1 reply
22 hours agoView thread

sekiro enthusiast  11:28
:sob-blood:

High Temp Hydrogen Attack:turtle:  11:28
also yeah same

sekiro enthusiast  11:30
you can make a generic Bag type and then subclass that to different colors of bags, and use that as the place to store the --i have to go to a meeting jfc i hate today

sekiro enthusiast  11:54
here is some even more intense details on how git pull works https://longair.net/blog/2009/04/16/git-fetch-and-merge/

High Temp Hydrogen Attack:turtle:  12:06
I drew a model of the example in ms paint

High Temp Hydrogen Attack:turtle:  12:06
image.png
image.png


:learn:
1
:heavy_plus_sign:
1


1 reply
21 hours agoView thread

janetAPP  12:07
lol wut?

sekiro enthusiast  12:07
holy shit yes
12:07
ths is shitposting

High Temp Hydrogen Attack:turtle:  12:07
looks a lot like a directed acyclic graph to me
12:07
I learned stuff yesterday

sekiro enthusiast  12:08
i have a suggestion of what might be a fun way to stretch those muscles now that you Know Things, if you're interested

High Temp Hydrogen Attack:turtle:  12:08
:corn:
12:09
-420 btw
janet
high temp hydrogen attack :arrow_up: 341 / :arrow_down: -420 sekiro enthusiast
From a thread in #advent | Yesterday at 12:07 | View reply
:heart_eyes:
1


High Temp Hydrogen Attack:turtle:  12:09
ti ezalb
:learn:
1


1 reply
21 hours agoView thread

sekiro enthusiast  12:10
go check out https://ohshitgit.com/ again now that you're a jedi master and for each problem and solution see if you can
- imagine how a graph might look in the "broken" state described by the problem
- understand what katie's suggested commands do to "fix" that state
- what the graph might look like in the fixed state

High Temp Hydrogen Attack:turtle:  12:11
oh shit I have homework

sekiro enthusiast  12:11
heads up, just from skimming this - some of these situations don't change the shape of the graph, just the contents :no_mercy:

High Temp Hydrogen Attack:turtle:  12:12
coolcoolcool
12:13
also can I mention how annoying it is to me that there wasn't a way to draw the green and purple (lol) nodes without having their lines cross somewhere?
High Temp Hydrogen Attack
image.png
image.png


Thread in #advent | Yesterday at 12:06 | View message
12:14
hmmmm I suppose I could have swung the green (rightmost) one up so it went over and around the blank node at the top

sekiro enthusiast  12:15
hm yeah i suppose
12:15
that's rough though
12:15
alternatively you could swap the positions of the uh... blue? one? and the...green? one?
12:15
because those are in equivalent positions
12:15
oh wait
12:15
they both point to that other one
12:16
well this is why merge commits fucking blow
:lol:
1

12:16
commits should have exactly one (1) parent fite me

High Temp Hydrogen Attack:turtle:  12:16
I guess I was stuck with the idea of a tree, but it isn't a tree because nodes have multiple parents
12:16
or something
12:16
yeah okay

sekiro enthusiast  12:17
this is fun because now you get to hear some of my stupid opinions on new tech stuff
:heart:
1


High Temp Hydrogen Attack:turtle:  12:17
lolol

sekiro enthusiast  12:17
the only way that a commit can have more than one parent is if a merge occurs
12:17
this causers a special merge commit to be created
12:18
you've already discovered that having multiple parents makes the graph suddenly more than twice as complex
12:20
me and my team at etsy actually don't ever create merges this way. We use a git operation called rebase ing. a rebase lets you eliminate merge commits but you do have to "rewrite history" aka, change a single commit's parent, which is also generally a little risky-feeling. If you never change history it's basically impossible to lose data. Once you start fucking around in the past it gets a lot more likely that you'll just lose some stuff entirely with a bad graph operation because we're all just fish with fur (edited)

High Temp Hydrogen Attack:turtle:  12:21
like people disappearing out of pictures in back to the future :seemsgood:

sekiro enthusiast  12:23
^
12:23
i'm trying to find a gif of rebasing
12:25
it's like if your main branch has commits
A B C
and you create a new branch at C and add commit D. So that branch 2 now looks like
A B C D
then someone else comes along and adds E to the main branch so
main: A B C E
other: A B C D
if you were to merge you'd end up with a new commit on main called F with both D and E as its parent. I'm not going to attempt to draw this in ascii. You did the mspaint, you get it

High Temp Hydrogen Attack:turtle:  12:25
:nod:

sekiro enthusiast  12:26
a rebase creates a new base for your branch so in our example we made a new branch starting on commit C. rebase let's us say "okay go back and change our base commit to E. That includes C , where we actually departed from, plus some extra stuff"
12:26
there's only a problem if the same file has changes on the same lines in both commit E and D
12:26
and that's a problem for both merges and rebases
12:27
either way you get a "merge conflict" (sometimes called a rebase conclict while rebasing, but all rebase conflicts are in fact file merge conflicts as well)

High Temp Hydrogen Attack:turtle:  12:27
okay that makes a reasonable amount of sense, but what does changing the base of other branch accomplish? (edited)

sekiro enthusiast  12:27
and you the miserable human being with a brain have to resolve the merge conflict using your thinking and typing
12:27
aaah right ty that's the last piece here

High Temp Hydrogen Attack:turtle:  12:28
can I try and figure it out first?
:nod_fast:
1


sekiro enthusiast  12:29
spoilers

okay so now that we've rebased other onto the newest copy of master we can do a "fast-forward" merge instead of a "three-way" merge. Fast-forward merges maintain the linearity of our graph :chefs-kiss:
main: A B C E
other: A B C D
$ git checkout other
$ git rebase main
main: A B C E
other: A B C E D
$ git checkout main
$ git merge other --ff-only
main: A B C E D
other: A B C E D


1 reply
21 hours agoView thread

High Temp Hydrogen Attack:turtle:  12:29
changing the base of other from C to E is basically just adding E to the branch, because everything else is the same (or there'd be an error)
:nod_fast:
1

12:30
so the main has A B C E and other has A B C E D
12:30
and at that point, merging is basically just adding D to main?
:this-hand:
1


sekiro enthusiast  12:31
my spoiler has the actual git commands you'd use to do this

High Temp Hydrogen Attack:turtle:  12:32
can you explain this? Fast-forward merges maintain the linearity of our graph
12:32
oh
12:32
so since we moved the base of the branch to the front of the "line" of our linear main branch
12:33
it's basically the new front (edited)

sekiro enthusiast  12:33
we avoid ever having a commit with two parents
12:33
since the only reason that we had a problem was that someone added to main
12:33
if no one ever added to main then our branch could zip right back in as though it never existed

High Temp Hydrogen Attack:turtle:  12:34
right
12:34
got it

sekiro enthusiast  12:34
and in fact it doesn't really exist branches are pointers, so it'd just be pointers moving along the same line, in a parallel fashion
12:34
so the rebase is necessary once we get commit E since there's no existing line connecting E to D
12:35
that feels more confusing tbh

High Temp Hydrogen Attack:turtle:  12:35
maybe, but I get it

sekiro enthusiast  12:35
lol phew
12:35
let's see what the graph of a work repo looks like

High Temp Hydrogen Attack:turtle:  12:35
since the entirety of main is in other, main isn't really a parent to the merge
12:35
it's a parent to other
12:36
it's a straight line, but slightly bent and then bent back

sekiro enthusiast  12:36
:nod: or we could say that main has just fallen behind
12:36
because if it's all a straight line, it's just that main is one step from the end of the line (edited)

High Temp Hydrogen Attack:turtle:  12:36
do branches ever get abandoned?

sekiro enthusiast  12:37
yes and branch hygiene is a thing
12:37
http://d34db33f.s3.amazonaws.com/2020-12-07T12%3A37%3A21%2C762671129-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607967444&Signature=bV014PxM12EHa%2B2GMW6EbN9U15U%3D

(333 kB)
http://d34db33f.s3.amazonaws.com/2020-12-07T12%3A37%3A21%2C762671129-05%3A00.png?AWSAccessKeyId=AKIA6DX2Z72FIUSQBIXV&Expires=1607967444&Signature=bV014PxM12EHa%2B2GMW6EbN9U15U%3D

High Temp Hydrogen Attack:turtle:  12:37
do they get deleted? From what you said before, you don't want to fuck with the past, but what about parallel universes?

sekiro enthusiast  12:37
branches are just pointers so deleting a branch is honestly whatever
12:38
you can end up with orphan commits but those won't be deleted immediately either

High Temp Hydrogen Attack:turtle:  12:39
branches are just pointers
12:39
you can delete branches without deleting the commits on that branch?
:nod:
1


sekiro enthusiast  12:42
an orphaned commit starts in our situation like above
main: A B C
other: A B C D
but then if we were to delete the other pointer that's pointing at commit D then suddenly there's no easy way to get back to commit D. Nothing is pointing at that commit. It's just all alone, un-named and unknown. Git will let you do this, but you have to say "yes, i really mean it" because orphaned commits are kinda risky. Git will automatically find and delete orphaned nodes over time as a garbage collecting process, so if you didn't mean to orphan a commit, it's worth slapping a label on that commit (aka putting it on a branch).
$ git branch
* main
  other
$ git branch -d other
error: The branch 'other' is not fully merged.
If you are sure you want to delete it, run 'git branch -D other'.

High Temp Hydrogen Attack:turtle:  12:43
so the email you get about stale branches, do commits get orphaned when you're deleting them? Or do you delete the commits as well

sekiro enthusiast  12:44
so most of those have been merged into main

High Temp Hydrogen Attack:turtle:  12:44
so all those commits still have a pointer somewhere

sekiro enthusiast  12:44
at work usually one or main branch is used for deploying to real infrastructure
12:45
they don't have a pointer specifically to them but they are contained in the history of a node with a pointer :grimacing:

High Temp Hydrogen Attack:turtle:  12:45
mmmmmmmmmmm
12:45
okay yeah

sekiro enthusiast  12:45
so like in the case of ABCD only D needs to have a branch pointing at it
12:45
also there are things called tags

High Temp Hydrogen Attack:turtle:  12:45
shhhhhhhh

sekiro enthusiast  12:45
tags are identical to branches

High Temp Hydrogen Attack:turtle:  12:45
no new stuff
12:45
stahp

sekiro enthusiast  12:45
but they do not move automatically
12:46
no but you already have thought "I bet this exists"
12:46
and it does
12:46
a tag is a branch that doesn't move when you commit. It's a static pointer.
12:46
ok ok i stop
12:46
i stop

High Temp Hydrogen Attack:turtle:  12:47
okay there seems to be nuance there
12:47
but I can't at the moment
12:47
I need to shower and go to the dump and work

sekiro enthusiast  12:47
yeah i gotta work too it's lame
12:47
okay thx for chilling

High Temp Hydrogen Attack:turtle:  12:48
I'll have to scroll back through all this and add to my notepad notes


