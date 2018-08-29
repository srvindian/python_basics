class A:
    def __init__(self,name=""):
        self.name=name
    def fun(self):
        print('I am a parent value received from child:',self.name)
        #raise NotImplementedError("Must be implemented in subclass")

class B(A):
    def __init__(self,name="Sourav"):
        self.name=name
        super().fun()
    def fun(self):
        print('I am a child with original value:',self.name)
    
if __name__=="__main__":
    b=B("India")
    b.fun()
    
