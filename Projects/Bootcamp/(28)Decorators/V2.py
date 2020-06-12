# Decorators are functions (Examples of Higher Order Functions)
# Decorators wraps other functions and enhance their behaviour
# Decorators have their own syntax, using '@' (syntatic sugar)

# Now we will see how to implement Decorators without @
# We can save the decorated functions with the same name or with different names
def be_polite(fn):
    def wrapper():
        print('What a Pleasure to meet you!')
        fn()
        print('Have a nice day!')
    return wrapper


def greet():
    print('My name is Elemento!')


def rage():
    print('I hate you!')


polite_greet = be_polite(greet)
polite_greet()
rage = be_polite(rage)
rage()


# Now we will see how to implement Decorators using @
# We can see that @ decorate our function and save it with the same name itself
@be_polite
def love():
    print('I love you!')


love()
