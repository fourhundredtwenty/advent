High Temp Hydrogen Attack:turtle:  11:35
is there a consensus on where to put comments?
do you put them on the same lines as code?
is it bad to interrupt loops with comments?


The answer is really "do whatever feels good for you" but you're right to guess that there's a Whole Fucking Set Of Opinions about this. Python in particular is a language with real conventions and standard idioms for style. There's an official style guide called PEP 8. PEPs are Python Enhancement Proposals they're official documents by the community of developers that do things like propose new syntax and data structures, or new additions to the standard library, or in the case of PEP #8, a description of the style recommendations - a "style guide" . https://www.python.org/dev/peps/pep-0008/ idk what it says about inline comments though

Here's my personal take on style for comments
- if it's really short you can put a comment inline with your code
int(blob, base=2) # converts a string of 0s and 1s to int
and even that feels like it's cutting it close on being too long of an inline comment.
Also there's a tradition that you shouldn't make any one line go past 80 columns. This is an antiquated rule because it only stems from the fact that the old IBM punch cards were 80 columns wide which lead early teletypes to also be 80 columns wide in order to display the data. 80 columns is an arbitrary number that you should never have to follow. But trying to keep lines relatively short does help readability. And it also lets people with poor eyesight increase their zoom levels a lot without getting demolished by line wrapping.
- if i'm gonna go over 80 columns i try to split my code up into little functional blocks and put my comment above the most relevant of those lil blocks. If that block is inside of a loop or a function definition that's cool. But often when i start to write something inside of a function i realize i also need to write a short description of the function itself above the function signature so that my stuff inside makes sense.

PS, i've started using a super opinionated auto-formatter for my solo projects so that i can stop thinking about code formatting in general. The one I use is called Black as in "any color you like as long as it's black" https://github.com/psf/black. no matter how you write your comments black will just reformat them to be in-line with its demands.
