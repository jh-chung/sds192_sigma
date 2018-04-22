"""
    Application: Project 1
    Start: 1.31.2018, start at 1:42 PM EST
    Written: Jay-Ho Chung
    Purpose: Maximizing Avery's time to grind.
"""

print("So before we start, we need to understand a few requirements for this project.")
#So before we start, we need to understand a few requirements for this project.
print("The first requirement is to have (at least) 3 variables with string values, 2 variables with integer values, and 1 with a floating point value.")
#The first requirement is to have (at least) 3 variables with string values, 2 variables with integer values, and 1 with a floating point value.
#So let's first create some variables. Before that, we need to understand what kind of program we want to make.
print("The program we should make is how much your beasting and feasting ratio is.")
#The program we should make is how much you study in a day. Maybe we will modify it to give more useless responses.
#Here are the variables.
#The first variables will be our float.


B = 0.5 #This is how long Avery is in school for. Note that this is our float.
#Next, let's go for our integers.
S = 12 #This is how long Avery sleeps for.
P = 3 #This is how long Avery practices for.
D = 4 #This is how long Avery drives for.
G = 24-(B+S+P) #This is how much free time Avery has.
N = "Avery" #Let's start using this.

print(str(B)) #Repetition operator here.
print(str(S))
print(str(P))
print(str(D))
print(str(G))
print(str(N)*3) #Printing our variables once

print("") #Printing our values and putting a blank line.

print(B, S , P , D , G , N) #Printing our variables in a comma.
print("")


#Changing our variables from here.
B = 6.5 #This is how long Avery is in school for. Note that this is our float.
#Next, let's go for our integers.
S = 7 #This is how long Avery sleeps for.
P = 2 #This is how long Avery practices for.
D = 1 #This is how long Avery drives for.
G = 24-(B+S+P) #This is how much free time Avery has in a day.
N = "Avery" #Let's start using this.

print(str(B))
print(str(S))
print(str(P))
print(str(D))
print(str(G))
print(str(N)) #Printing our (new) variables once
print("") #Printing our values and putting a blank line.


def useless_stuff(): #Time to concatenate.
    print(str(N) + " is in school for " + str(B) + " hours.")
    print(str(N) + " sleeps for " + str(S) + " hours.")
    print(str(N) + " swims for " + str(P) + " hours.")
    print(str(N) + " has " + str(G) + " hours of free time in a day.")
    print("") #Meeting the requirement of blank line again
for i in range(5): #This is the looping my code 5 times. 
    useless_stuff()

W=G*7 #The number of hours Avery has to do other things in his life. Our first mathematical function to find how much time Avery has in a week. 
#Note to Ms. Keough, you told me that most functions for Area, Volume, etc. were multiplication: I can, therfore, just include multiplication in 3 equations.
def hours_n_hasinweek(): #My concatenation.
    print("How much free time does Avery have in a week?")
    print("The answer is " + str(W))
    print(str(N) + " has a maximum of " +  str(W) + " hours to grind in a day.")
    print("") #Blank line

for i in range(10): #Just making another loop.
    hours_n_hasinweek()
print("")

#We first need to start using sep function. After that, create more equations.
print(B, S, P, D, G, N, sep=', ')

#Now we have to use our end function. We'll put something at the end.
print(B, S, P, D, G, N, sep=', ', end=': Here are my (new) variables. \n')

#Back to our second multiplication function.
Y=W*52 #Time Avery has in a year
H=Y*4 #Free time Avery has in all of high school
L=Y*70 #Time "will" have in his life, assuming he followed roughly this schedule since 10 to age 80. Very inaccurate.

#Let's just print these.
def potential_time():
    print("How much time has Avery had free in a day?")
    print(str(G)+" hours")
    print("How much time does Avery have in a year?")
    print(str(Y) +" hours")
    print("How much free time has Avery had in high school?")
    print(str(H)+ " hours")
    print("How much free time has Avery had in his life?")
    print(str(L)+ " hours")

#Loop again, it's going to loop for a while.
for i in range(10):
    potential_time()
