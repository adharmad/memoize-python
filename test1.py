from memoize import Memoize

@Memoize
def foo(s1, s2):
    print ("s1 = ", s1)
    print ("s2 = ", s2)

@Memoize
def square(x):
    return x*x

if __name__ == '__main__':
    #foo('hello', 'world')
    #foo('hello', 'world')
    
    square(1)
    square(2)
    square(1)
    square(2)
    square(3)
