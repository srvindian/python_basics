class B():
    def myMethod(self):
        print('This is child class method')
class A:
    def myMethod(self):
        print('This is parent class method')
class C(B,A):
    pass
if __name__=="__main__":
    a=A();a.myMethod()
    b=B();b.myMethod()
    c=C();c.myMethod()
