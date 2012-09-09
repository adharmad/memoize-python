# memoize module in python
# This is implemented as a class and can be used as a decorator
# for any function call
# Usage:
# @Memoize
# def functionName(arguments):
#   ...
#

class Memoize:
    def __init__(self, f):
        self.f = f
        self.cache = {}

    def __call__(self, *args):
        # Construct a cache key from the function name and arguments
        cacheKey = self.f.__name__
        for a in args:
            cacheKey += '_' + str(a)

        if not cacheKey in self.cache:
            self.cache[cacheKey] = self.f(*args)

        return self.cache[cacheKey]
