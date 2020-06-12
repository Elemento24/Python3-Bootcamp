# We can also use a Generator Expression over Lists, when we are dealing large data
# They will save a lot of memory, though they might be slow as compared to lists

# def fib_list(max):
#     nums = []
#     a, b = 0, 1
#     while len(nums) < max:
#         nums.appedn(b)
#         a, b = b, a+b
#     return nums

# The above approach will return a list of all the Fibonacci Numbers

def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x+y
        yield x
        count += 1

# The above approach just returns a single Fibonacci Term at a time, unless we call next() on it


for n in fib_gen(10):
    print(n)
