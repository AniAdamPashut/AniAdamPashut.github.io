---
title: Python Decorators
...

# Python Decorators

Decorators are a cool feature that the python language contains. In this post I'll showcase decorators as well as one easy practical example. But first, What is a decorator and how does it work?

## The W's

I already answered the what so I'll go straight to the how, why and where.
A decorator is noted at the top of a function's signature using the `@` symbol. See the following example as reference.

```py
@decorator
def function():
    pass
```

Please note that this is equal to doing `function = decorator(function)`. The order of execution for multiple decorators is as follows

```py
@dec2
@dec1
def function():
    pass
```

Translates to:

```py
def function():
    pass

function = dec2(dec1(function))
```

Lastly, I will establish the why. Why do we need decorators? But this question has a flaw inside, It's way too general. Decorators are no more than syntactic sugar and have many many use-cases. So I will instead ask, What do decorators allow us to do. And the answer to that question is pretty simple. Decorators allow us to play with a function's inner object before execution in a nice manner.
<br><br>
To Demonstrate it I'll show some use-cases. The @property decorator allows us to create a getter for a property on an object. The @cache decorator allows us to enable memoization for a function. The options are endless but one thing stays consistent. Decorators increase efficiency.

## Curry is a dish 🥘
Currying is a powerful technique in functional programming that allows the use of multiple "middleman" functions. Currying allows us the separate the load on different function in a chain-like setup. Although this happens automatically in functional languages (e.g. Haskell, OCaml) it is not in python, but we can still utilize it.

A simple example for currying is an add function. A normal un-curried function would look like this
```py
def add(x, y):
    return x + y
```

An example that contains currying looks like this
```py
def add(x):
    def adder(y)
        return x + y
    return adder
```

This allows us to bind the `x` variable to the function and reuse it multiple times. 
```py
add3 = add(3)
print(add3(2)) # 5
print(add3(7)) # 10
print(add3(69)) # 72
```

The use of currying helps us when using decorators because the decorator can be an Expression. This means that I can bind a value to my decorator function while also using the function to decorate.

```py
def curry(x):
    def actual_decorator(method):
        print(x)
        return method

    return actual_decorator
    

@curry(3)
def func():
    ...
```

Since the `curry(3)` expression evaluates to a decorator function it's still valid python code with the addition of the curried value bound to the decorator function.

## Flask is a cool framework

Anyone familiar with flask knows `app.route()` function. It haunts us everywhere. The infamous flask's "Hello World" example feels magical. Let's have a look at the flask "Hello World" example.

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    return "hello, world"

app.run()
```

This snippet is kinda obvious, you import flask, create an application and run it. The more *magical* part is the root function. How does it bind the root function to run on each request to the `"/"` endpoint? To answer this question I will create a class that will try to mimic the `Flask` function. The class will hold 3 functions `__init__`, `run` and `route` (I will only implement `route`).


```py
from typing import Callable

class SoNotAFlaskCloneForReal:
    def __init__(self):
        self._endpoints: dict[str, Callable] = dict()


    def run(self):
        ...

    def route(self, ep):
        def actual_decorator(method):
            self._endpoints[ep] = method
            return method
        return actual_decorator
```

Utilizing this class will be the same as utilizing the `Flask` class. This is all thanks to the currying function `route` returning the curried decorator. An example of execution is included below and a full working example with a server is included in the github repo of this site.

```py
app = SoNotAFlaskCloneForReal()

@app.route('/')
def root():
    return "Hello, World"

app.run()
```

## References
- [decorators](https://peps.python.org/pep-0318/)
- [@property](https://docs.python.org/3/library/functions.html#property)
- [@cache](https://docs.python.org/3/library/functools.html#functools.cache)
- [currying (general)](https://www.linkedin.com/advice/0/what-currying-functional-programming-how-can-you-bfyhe)
- [currying (haskell)](https://wiki.haskell.org/Currying)