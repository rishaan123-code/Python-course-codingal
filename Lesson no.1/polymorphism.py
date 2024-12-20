class cat:
    def __init__(self,name,age):
        self.name=name  
        self.age=age
    def sound(self):
        print("meow")
    def info(self):
        print("My name is ",self.name,"my age is ",self.age,"I am a cat")
        
class dog:
    def __init__(self,name,age):
        self.name=name  
        self.age=age
    def sound(self): 
        print("bhow")
    def info(self):
        print("My name is ",self.name,"my age is ",self.age,"I am a dog")
ob1=cat("billy",7)
ob2=dog("bruce",9)
ob1.sound()
ob2.sound()

            
    