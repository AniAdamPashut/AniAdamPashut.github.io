# Mapping

Functional programming (FP) heavily affect the way we program. Almost all programs use one or more aspects of functional programming. Even when using OOP (which often seen as the arch nemesis of FP) we use FP methods to better our code.

## Recursion, Immutability and Purity
Functional programming consists of methods and practices that might conflict with our current view on programming. In a functional language (e.g haskell) we cannot mutate a variable. Everything is constant. Assume we have an array of integers and we want to print it. A non-functional approach could look like this.
```
void print_array(int *arr, int len) {
    for (size_t i = 0; i < len; i++) {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}
```
But this way has a flaw in it. We mutate the `i` variable repeatedly on each iteration of the loop. Remember, this is not allowed in functional languages. Functional languages work around this with the use of recursion. A recursive function approach could look like this:
```
void print_array(int *arr, int len) {
    if (len == 0) {
        printf("\n");
        return;
    }
    printf("%d, ", *arr);
    print_array(arr + 1, len - 1);
}
```
A functional language prefer this approach as it keeps the functions *pure*. A pure function will produce no "side-effects" and it's output will only depend on it's input. (The example above is impure but it demonstrates the use of recursion) For example the function `lambda x: x + x` in python is a pure function as it produces no side effects and the output is based solely on it's input.

## Python's map function

The built-in function `map` is a very useful function. Do you know that it has functional origins? Let's try to create it by ourselves and step by step return to the functional origins. First, we would create a function that takes a list of integers and adds one to each. Just to get a sense of what we want to do.

```py
def step_one(array):
    result = []
    for x in array:
        result.append(x + 1)
    return result
```

This approach works, but it's not as extendable as the build-in map function. let's try to make it more adaptive. instead of computing the value inside our function we will take another function that computes it for us. That way we won't have to create a new function for each transformation.

```py
def step_two(transform, array):
    result = []
    for x in array:
        result.append(transform(x))
    return result
```

This function also works and it's adaptive. So we can stop here. Just kidding, we can't. This function is impure. Due to `result.append` the function mutates a variable and produces a side effect. Let's try to come up with a more functional way. Maybe recursion will solve this problem.

```py
def step_three(transform, array):
    if len(array) == 0:
        return []
    
    return [transform(array[0])] + step_three(transform, array[1:])
```

Now this is a pure function. This function produces no side effect. But This function is kinda awkward a simple `(transform(x) for x in array)` would suffice. Because python is a mutable language in it's nature it seems weird to try and avoid it. Using a functional language will do this justice

## A Functional Map
```fs
let rec mapOnList transform xs =
    match xs with
    | [] -> []
    | first::rest -> transform first :: map' transform rest
```

This function is pretty simple. We get 2 arguments, `transform` and `xs`. We match `xs` against the empty list, any map on an empty list will result in an empty list so we use it as the base case for our recursion. If `xs` is not empty, we split it to 2 parts. Its head, the first element and its tail, the rest of the elements. A python translation of this will look somewhat like this:
```py
first, tail = xs[0], xs[1:]
```
We apply the transformation on the first element and append the result of the rest of the elements recursively. We then append it to the transformation of the first and return it.

## Map is Just an Elevator

All of this is very nice, but it isn't what the map function really is. Generally, the job of a map function is to elevate another function from a base world to an elevated world. For example, let's define an add 1 function: `let add1 x = x + 1`. The add1 function operate on integers. The integer world is our base world. Using the map function we can create a function that will add 1 to each number in a list of integers `let addOneToEach = mapOnList add1`. The map function elevates the add1 function from its base domain (integers) into an elevated domain (integer lists). In the same way, we can define a map function that will work on option types. 

```fs
let mapOnOption f opt = 
    match opt with
    | None -> None
    | Some x -> Some (f x)
```

A function such as `let addOneToSomeValue = mapOnOption add1` that will take an `int option` and will return another `int option` with the wrapped value increased by one. Though the implementation is different the concept is the same. We take a function `f` and change it's domain. 

## References
- [Dear Functional Bros](https://www.youtube.com/watch?v=nuML9SmdbJ4)
- [Elevated World](https://fsharpforfunandprofit.com/posts/elevated-world/#map)
- [Maps and Filters](https://learnyouahaskell.com/higher-order-functions#maps-and-filters)
