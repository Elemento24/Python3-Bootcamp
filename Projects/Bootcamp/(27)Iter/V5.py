# def current_beat():
#     max = 100
#     nums = (1, 2, 3, 4)
#     i = 0
#     result = []
#     while len(result) < max:
#         result.append(nums[i])
#         i = (i+1) % 4
#     return result


# print(current_beat())

# If we want to create some function which will keep on iterating, as and when called...
# ... then, we could go with the function as above, and have a very large list and iterate over it

# Or we could just use an infinite iterator function

def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        yield nums[i]
        i = (i+1) % 4


counter = current_beat()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
