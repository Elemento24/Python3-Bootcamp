# In this, we will see a nice Decorator Function (not built-in)
# The 'enforce' decorator checks the types of the arguments of a function
# Also, it try to change the types of the arguments into specified types, if possible


def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # As we know that args is a tuple, so we try to convert it into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append(t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


@enforce(float, float)
def divide(a, b):
    print(a/b)


repeat_msg('Hello', 5)
repeat_msg('Hey', '5')

divide(1, 2)
divide('1', '2')
