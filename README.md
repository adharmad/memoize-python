A simple memoize module in python.

Memoization is a technique to improve performance by caching results of
idempotent function calls. 

The simplest example is while calculating fibonnaci numbers in a
manner. 

fib(0) = 1
fib(5) = fib(4) + fib(3)
       = (fib(3) + fib(2)) + (fib(2) + fib(1))
       = ...

As noted, while computing fibonnaci numbers there are repeated
invocations of the fibonnaci function with the same parameter which in
turn results in more resursive and repeated calls. By using memoization,
the result of a function call can be cached and instead of computing the
result of the function again, the value can be fetched from the cache.

