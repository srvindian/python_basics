class A:
    name='A parent class'
    @classmethod
    def foo(ref):
        print('hello %s'%ref.name)
class B(A):
    name='B child class of A'
    pass
class C(A):
    name='C child class of A'
    @classmethod
    def foo(ref):
        print('hello %s'%ref.name)
if __name__=="__main__":
    A.foo()
    B.foo()
    C.foo()
