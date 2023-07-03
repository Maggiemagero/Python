class fruits:
    def __init__(self,type,color,price,shape):
        self.fruittype=type
        self.fruitcolor=color
        self.fruitprice=price
        self.fruitshape=shape

    def display(self):
       print( self.fruittype,self.fruitcolor,self.fruitprice,self.fruitshape)

myobj=fruits('Banana','Green',20,'curved')
myobj.display()
myobj=fruits('Mango','green',30,'oval')
myobj.display()
#class people
#name,age,gender
