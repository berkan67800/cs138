# PLEASE see the README.md file

def myAdd( a,  b ): 
  return a + b  # DONE: returns the sum of a and b

def mySub( a,  b): 
  return a - b # returns the subtraction of a and b
  
def myMul( a,  b): 
  return a * b # returns the multiplication of a and b

def myDiv( a,  b): 
  if(b == 0): # if the divider is 0, it prints '(ERROR)' and returns 0
    print ("(ERROR)")
    return 0
  return a / b # returns the division of a and b

def myEquation( a,  b ) : 
  return myAdd(myDiv(myMul(a,b),mySub(b,a)),5) #returns the result of: (  (a *  b) / ( b - a)  ) + 5 



#######################################################################
# MAIN section starts below here (define your functions above here)
########################################################################



# DONE: prompt the use for 2 floating point values
x = float( input( "Please enter a floating point value for x: "))
y = float( input( "Please enter a floating point value for y: "))

# TODO: print the result of x-y  (use your mySub() function)
# TODO: print the result of x*y  (use your myMul() function)
# TODO: print the result of x/y  (use your myDiv() function)
# TODO: print the result of calling your myEquation( ) with x and y

print(  x, "+", y, "=", myAdd( x, y ) ) # DONE: print the result of x+y  (this one is done for you)
print(  x, "-", y, "=", mySub( x, y ) )
print(  x, "*", y, "=", myMul( x, y ) )
print(  x, "/", y, "=", myDiv( x, y ) )
print(  "My equation =","(  (a *  b) / ( b - a)  ) + 5 ", "=", myEquation( x, y ) )