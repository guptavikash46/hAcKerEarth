def LeapYear(num):

 if num%4==0 and num%100!=0 or num%400==0:
  print(num, 'is leap year.')
 else:
  print(num,'is not a leap year')

""" Second function """  

def CheckCasing(charac):

 checkChar = charac.upper();

 if charac==checkChar:
  print(charac,'is a capital letter')
 else:
  print(charac,'is a non-capital letter')
  
  """Third function"""
  
 
def printFibo(num):
 
  a,b =0,1
  while a<=num:
    print(a, end=" ")
    a,b = b,a+b
	

   