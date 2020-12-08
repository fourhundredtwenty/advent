Okay so everything across those 6 lines is a list comprehension, just stretched out and made multi-line. A list comprehension is a for loop inside of an empty list whose output is appended to that empty list that. If you feel like you already get list comprehensions then skip to the very last line and i'll see you again soon. If you're still here that's neat.

So these are exactly equivalent

```numbers_around_five = []
for i in range(10):
    numbers_around_five.append(i)```
and

```numbers_around_five = [i for i in range(10)]```
list comprehensions are built out of 3 parts and only one is optional

We're starting in the middle out, so first of all there's the part that looks like a for loop in the middle of this list. It is exactly a for loop. You say what iterable object you want to iterate over and you specify what variable name you want to use to reference that element and the rest of the list comprehension references that variable and gets executed once for each element in the input iterable (the input here is `range(10)`)

```[i for i in range(10)]
    ^^^^^^^^^^^^^^^^^```
anything you can put in the `for` line of for loop can go in this position in a list comprehension. The rest of the list comprehension has access to the variable name you choose here in the loop declaration.

The first `i` inside the brackets is equivalent to the value inside of the `append(i)` call from the for loop example.


```[i for i in range(10)]
 ^```
You also have the opportunity to modify that value before outputting it. So for example you can use this accumulator position to generate some powers of 2

```>>> [2**i for i in range(10)]
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]```
The last part of the list comprehension is a conditional. This is like adding an `if` statement inside of a for loop, for example

```odd_numbers = []
for i in range(10):
    if i % 2:
        odd_numbers.append(i)```
is the same as

```>>> [i for i in range(10) if i % 2]
[1, 3, 5, 7, 9]```
And that's really it for the conditional. It's an if statement. If it evaluates to false then you throw away the value and if it evaluates to true then you go over and evaluate the accumulator position and append that value to the list.

---

Okay so that's just the list comprehension side. There's three parts. Next I'm gonna point out the three parts in my code and how they work together by these same rules. But now i have to write that bit! I'm also down to answer any questions about this because idk if it's clear at all
