# SUMMARY

- At the top of your main.py file, implement functions for the 4 basic operations on a standard calculator (subtraction, addition, division, multiplication) 
- Implement a 5th function that  utilizes all of the above functions to compute the result of the equation shown below:

               (  (a *  b) / ( b - a)  ) + 5    # YOU MUST USE YOUR FUNCTIONS FOR THIS EQUATION (use floating point division)

- In the main section below your functions, prompt the user for 2 floating point values
- Use those values when you "call"  each of your 5 functions.  
- Print out the return value from each function call


# **STEPS**

- Step 1: Review myAdd(a, b) which has already been written for you at the top of main.py
- Step 2: Implement mySub( a, b ) below myAdd( a, b )
- Step 3: Implement myMul( a, b) below mySub( a, b )
- Step 4: Implement myDiv( a, b) below myMul( a, b )
  - For myDiv, you must test to be sure the 2nd argument (b) is not zero;
  - if the second argument of the division function is zero, then your myDiv() function must
    - print "(ERROR)" in capitals with parenthesis,
    - and return a value of Zero (0)
- Step 5: Implement the function myEquation( a , b) which must:
  - return the result of this equation: (  (a *  b) / ( b - a)  ) + 5
  - you must use ONLY myAdd, mySub, myMul, and myDivto compute the equation
  - you may not use +, -, *, or / in your solution

# **REQUIREMENTS**

- Use the function prototypes provided as the basis for the functions you implement
- Implement your functions ABOVE the main section
- Call each of your functions one time from within main section, using the same x and y values.
- Your **myEquation()** function described above MUST utilize your functions.  
- Your **myEquation()** function CANNOT use Python operators at all (no use of +, -, /, or * )
- You must use floating point division for your **myDiv()** function


**HINTS**

- Be sure to print "(ERROR)" if the 2nd argument of your division function is zero
- Be sure to return zero if the 2nd argument of your division function is zero
- For myEquation(): You can nest function calls within other function calls like this:

```
        myAdd( myMul( a, a ),   myDiv( b, b ) ) # same as ( a*a ) + ( b/b ) 
```

- From main(), you can print out the return value of any function (assuming it has one) like this:

```
       print( a, "+", b, "=", myAdd( a, b ) )  # x==5 and y==1, prints "5+1=6"
```

# SUBMISSION

Test your results using the examples provided below. Submit your assignment via this repl via canvas when you are satisfied with your results.



# SAMPLE OUTPUT
```
Example 1

Enter a value for x:  5
Enter a value for y:  2
5+2=7
5-2=3
5*2=10
5/2=2.5
My equation = 1.66667

Example 2

Enter a value for x:  10
Enter a value for y:  3
10+3=13
10-3=7
10*3=30
10/3=3.333
My equation = 0.714286  

Example 3

Enter a value for x:  8
Enter a value for y:  -2
8+-2=6
8--2=10
8*-2=-16
8/-2=-4
My equation = 6.6

Example 4

Enter a value for x:  9 
Enter a value for y:  9
9+9=18
9-9=0
9*9=81
9/9=1
My equation = (DIVISION ERROR)5
```

# CONCEPTS COVERED

- function definitions
- calling functions from other functions
- nested function calls
- passing arguments to functions
- function return values, including None
- input
- print
- variable scope


