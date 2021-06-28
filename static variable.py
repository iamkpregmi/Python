class Test:
    a=10    #static variable 1st method
    def __init__(self):
        self.x=1    #instance variable
        Test.y=45   #static variable 2nd method

    def f1(self):   #instance member function
        self.x=2    #instance variable
        Test.c=30   #static variable 3rd method

    @staticmethod
    def f2(m,n):    #static methond function
        Test.d=40   #static variable 4th methond

    @classmethod
    def f3(cls):
        cls.e=50    #static variable 5th method
        Test.f=60   #static variable

Test.g=70 #static variable 6th method
