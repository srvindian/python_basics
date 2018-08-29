class Emp:
    'my employee class'
    count=0      #class/static variable
    @staticmethod
    def myStaticMethod():
        print('Here is my static Method.....')
    def __init__(selfie,name,age,salary=10000):
        if salary<10000:
            msg="8000 Rs. is too low salary..."
            raise Exception(msg)
        selfie.e_name=name
        selfie.age=age
        selfie.salary=salary
        Emp.count+=1
    def dispEmp(self):
        print('\nName:{0}\nage:{1}\nsalary:{2}'.format\
              (self.e_name,self.age,self.salary))
        Emp.count+=2000
    def dispCount(selfish):
        s=''
        if Emp.count>1:
            s='s'
        print('Total number of employee%s=%d'%(s,Emp.count))
    def __del__(s_elf):
        print('destructor is called...and employee%d is deleted'%s_elf.count)
if __name__=="__main__":
    e1=Emp(age=24,name='Sourav',salary=80000)
    e1.dispEmp()
    e1.dispCount()
    e2=Emp(age=24,name='Levina',salary=67000)
    e2.dispEmp()
    Emp.count=1000
    e2.dispCount()
    del e1
    Emp.myStaticMethod()
