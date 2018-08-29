class String:
    def __init__(self,val=None):
        self.val=val
    def __mod__(self,otherStr):
        return self.val+otherStr.val
if __name__=="__main__":
    s1=String('Sourav')
    s2=String('Mondal')
    print(s1%s2)
    
