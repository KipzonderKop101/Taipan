# Introduction
Taipan is a Python based programming language build for an easy to understand source-code. Taipan is inspired by Basic, but is actually Basic. But instead of it being just Basic, we are also inspired by Python. 

Taipan is designed to be understandble. Also for people who are not known with code. Our mission is for anyone to understand what the code will output, even if they have never worked with a programming language!

But of course like any programming language that requires a good set of docs so you can understand how to use it. And the Taipan version is right here in the readme! We are working on a more detailed and better doc and you can expect that to release soon. 

Now, for the practial information. As mentioned before Taipan is inspired by basic and that allows it to be understandble. And for someone who has worked with code before this doc will be overkill. But for new comers to the language or just code in general, here are the docs.

Quick word before we start. We would like to thank you for choosing Taipan and trying it out! We hope you have a great expierence with Taipan. We are realising updates on the regular. 

To people with ideas. If you have any plan on how you'd like to see the language change. Let us know! We would love to upgrade our language and making it more user friendly.

As mentioned Taipan is inspired by Basic. So a lot of things will be simulair. But there is a mix of Python thrown in there, and we are working on giving it it's own 'twist'. We 

Taipan knows all the letters and numbers of the English alphabet. And you can use all of those.

# Installation

There are few ways to install Taipai. The first being downloading the code and running it inside of your terminal. This is not the most efficient way but for some people the source code can be needed. You are free to download the code in this rep.

You need to put all of the code into a folder and than run `shell.py` with your favorite code editor.

This will open up terminal and write `taipan ~ >` which means it is ready to go. From that point you can write your code and type enter and your code will be processed.

`Taipan IDE` 

The second way, and also the way we recommand you download, is by downloading the Taipan IDE. Which includes the language. This is just clicking the download button and following the set-up. 

# The docs

Taipan can do easy math just as how you would calculate it on a piece of paper. It calculates the awnser fast for you and gives you a simple anwser. No printing needs to be done.

Here is a list of the operators it nows 
- `+` add two numbers to each other
- `-` substract two numbers from each other
- `*` multiply two numbers
- `/` divide a number 
- `(` or `)` to change the order it calculates in

As you can see there are all very easy. But we will show you some examples.

```
5 + 5 
-----
output: 10
```

```
10 - 5
-----
output: 5
```

```
10 * 10
-----
output: 100
```

```
10 / 2
-----
output: 5
```

```
10 + 2 * 5
-----
output: 20
``` 
output will be 20, because `*` and `/` go before `+` and `-`. So the `2 * 5` will be calculated first and than the outcome of that will be added to 10. 

But you can change this with `()` 

```
(10 + 2) * 5
-----
output: 60
```
output will be 60. Since it will calculate `10 + 2` first, which is 12. And than will multiply that by 5, resulting in 60.

You can also use this with variables
```
var a = 5
var b = 15
a + b
-----
output: 20
```
output will be `20`. Since `a` holds a value of 5 and `b` of 15. And 15 + 5 = 20.

# Variables

Variables work really easy in Taipan. The keyword for a variable is `var` and you can give it a name and value. 

For example 
```
var a = 5
-----
output: 5
```

This will create a viarable called a with a value of 5.

You can create multibale variables and than add, substract, divide and multiply them with ease.

That would look like this
```
var a = 5
var b = 9
a + b
-----
output: 14
```


# Comperisions and logic operators

Taipan knows a few comperisons which will return either `1` for true or `0` for false. This way you can check if a value is True or False, which you can use in if statements.

- `>`  is bigger than 
- `<`  is less than
- `==` is equal to
- `!=` it not equal to
- `>=` is bigger than or equal to
- `<=` is less than or equal to

for example
```
1 > 2
-----
output: 0
``` 
Because 1 is not more than 2

```
1 < 2
-----
output: 1
```
Because 1 is less than 2

```
2 == 2
-----
output: 1
``` 
Because 2 is equal to 2

```
3 != 3
-----
output: 0
```
Because 3 does equal 3 and there is not false

```
3 >= 5
-----
output: 0
```
Since 3 is not bigger or equal to 5

```
2 <= 5
-----
output: 1
```
Since 2 is less or equal to 5

Of course all of the comperisons can also be used with variables too.

```
var a = 5
var b = 7

a >= b
-----
output: 0
```
Since 5 (variable a) is not bigger or equal to 7 (variable b)

Logic operators work with Taipan as well. Here is a list of the Taipan support logic operators.

- `and` Will return 1 (True) if **both** values are true
- `or`  Will return 1 (True) if **one** of the values is true
- `not` Will return 1 (True) if something is **not** true

So for example

```
5 == 5 and 7 == 7
-----
output: 1
```
Since 5 is equal to 5 **and** 7 is equal to 7

```
7 == 4 or 3 == 11
-----
output: 0 
```
Because 7 is not equal to 4 or 3 is not equal 11. Both values are false, so it will return false.

# If statements 

Taipan if statemenst are mostly written on one line. But for the rest they work like you'd expect them to. If something is true, then do something. 

Examples
```
var a = 25
var b = if a == 25 then 20
-----
output: 20
```
This code above returns 20 because a is equal to 25. 

Now let's see what happens when the if statement is not happening
```
var a = 25
var b = if a == 15 then 20
-----
output: 
```
As you can see it will give no output. Because the rest of the if statement will not be read, since the if statement is not true.

Let's use the it now with else
```
var a = 15
var b = if a == 25 then 20 else 30
-----
output: 30
```
This code will return 30, since a is not equal to 25 it will check for the else, which returns 30

Now let's use this in an actual useful code
```
var age = 20
var price = if age >= 18 then 40 else 20
-----
output: 40
```
This code will check if the age is above or equal to 18, if so, the price will be 40. Otherwise it will be 20

# For statements

For statements, simply put, is a statements that keeps running until whatever condition it has is satisfied. This is also how they work inside for loops. 

```
var result = 1

for i = 0 to 6 then result = result * i
-----
output: 120
```
The code above will output 120

# While statements

While statements will run for as long a statement is true. Meanining you can create loops.

```
var result = 5

while result = 5 then 123
-----
output: 
```
There will be no output because you need to use print for this to actually work. 


