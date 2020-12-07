# uh oh, graph theory

So before i give a specific answer to each of the questions in _uh oh, graph theory_ I'm going to just talk about the guts of git because it makes the answers make sense. Otherwise it's kind of just arbitrary "because i said so"

The title of the section is a spoiler but Git is a *graph*. Maybe you remember graph theory from being a nerd or from college or whatever.

Here's a picture of a graph. You don't have to look too hard at it, there's no specific examples relating to this graph. i just like having examples to look at

![A simple Git graph. The red circles represent bug-fix commits.](https://www.researchgate.net/profile/Liqian_Chen/publication/326104038/figure/fig1/AS:708614083858432@1545958171047/A-simple-Git-graph-The-red-circles-represent-bug-fix-commits.png)

Graphs consist of *nodes* which are the circles in the image above and *edges* which are the lines which connect the nodes. Git uses this concept to store merging and branching code changes. There are some specific rules that git graphs have to follow, specifically. This is actually not too important but it's cool to know the deets. In Computer Science words git's graph is a specifically a _directed acyclic graph_
1) The edges are one-way. That is, the edge between any two nodes is *directed*. It only goes one direction. In practice this means that git nodes specify their parents, not their children.
2) Loops are not allowed. Git will not let you create a situation where a node is, directly or indirectly, its own child. This feature of forbidding circular dependencies is called being _acyclic_.

I'm so sorry, this is absolutely real and this is real software that people use every day and it's just solid wall of of graph theory if you want to know why it is the way it is.

Here's another picture of a git graph. This one is has the arrows going in the correct direction for git's DAG behavior. In this figure time is flowing from left to right, and the arrows are pointing from right to left - backwards - from each commit to it's parent commit.
![Image for post](https://miro.medium.com/max/500/1*bkT3ig0T_VRkQpTb1XjZGA.png)

~~okay skip to here if you don't want to read about what graphs are and stuff

So Git uses a graph to represent changes that occur to a folder full of text files  (i.e. a repo of code) . Every commit is a node in the graph that has a pointer to its parents and a stored copy of the changes you comitted.  Your fundamental, atomic operation for storing code in git is creating a commit -- that is creating a node. `git commit` is your generative tool in git. But you have to do the work of deciding when to commit. And you also get to/have to control where in the graph your new commit goes. Manually creating commits is your burden as a living, thinking human. I feel like that's not a helpful thing to say. But what i'm trying to say is that you make commits because the data structure git is based on _is_ the concept of commits. this *is* the game. In order to track your changes git uses the idea of commits, so we must make them to use git.

I want to show an example of how git creates a graph, commit by commit from an empty repository.

```console
# make an empty folder
$ mkdir test_repo
$ cd test_repo

# initialize git in this folder
$ git init
```

At this point i have an empty folder and that folder is also an empty git repository. If I ask git to show me a visual representation of the graph that is this repo? well it's going to be empty also since we have no files

```console
# hey, git, show me this graph.
$ git log --oneline --graph
fatal: your current branch 'main' does not have any commits yet
```

 So next i create a single file. At this point i haven't made a commit so our graph will still be empty

```console
# create a new file called "example1"
# and write the string "adamis20" to that file
$ echo "adamis20" > example
$ git log --oneline --graph
fatal: your current branch 'main' does not have any commits yet
```

My next step is to add the new file to the staging index. At this point there STILL won't be a single node in our graph. The staging index is a collection of files that will be part of the next commit. Since commits are the fundamental building blocks of git, it's nice to have a staging area that lets you choose what goes into a commit before you pull the lever.

```console
# our new file is going into the next commit
$ git add example
```

At this point everything is ready to go and we create the first node in our graph - often called the `initial commit` or `root commit`

```console
# create the initial commit
$ git commit -m "big bang"
[main (root-commit) f9feac5] big bang
 1 file changed, 1 insertion(+)
 create mode 100644 example

# check it out we've got a node (commit) in our graph (repo)
git log --oneline --graph
* f9feac5 (HEAD -> main) big bang
```

Now I'm going to make a change to the file and commit that as well and show that creates another node in the graph.

```console
$ echo "adamis30" > example # change the file
$ git add -u # stage the file
$ git commit -m "the years start coming" # make a commit
[main 68b227c] the years start coming
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git log --oneline --graph
* 68b227c (HEAD -> main) the years start coming
* f9feac5 big bang
```

You can see that there is now a second entry in this list: the new commit. This small two-commit git repo could continue on in this same way forever. One commit following its parent on down the line towards infinity. `A -> B -> C -> D` and so on. This pattern of use is common and cool. Your repo is a linear graph, and you can see that here in the CLI

```console
~ ❯❯❯ cd development/AdamAdvent2020/
~/d/AdamAdvent2020 ❯❯❯ git pull
... blah blah blah ...
~/d/AdamAdvent2020 ❯❯❯ git log --oneline --graph
* a7e2b01 (HEAD -> main, origin/main, origin/HEAD) day 6 code
* a4921a2 added day 5 code part 1 and 2
* 3a0b6ad added finished code for part 2 day 4
* e41d041 Add files via upload
```

or you can see a more graphical representation [here on github](https://github.com/Trainpants/Advent2020/network).  Your repo is a graph of 4 commits in a line.

History tangent: Git isn't the first thing like git. This type of tool for managing code is called a "version control system". Many pre-git version control tools didn't offer the ability to do branching, so this linear model that we've looked at so far for got was basically all you got in the 80s, 90s and early 2000s. So the ability to do fast, nearly unlimited branching in git was a complete game changer.

Summary so far:
Git is a graph
Commits are nodes
Create commits to store code

I think we can talk about branches now. While it may feel like branches are independent working copies of your code, that's not really the case. In fact branches are just pointers to commits. They are a little more than *just* a pointer. Theyr'e an auto-advancing pointer. This is an annoying definition alone. It's almost a trick. So I want to make a practical example of a normal use of a branch and examine what a branch is there.

When you start a repo you begin with on default branch and it's pointing at nothing. When you create an initial commit git points the default branch at the initial commit. You can see that in the examle earlier in the weird parenthetical string  `(HEAD -> main)` when the first commit is made.

Branches are auto-advancing, so if you We're already using a branch by default in git. Git has a "default branch" which has historically been called "master" but recently When you make a new branch that doesn't create a new commit.

and that the weird parenthetical string  `(HEAD -> main)` moved from the first commit to the new commit. For reference, here's what the graph of the demo repo looked like at the initial commit.

```console
git log --oneline --graph
* f9feac5 (HEAD -> main) big bang
```

This is saying that the branch `main` is pointing at the commit `big bang`.  The magic of branches, if there is any magic, is that they auto-advance when you create a new commit. So when I changed the file and comitted that, then `main` automatically advanced to point at the new commit. When you create a commit your current branch is always advanced to that newest commit.

You can make new branches and point them at other commits for free. Our demo repo has 2 commits and one branch. That branch (`main`) is pointing to the most recent of those two commits. So I'm going to create a new branch and point it to the same commit as `main`

```console
# what branches exist? just main
$ git branch
* main

# make a new branch
# new branches point to the current commit
# by default
$ git branch b2

$ git branch # show all branches
  b2
* main

# now both branches point at the same commit
$ git log --oneline --graph
* 68b227c (HEAD -> main, b2) the years start coming
* f9feac5 big bang
```

At this point we've got a repo with two branches and two commits and both branches are point at the latest commit

```
1     2
o  -- o
      ^ main AND b2
```

Now I'm going to make a new commit. I'm still *checked out* to `main` which is an important distinction. When I commit only the pointer for my checked-out branch will be advanced to the new commit. So in this case, `main` will move forward to a new third commit, but `b2` will remain at the second commit.

```console
# delete our one and only file
$ rm example
# stage the deleted file
$ git add -u
# commit the deletion
$ git commit -m "rip"
[main 1ccf75b] rip
 1 file changed, 1 deletion(-)
 delete mode 100644 example

# main is on our new commit
# b2 is on the old commit
$ git log --oneline --graph
* 1ccf75b (HEAD -> main) rip
* 68b227c (b2) the years start coming
* f9feac5 big bang
```

Now our graph looks like this with branch pointers

```
1         2         3
o ------- o ------- o
          ^ b2      ^ main
```

A branch is just a pointer. There are commands for moving branch pointers to arbitrary locations in the graph and all sorts of other nonsense that is only possible or reasonable because a branch is not any real set of files, it's a way of manipulating your view of the git graph.

I think maybe i will try to answer your original questions now

- can you have more than one commit on a branch at a time?

Yes? Sort of? No?
A branch can point to any commit. If a branch points to the commit at the end of a chain of 4 commits, then does that branch "have" more than four commits? In a way a branch can only ever have one commit and that is the single commit that the branch points at. Branches cannot point at multiple commits, that much is easy to say.

- does the second one overwrite the first?

branches do sort of work by being "over-written" when you make a new commit. In that the branch itself will automatically move to point at the most recent commit that you made. But since all commits keep track of their original parent commits there's no way to lose track of that intermediary commit. If you make multiple commits on a branch you just get a longer and longer graph. One of the fundamental rules of git is that the past is immutable. Once a commit has been made you shouldn't go manipulating what parents that commit has or changing the content of the commit. You can always go forward by creating more commits, but if you go back and delete or manipulate history you can risk damaging your past and that's philosophically heavy and technologically annoying. I guess i would say if you're following good git hygeine you'll never overwrite anything. That may be too extreme of a maxim but it's close to right.

- I guess I'm mostly unsure why I'm committing

i don't want to belabor the point on this one.


Okay, that's it, that's the graph theory i've known was going to be a challenge to write. I hope it's an enjoyable challenge to read too.
