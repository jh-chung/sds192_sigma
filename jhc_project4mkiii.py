"""
Application: Project 4 mki, Small Functions
Name: Jay-Ho Chung
Start Date: 12:43 PM, March, 14, 2018
"""

# Apparently the number 6 is great. It is also Baker Mayfield's number.

# Function 1. 
# Our first function takes two arguments f and s. (First and second number)

def love6(f , s):
    if  f == 6 or s == 6:
        return True # return always breaks out of the code
        
    elif abs(f+s) == 6:
        return True
        
    elif abs(f-s) == 6:
        return True
    
    else:
        return False

    # Calling on the function with the arguments
print("First function results")
print(love6(6 , 4))
print(love6(4 , 5))
print(love6(1 , 5))
print(love6(-2 , 4))
print("") #I want to separate first function results


#Function 2.


# Takes an input, needs to be near a multiple of 10.


# Remember that % is the modulus, finds remainder

def near_ten(t):

    r_mndr = t % 10 # Finding us remainder

    if (r_mndr) <= 2 or 10 - r_mndr <= 2: # Need this condition 10 - remainder needs to be clsoe to a *multiple* of ten
        return True

    else:
        return False
print("Second function results")
print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
print("")

# Function 3.


def max_of_three(f_st = 0 , s_nd = 0 , t_rd = 0): #Defining as 0 first.
    while True:
        try:
            if (f_st == 0 and s_nd == 0 and t_rd == 0): # No comparison if all are 0 
                o_ne = int(input("Choose your first number. "))
                t_wo = int(input("Choose your second number. "))
                t_re = int(input("Choose your third number. "))
            else:
                o_ne = f_st
                t_wo = s_nd
                t_re = t_rd
            if o_ne >= (s_nd and t_re):
                return o_ne
            elif s_nd >= (o_ne and t_re):
                return s_nd
            elif t_re >= (o_ne and s_nd):
                return t_re
        except:
            print("Only numbers. ")
            continue



print(max_of_three(1,0,2)) # Calling it. Really, I forgot to do this
print(max_of_three(-1 , -2 , 0))



# Function 4.
print("")
print("")
#Ask the inputs

def near_ten_of_three(a , b, c):
    while True:
        out_put = max_of_three(a , b , c)
        if out_put < 0:
            sol_n = out_put * -1 # Making output +
            re_zult = near_ten(sol_n)
            return re_zult
        else:
            sol_n = out_put
            re_zult = near_ten(sol_n)
            return re_zult

    
print(near_ten_of_three(1 , 2 , 9)) # Just calling on it to put in our inputs
print(near_ten_of_three(1 , 3 , 2))
print("")
print("")
print("")






# Function 5.

# Need something like this

def wind_chill():

    while True:
        try:
            #General equation which needs to accept floats
            T = float(input("Temperature: ")) #By writing float() over all of this, our functions also accepts float values. Could write it a different way too.
            #Temperature is degrees
            V = float(input("Wind speed: ")) #Wind speed in MPH
            W = 35.74 + 0.6215*(int(T)) - 35.75*((int(V))**0.16) + 0.4275*T*((int(V))**0.16)
            return W
                    
        except ValueError:
            print("Error, your mu needs to be a float or a number.")
        
                
    print("Temperature (Farenheit): " + str(T))
    print("Wind speed (MPH): " + str(V))
    print("Your Wind Chill (Farenheit): " + str(W)) #Printing the wind chill temperature values that the user inputs.
        



print(wind_chill())
print("")
print("")

#Function 6 (Credit Card).

"""
Leading 6 digits are the IIN, next 9 are the individual account id number. the last digit is the check digit.
"""

def credit_checker(c_n):
    l = len(str(c_n))
    print(l)
    c_n = int(c_n)
    sum_n = 0
        
    if l == 16:
        print(c_n)
        for i in range(16):
            digit_n = c_n % 10
            c_n = c_n - digit_n # Takes out the 16th digit
            c_n = c_n / 10 # Gives us 15 digit
            
            if i % 2 == 1: # Odds
                digit_n = digit_n * 2
                
                if digit_n > 9:
                    digit_n = digit_n - 9
                    sum_n = sum_n + digit_n # Taking the sum when the digits are greater than 9
                
                else:
                    sum_n = sum_n + digit_n # Taking the sum when the digits are not greater than 9

            if i % 2 == 0:
                sum_n = sum_n + digit_n 

        if sum_n % 10 == 0: # Last condition, if modules equals 0
            return True
        else:
            return False
    else:
        return False

print(credit_checker(7992739871))

print(credit_checker(5105105105105100))

print("")

print("")

print("")

def chk_cmptr(c_n):
    l = len(str(c_n))
    print(l)
    c_n = int(c_n)
    sum_n = 0

    if l == 15: # We are putting in a 15 digit number
        print(c_n)
        for i in range(15):
            digit_n = c_n % 10
            c_n = c_n - digit_n # Takes out the 16th digit
            c_n = c_n / 10 # Gives us 15 digit, removing the digit
    
            if i % 2 == 0:
                digit_n = digit_n * 2 # Have to multiply by 2 no matter what

                if digit_n > 9:  # In the case taht our digit is greater than 9
                    digit_n = digit_n - 9 # Need to subtract by 9
                sum_n  = sum_n + digit_n

            else:
                sum_n = sum_n + digit_n

        sum_n = sum_n * 9 # Multiplying the sum by 9 
        check_digit = sum_n % 10
        return check_digit
        
    else:
        return False


print(chk_cmptr(510510510510510))
print(chk_cmptr(488770445518583))
print(chk_cmptr(37976208860029))
print(chk_cmptr(353912446217849))
