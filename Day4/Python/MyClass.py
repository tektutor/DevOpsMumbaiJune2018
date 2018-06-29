#!/usr/bin/python

class MyClass:

    def __init__(this):
        print ("This is called as constructor")
        print ("You can initialize member variables here automagically/n")
        this.x = 100
        this.y = 200

    def setValues(this, val1, val2):
        this.x = val1
        this.y = val2

    def printValues(this):
        print ("Value of x is ", this.x )
        print ("Value of y is ", this.y )
        print ("\n")
    
if __name__ == "__main__":
   print("Constructing object 1")
   obj1 = MyClass()

   print("Constructing object 2")
   obj2 = MyClass()

   print ("Before calling setValues function")
   print ("Object 1 values")
   obj1.printValues()

   print ("Object 2 values")
   obj2.printValues()

   print ("After calling setValues function")

   obj1.setValues(500,600)
   obj2.setValues(10, 20)

   print ("Object 1 values")
   obj1.printValues()

   print ("Object 2 values")
   obj2.printValues()

  
