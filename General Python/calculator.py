def add(n11,n15):
   return n11 + n15

def subtract(n11,n15):
   return n11 - n15
    
def multiply(n11,n15):
   return n11 * n15

def divide(n11,n15):
   return n11 / n15

def percent(n11,n15):
    return n11 / n15 * 100

def exp(n11,n15):
    return n11 ** n15
                                        
def calculator1(n11,n15,func):
   return func(n11,n15)
    
print(calculator1(15,1.422,exp))
