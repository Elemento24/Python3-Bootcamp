class A:
    def do_something(self):
        print('Method defined in A!')


class B(A):
    def do_something(self):
        print('Method defined in B!')
        super().do_something()


class C(A):
    def do_something(self):
        print('Method defined in C!')
        super().do_something()


class D(B, C):
    def do_something(self):
        print('Method defined in D!')
        super().do_something()


thing = D()
thing.do_something()

# When we have Multiple Inheritance Classes, which may have other Inheritance Classes...
# ... in that case, we take help form M.R.O. (Method Resolution Order)
# There are 3 methods to find out the MRO of a class

# print(D.__mro__)
# print(D.mro())
# help(D)

# The MRO in this case for D is D->B->C->A->Object
