"""
    Application: Game mk.I
    Author: Jay-Ho Chung
    Start: Monday, 2/12, 1:16 PM EST
    Class: Hnrs Comp Sci II
"""

# So, what kind of game do I want to create? I was thinking about a random birth generator. A series of randomness that determines your life based on your birth. The game of life, basically

# There are some philosophical ideas behind this really. I, personally, just wonder how much of our lives is predetermined. I am not going to provide an answer to that question, but I want to design a game that reflects the idea of predetermined factors or important factors that you cannot necessarily control.
# In general, the idea is to give the player the illusion that the game is not somehow rigged, yet it is. No matter what the player does, they will probably lose.
# Put simply, I just wanted a game that was unfair. 

print("Let's play a game.")
print("Make sure to choose wisely. The choices you make will affect what happens throughout the course of the whole game.") # This is kind of a lie; the factors are somewhat predetermined because of the random number generator
a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
# Defining and using constants
print("Commecning count down. Ground control to Major Tom. ") # Sorry for the Bowie reference
print("Here is your count down: " + f)
print("Here is your count down: " + e)
print("Here is your count down: " + d)
print("Here is your count down: " + c)
print("Here is your count down: " + b)
print("Here is your count down: " + a)

from random import *
R = randint(1, 1000000000000000000000000) # This chooses a random integer


def white_rabbit(): 
    user_name = input("Welcome, give your name: ")
    user_age = input("Your age: ")
    print("Your Social Security number: ")
    print("Don't give people your Social Security Number, " + user_name + " of " + user_age + " years of age.")
    b_n = input("Choose a number between 1 and 100, but choose carefully: ") #You don't have to follow these rules, especially when my code is not supposed to break. Another note, I'm testing if people will really confine themselves within 1 and 100.
    print("You chose " + str(b_n) + ".")
    input("Are you sure that " + str(b_n) + " is the number that you want? ")
    print("That's a small number.") #Hint if they play again
    print("Too late now....") # Another warning
    return b_n

for i in range(1):
    L = white_rabbit()

while True:
        try:
            b_n = int(L)
            break
        except:
            print("Error. Looping again")
            print("Type in numbers! Numbers!")
            for i in range(1):
                L = white_rabbit()

# The integer values you have chosen affect your player, which will again depend on a location. 

if  int(b_n) > int(R):

    if int(b_n) >= int(R*R) or int(b_n) > 3*R:
        print("You are Quinn.")
        player_name = "Quinn"
        
    else:
        player_name = "JD"

elif int(b_n) == int(R) or int(b_n) == 7:
    print("You are off to a great start. You are Jay-Ho.")
    print("Let's begin.")

else:
    if int(b_n) <= int(R)/2 and int(R) >= 0:
        print("You are Brett.")
        player_name = "Brett"
    else:
        print("You are Nick.")
        player_name = "Nick"

print("Now that you have a player, time to begin.")
print("Let's see where you end up.")
# Time to set a location.
L = randint(1 , 200) # Random number for location.

l_s = input("Choose a number, again, from 1 to 100: ") # l_s or location setter. Once again, they need to think out of the box.
print("You chose " + str(l_s) + ".")
input("Are you sure that " + str(b_n) + " is the number that you want? ")
print("That's a small number, again.") #Hint if they play again
print("Well, too late again...") # Another warning

if player_name == "Quinn":
    if L < int(l_s):
        if L < 3*int(l_s):
            print("You are going to the squash court.")
            l_1 = "Squash Court" 
        elif L < 2*int(l_s ) or L == int(l_s):
            print("You are going to the parking lot.")
            l_1 = "Parking Lot"

    else:
        if int(l_s) == int(0):
            print("You are going to the swimming pool.") # Switch it up. For Quinn, you have to get 0 if you want to go the pool.
            l_1 = "Swimming Pool" 

        else:
            print("You are going to school.")
            l_1 = "School"
            
if player_name == "Nick":
    if L < 2*int(l_s ) or L == int(l_s):
        print("You are going to school.")
        l_1 = "School"

    elif  int(l_s) == int(0):
        print("You are going to the parking lot.")
        l_1 = "Parking Lot"

    elif int(l_s) < int(0):
        print("You are going to the squash court") # Disadvantage for Nick with negative numbers.
        l_1 = "Squash Court"

    else:
        print("You are going to swimming pool.") # The swimming pool is Nick's strength. I don't really want him to get to the pool, which is why we have the L*2 condition.
        l_1 = "Swimming Pool" 

if player_name == "JD":

    if L < 2*int(l_s ) or L == int(l_s):
        print("You are going to swimming pool.") 
        l_1 = "Swimming Pool" 

    elif  int(l_s) == int(0):
        print("You are going to the squash court.") # This time you have to choose 0 for JD. In the case that someone plays again, I don't want them to just always put in larger numbers.
        l_1 = "Squash Court"

    elif int(l_s) < int(0):
        printi("You are going to school.")
        l_1 = "School"

    else:
        print("You are going to parking lot.") 
        l_1 = "Parking Lot" 

if player_name == "Brett":

    if L < 2*int(l_s ) or L == int(l_s):
         print("You are going to the parking lot.")
         l_1 = "Parking Lot"

    elif  int(l_s) == int(0):
        print("You are going to school.") 
        l_1 = "School" 

    elif int(l_s) < int(0):
        print("You are going to the squash court")
        l_1 = "Squash Court"

    else:
        print("You are going to swimming pool.")
        l_1 = "Swimming Pool" 


# Right now, we have four different players and four different locations. Creating different scenarios for all of them. 



# Starting at the games locations, this is if JD ended up in the courts. Best scenario for him

if player_name == "JD":
    if l_1 == "Squash Court":
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(7)
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho moves in the first quarter and volleys.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(12)
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has lost the match.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(14)
    # Now we send JD to the pool.
            print("You are now in the pool " + str(player_name) + ".") # JD will go to the pool next, no matter what.
            print("You will be swimming against Quinn in the 50 free.")
        s_stroke = input("Choose a number for the strength of the strokes: ") # Asking for a strength of swimming stroke.
        if int(s_stroke) > 1000:
            print("You had too many strokes without enough leg power. You lose")
            p_ts2 = int(0)
        elif int(s_stroke) >= 100:
            print("Nice tempo! Unfortunately, Quinn is too fast in the 50.")
            p_ts2 = int(0)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts2 = int(0)
    # Now we send JD to the school.
        print("Well, next location. You received " + str(p_ts2) + " point for the last event.")
        print("Moving on to the school.") 
        print("Oh no! You have a test in Precalc! It's on derivatives.")
        s_test = input("Quick! Choose a number. Don't make it too high or too low. ")
        if int(s_test) > int(0) and int(s_test) < int(100):
            print("You had did somewhat well. At least you didn't choose 0.")
            print("That's why you don't grind at home, JD.")
            p_ts3 = int(85) 
        elif int(s_test) == int(0):
            print("She would never give a derivative that's just 0.")
            print("That's why you don't grind at home, JD.") # Meta joke about JD "grinding"/working hard at home for school.
            p_ts3 = int(0)
        else:
            print("No derivative would be that high. Keefe dropped you.")
            print("That's why you don't grind at home, JD.")
            p_ts3 = int(0)
        print("Next location, the parking lot. You received " + str(p_ts3) + " points at the school.")
    # JD's final location: the parking lot if he starts at the court.
        print("Here's your final location: the parking lot.")
        print("You have to drive against Brett.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Want to do the opposite of being reasonable in this case. 
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won with a bicycle, but you moved your legs quickly enough.")
            print("Unfortunately, your legs are broken.")
            p_ts4 = int(40)
        else:
            print("You have lost to Brett, His whip was not mach for you.")
            p_ts4 = int(-30)
    total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
    print("These are your total points: " + str(total_points))
    
# Next scenarion if JD is the player and starts in the pool.
    if l_1 == "Swimming Pool":
            print("You are now in the pool " + str(player_name) + ".") # JD will go to the pool next, no matter what.
            print("You will be swimming against Quinn in the 50 free.")
            s_stroke = input("Choose a number for the strength of the stroke, but choose a reasonable number: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. A smart swimmer would not, however, that you want to hit about 100 strokes in the 50 free. 
            if int(s_stroke) > 1000:
                print("You had too many strokes without enough leg power. You lose")
                p_ts2 = int(-10)
            elif int(s_stroke) >= 100:
                print("Nice tempo! Unfortunately, Quinn is too fast in the 50.")
                p_ts2 = int(10)
            else:
                print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.") 
                p_ts2 = int(-20)
            print("Well, next location. You received " + str(p_ts2) + " point for the last event.")
            print("Moving on to the school.") # Pool, school
            print("Oh no! You have a test in Precalc! It's on derivatives.")
            s_test = input("Quick! Choose a number. Don't make it too high or too low. ")
            if int(s_test) > int(0) and int(s_test) < int(100):
                print("You had did somewhat well. At least you didn't choose 0.")
                print("That's why you don't grind at home, JD.")
                p_ts3 = int(85) 
            elif int(s_test) == int(0):
                print("Keefe would never give you an easy derivative equal to.")
                print("That's why you don't grind at home, JD.") # Meta joke about JD "grinding"/working hard at home for school.
                p_ts3 = int(0)
            else:
                print("No derivative would be that high. Keefe dropped you.")
                print("That's why you don't grind at home, JD.") 
                p_ts3 = int(0)
            print("Next location, the squash court. You received " + str(p_ts3) + " points at the school.")
            print("You will be playing Jay-Ho.")
            print("Jay-Ho wins the racket spin. He will serve first.")
            print("Jay-Ho hits you with a filthy serve.")
            print("You need to return the serve.")
            s_squash = input("Choose a number for the strength of the return. Return it well, maybe a bit lower: ") # Asking for a strength on the return of the serve. Telling them to hit it lower than 100.
            if int(s_squash) > 1000:
                print("You returned a lob shot. Way too high.")
                print("You've lost the match.")
                p_ts1 = int(7)
            elif int(s_squash) >= 100:
                print("You've hit a volley.")
                print("Jay-Ho moves in the first quarter and volleys.") # Real squash tips.
                print("You've lost the match. Good effort.")
                p_ts1 = int(12)
            else:
                print("You've hit a dropshot!")
                print("Jay-Ho has lost the match.")
                print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
                p_ts1 = int(14)
                print("At the end, in the courts, you won " + str(p_tsl) + " points.")

            print("Here's your final location: the parking lot.")
            print("You have to drive against Brett.")
            s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Want to do the opposite of being reasonable in this case. 
            from random import *
            s_v = randint(1, 100)
            if int(s_v) < int(s_vehicle):
                print("You won with a bicycle, but you moved your legs quickly enough.")
                print("Unfortunately, your legs are broken.")
                p_ts4 = int(40)
            else:
                print("You have lost to Brett. You were no match for his beast of a car.")
                p_ts4 = int(-30)
    total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
    print("These are your total points: " + str(total_points))

# Scenario 3: JD starts at the school.
    if l_1 == "School":
            print("You are now in the school,  " + str(player_name) + ".") # JD will go to the pool next, no matter what.
            print("Oh no! You have a test in Precalc! It's on derivatives.")
            s_test = input("Quick! Choose a number. Don't make it too high or too low. ")
            if int(s_test) > int(0) and int(s_test) < int(100):
                print("You had did somewhat well. At least you didn't choose 0.")
                print("That's why you don't grind at home, JD.")
                p_ts3 = int(85) 
            elif int(s_test) == int(0):
                print("Keefe would never give you an easy derivative equal to.")
                print("That's why you don't grind at home, JD.") # Meta joke about JD "grinding"/working hard at home for school.
                p_ts3 = int(0)
            else:
                print("No derivative would be that high. Keefe dropped you.")
                print("That's why you don't grind at home, JD.") 
                p_ts3 = int(0)
            print("Next location, the parking lot. You received " + str(p_ts3) + " points at the school.")
    # Parking lot
            print("You are in the parking lot.")
            print("You have to drive against Brett.")
            s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Want to do the opposite of being reasonable in this case. 
            from random import *
            s_v = randint(1, 100)
            if int(s_v) < int(s_vehicle):
                print("You won with a bicycle, but you moved your legs quickly enough.")
                print("Unfortunately, your legs are broken.")
                p_ts4 = int(40)
            else:
                print("You have lost to Brett. You were no match for his beast of a car.")
                p_ts4 = int(-30)
    #Swimming Pool
            print("Moving on to the swimming pool.")
            print("Swimming the 100 Back against Nick.") # Switching from Quinn to Nick.
            s_stroke = input("Choose a number for the strength of the stroke, but choose a reasonable number: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. A smart swimmer would not, however, that you want to hit about 100 strokes in the 50 free.
            if int(s_stroke) > 1000: # Backstroke, you want as many people
                print("You had an impressive number many strokes without enough leg power. You lose but did well.")
                p_ts2 = int(30)
            elif int(s_stroke) >= 100:
                print("Nice tempo! You could have been faster. Unfortunately, Nick is too fast in the 100.") # Making it clear how to win next time.
                p_ts2 = int(10)
            else:
                print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
            print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
# Courts
            print("Moving on to the final location: the courts.")
            print("You will be playing Jay-Ho.")
            print("Jay-Ho wins the racket spin. He will serve first.")
            print("Jay-Ho hits you with a filthy serve.")
            print("You need to return the serve.")
            s_squash = input("Choose a number for the strength of the return: ") # Asking for a strength on the return of the serve.
            if int(s_squash) > 1000:
                print("You returned a lob shot. Way too high.")
                print("You've lost the match.")
                p_ts1 = int(7)
            elif int(s_squash) >= 100:
                print("You've hit a volley.")
                print("Jay-Ho moves in the first quarter and volleys.") # Real squash tips.
                print("You've lost the match. Good effort.")
                p_ts1 = int(12)
            else:
                print("You've hit a dropshot!")
                print("Jay-Ho has lost the match.")
                print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
                p_ts1 = int(14)            
            total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
            print("These are your total points: " + str(total_points))

# JD Scenario 4, starting at the parking lot.
    if l_1 == "Parking Lot":
        print("Next location, the parking lot. You received " + str(p_ts3) + " points at the school.")
        print("You are in the parking lot.")
        print("You have to drive against Brett.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Want to do the opposite of being reasonable in this case.
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won with a bicycle, but you moved your legs quickly enough.")
            print("Unfortunately, your legs are broken.")
            p_ts4 = int(40)
        else:
            print("You have lost to Brett. You were no match for his beast of a car.")
            p_ts4 = int(-30)
        print("You received " + str(p_ts4) + " points after racing with Brett.")
# Next, JD heads to the school.
        print("Well, next location. You received " + str(p_ts2) + " point for the last event.")
        print("Moving on to the school.") 
        print("Oh no! You have a test in Precalc! It's on derivatives.")
        s_test = input("Quick! Choose a number. Don't make it too high or too low. ")
        if int(s_test) > int(0) and int(s_test) < int(100):
            print("You had did somewhat well. At least you didn't choose 0.")
            print("That's why you don't grind at home, JD.")
            p_ts3 = int(85) 
        elif int(s_test) == int(0):
            print("Keefe would never give you an easy derivative equal to.")
            print("That's why you don't grind at home, JD.") # Meta joke about JD "grinding"/working hard at home for school.
            p_ts3 = int(0)
        else:
            print("No derivative would be that high. Keefe dropped you.")
            print("That's why you don't grind at home, JD.")
            p_ts3 = int(0)
        print("Next location, the parking lot. You received " + str(p_ts3) + " points at the school.")
# Courts
        print("Moving on to the final location: the courts.")
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(7)
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho moves in the first quarter and volleys.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(12)
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has lost the match.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(14)
# Pool
            print("Moving on to the swimming pool.")
            print("Swimming the 100 Back against Nick.") # Switching from Quinn to Nick.
            s_stroke = input("Choose a number for the strength of the stroke, but choose a reasonable number: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. A smart swimmer would not, however, that you want to hit about 100 strokes in the 50 free.
            if int(s_stroke) > 1000: # Backstroke, you want as many people
                print("You had an impressive number many strokes without enough leg power. You lose but did well.")
                p_ts2 = int(30)
            elif int(s_stroke) >= 100:
                print("Nice tempo! You could have been faster. Unfortunately, Nick is too fast in the 100.") # Making it clear how to win next time.
                p_ts2 = int(10)
            else:
                print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
            print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")


# If your player is Brett.
# Running through the first scenario.
elif player_name == "Brett":
# First 4 scenarios, if Brett starts in the parking lot (This is the best scenario for Brett.)
    if l_1 == "Parking Lot":
        print("You are in the parking lot.")
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Brett will always win.
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough.")
            print("Unfortunately, his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your car.")
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        # Now the swimming pool.
        print("Moving on to the swimming pool.")
        print("Swimming the 100 Back against Nick.") # Switching from Quinn to Nick.
        s_stroke = input("Choose a number for the strength of the stroke, but choose a reasonable number: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. A smart swimmer would not, however, that you want to hit about 100 strokes in the 50 free.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well.")
            p_ts2 = int(30)
        elif int(s_stroke) >= 100:
            print("Nice tempo! You could have been faster. Unfortunately, Nick is too fast in the 100.") # Making it clear how to win next time.
            p_ts2 = int(10)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
        
        # Next, Brett heads to the school.
        print("Well, next location. You received " + str(p_ts2) + " point for the last event.")
        print("Moving on to the school.") 
        print("Oh no! You have a project in Ms. Keough's class! You have to make a game.")
        s_test = input("Quick! Choose a number of hours. Don't make it too high or too low. ")
        if int(s_test) > int(0) and int(s_test) < int(100):
            print("You had did somewhat well. At least you didn't choose 0.")
            p_ts3 = int(90) 
        elif int(s_test) == int(0):
            print("Not enough hours spent on the project.")
            print("But Brett never grinds at home and Miss Keough is very generous.") 
            p_ts3 = int(10)
        else:
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points in Keough's.")
        # Courts
        print("Moving on to the final location: the courts.")
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(3) # Brett is not too great at squash.s
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(7)
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has fectched it.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(0)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))


# Second Brett Scenario: Starting at school
    if l_1 == "School":
        print("Oh no! You have a project in Ms. Keough's class! You have to make a game.")
        s_test = input("Quick! Choose a number of hours. Don't make it too high or too low. ")
        if int(s_test) > int(0) and int(s_test) < int(100):
            print("You had did somewhat well. At least you didn't choose 0.")
            print("That's why you don't grind at home, JD.")
            p_ts3 = int(90) 
        elif int(s_test) == int(0):
            print("Not enough hours spent on the project.")
            print("But Brett never grinds at home and Miss Keough is very generous.") 
            p_ts3 = int(10)
        else:
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points in Keough's.")
    # Courts
        print("Moving on to the location: the courts.")
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(3) # Brett is not too great at squash.s
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(7)
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has fectched it.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(0)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
#Now the swimming pool.
        print("Moving on to the swimming pool.")
        print("Swimming the 100 Back against Nick.") # Switching from Quinn to Nick.
        s_stroke = input("Choose a number for the strength of the stroke, but choose a reasonable number: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. A smart swimmer would not, however, that you want to hit about 100 strokes in the 50 free.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well.")
            p_ts2 = int(30)
        elif int(s_stroke) >= 100:
            print("Nice tempo! You could have been faster. Unfortunately, Nick is too fast in the 100.") # Making it clear how to win next time.
            p_ts2 = int(10)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
# Parking lot
        print("You are in the parking lot.")
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Brett will always win.
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough.")
            print("Unfortunately, his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your car.")
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))

    
# Third Scenario: if Brett starts at the courts.
    if l_1 == "Squash Court":
        print("You are starting at the courts.")
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(3) # Brett is not too great at squash.s
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(7)
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has fectched it.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(0)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
# School
    print("Moving on to the final location: the school.") 
    print("Oh no! You have a project in Ms. Keough's class! You have to make a game.")
    s_test = input("Quick! Choose a number of hours. Don't make it too high or too low. ")
    if int(s_test) > int(0) and int(s_test) < int(100):
        print("You had did somewhat well. At least you didn't choose 0.")
        p_ts3 = int(90) 
    elif int(s_test) == int(0):
        print("Not enough hours spent on the project.")
        print("But Brett never grinds at home and Miss Keough is very generous.") 
        p_ts3 = int(10)
    else:
        p_ts3 = int(0)
# Parking Lot
    print("You are in the parking lot.")
    print("You have to drive against JD. Luckily, JD only has a bicycle.")
    s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Brett will always win.
    from random import *
    s_v = randint(1, 100)
    if int(s_v) < int(s_vehicle):
        print("You won! JD only has a bicycle, so you moved your legs quickly enough.")
        print("Unfortunately, his legs are broken. Still, you are victorious.")
        p_ts4 = int(40)
    else:
        print("You have won! JD was no match for your car.")
        p_ts4 = int(40)
    print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
# Finally the swimming pool.
    print("Moving on to the swimming pool.")
    print("Swimming the 100 Back against Nick.") # Switching from Quinn to Nick.
    s_stroke = input("Choose a number for the strength of the stroke, but choose a reasonable number: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. A smart swimmer would not, however, that you want to hit about 100 strokes in the 50 free.
    if int(s_stroke) > 1000: # Backstroke, you want as many people
        print("You had an impressive number many strokes without enough leg power. You lose but did well.")
        p_ts2 = int(30)
    elif int(s_stroke) >= 100:
        print("Nice tempo! You could have been faster. Unfortunately, Nick is too fast in the 100.") # Making it clear how to win next time.
        p_ts2 = int(10)
    else:
        print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
        p_ts2 = int(-20)
    print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
    total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
    print("These are your total points: " + str(total_points))
    
# Fourth Scenario: Starting at the pool.
    print("Starting at the pool.")
    print("Moving on to the swimming pool.")
    print("Swimming the 100 Back against Nick.") # Switching from Quinn to Nick.
    if l_1 == "Swimming Pool":
        s_stroke = input("Choose a number for the strength of the stroke, but choose a reasonable number: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. A smart swimmer would not, however, that you want to hit about 100 strokes in the 50 free.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well.")
            p_ts2 = int(30)
        elif int(s_stroke) >= 100:
            print("Nice tempo! You could have been faster. Unfortunately, Nick is too fast in the 100.") # Making it clear how to win next time.
            p_ts2 = int(10)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
    # Courts
        print("You are starting at the courts.")
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(3) # Brett is not too great at squash.s
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(7)
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has fectched it.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(0)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
# School
        print("Moving on to the final location: the school.") 
        print("Oh no! You have a project in Ms. Keough's class! You have to make a game.")
        s_test = input("Quick! Choose a number of hours. Don't make it too high or too low. ")
        if int(s_test) > int(0) and int(s_test) < int(100):
            print("You had did somewhat well. At least you didn't choose 0.")
            p_ts3 = int(90) 
        elif int(s_test) == int(0):
            print("Not enough hours spent on the project.")
            print("But Brett never grinds at home and Miss Keough is very generous.") 
            p_ts3 = int(10)
        else:
            p_ts3 = int(0)
# Parking lot
        print("You are in the parking lot.")
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Brett will always win.
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough.")
            print("Unfortunately, his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your car.")
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points)) 

# Done with Brett.

# Now we are coding for Nick.
elif player_name == "Nick":
# Scenario 1: Starting at the pool
    if l_1 == "Swimming Pool":
        print("You are Nick. Time to hit the pool.")
        print("Starting at the pool.")
        print("Moving on to the swimming pool.")
        print("Swimming the 50 Free.") # Switching from Quinn to Nick.
        s_stroke = input("Choose a number for the strength of the stroke and hit it hard: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. Someone who knows Nick and swimmin would know that he would need to go about slower but also fast.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well.")
            p_ts2 = int(20)
        elif int(s_stroke) < 100 and int(s_stroke) >= 75:
            print("Nice tempo! Quinn still won, but nice effort.") # You just can't beat Quinn here.
            p_ts2 = int(25)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Quinn in the 50 free.")
# Going to school next
        print("Moving on to the next location: the school.") 
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere
            print("You didn't do well. At least you didn't choose 0.")
            p_ts3 = int(60) 
        else:
            print("Not enough hours spent on the project.")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
# Moving on to the Courts
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(0) # Nick cannot really hit the ball too well because of his shoulder usually
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(0) # Nick isn't too great at squash.
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has fectched it.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(0)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
# Parking lot.
        print("You are in the parking lot, your final location.")
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Brett will always win.
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough.")
            print("Unfortunately, his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your car.")
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))
# Scenario 2 for Nick: Starting in the school.
    if l_1 == "School":
        print("Moving on to the first location: the school.") 
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere
            print("You didn't do too well. At least you didn't choose 0.")
            p_ts3 = int(60) 
        else:
            print("Not enough hours spent on the essay. It's never enough")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
        # Courts
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(0) # Nick cannot really hit the ball too well because of his shoulder usually
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(0) # Nick isn't too great at squash.
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has fectched it.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(0)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")

     # Parking lot
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Brett will always win.
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough.")
            print("Unfortunately, his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your car.")
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        # Swimming Pool
        print("Here's your final location.")
        print("Moving on to the swimming pool.")
        print("Swimming the 50 Free.") # Switching from Quinn to Nick.s
        s_stroke = input("Choose a number for the strength of the stroke and hit it hard: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. Someone who knows Nick and swimmin would know that he would need to go about slower but also fast.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well.")
            p_ts2 = int(20)
        elif int(s_stroke) < 100 and int(s_stroke) >= 75:
            print("Nice tempo! Quinn still won, but nice effort.") # You just can't beat Quinn here.
            p_ts2 = int(25)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Quinn in the 50 free.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))
# Scenario 3: Courts
    if l_1 == "Courts":
        print("You will be playing Jay-Ho.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(0) # Nick cannot really hit the ball too well because of his shoulder usually
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(0) # Nick isn't too great at squash.
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has fectched it.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(0)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
        # Swimming Pool
        print("Here's your final location.")
        print("Moving on to the swimming pool.")
        print("Swimming the 50 Free.") # Switching from Quinn to Nick.s
        s_stroke = input("Choose a number for the strength of the stroke and hit it hard: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. Someone who knows Nick and swimmin would know that he would need to go about slower but also fast.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well.")
            p_ts2 = int(20)
        elif int(s_stroke) < 100 and int(s_stroke) >= 75:
            print("Nice tempo! Quinn still won, but nice effort.") # You just can't beat Quinn here.
            p_ts2 = int(25)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Quinn in the 50 free.")
     # Parking lot
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Brett will always win.
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough.")
            print("Unfortunately, his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your car.")
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        print("Moving on to the final location: the school.")
        # School
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere
            print("You didn't do too well. At least you didn't choose 0.")
            p_ts3 = int(60) 
        else:
            print("Not enough hours spent on the essay. It's never enough")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))
# Scenario 4 for Nick: Starts at the lot.
    if l_1  == "Parking Lot":
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a vehicle! Think on the reasonable side. ") # Brett will always win.
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough.")
            print("Unfortunately, his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your car.")
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        print("Moving on to the next location: the school.")
        # School
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere
            print("You didn't do too well. At least you didn't choose 0.")
            p_ts3 = int(60) 
        else:
            print("Not enough hours spent on the essay. It's never enough")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
       # Swimming Pool
        print("Here's your next location.")
        print("Moving on to the swimming pool.")
        print("Swimming the 50 Free.") # Switching from Quinn to Nick.s
        s_stroke = input("Choose a number for the strength of the stroke and hit it hard: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. Someone who knows Nick and swimmin would know that he would need to go about slower but also fast.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well.")
            p_ts2 = int(20)
        elif int(s_stroke) < 100 and int(s_stroke) >= 75:
            print("Nice tempo! Quinn still won, but nice effort.") # You just can't beat Quinn here.
            p_ts2 = int(25)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Quinn in the 50 free.")
            # Courts
        print("You will be playing Jay-Ho. This is your final location.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(0) # Nick cannot really hit the ball too well because of his shoulder usually
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(0) # Nick isn't too great at squash.
        else:
            print("You've hit a dropshot!")
            print("Jay-Ho has fectched it.")
            print("Time to move on.") # JD hits 14 when I play him. By squash rules, this game would be 14-12, JD because first with 2 more points wins.
            p_ts1 = int(0)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))

# Finally, we're doing Quinn
if player_name == "Quinn":
    if l_1 == "Swimming Pool":
        print("Here's your next location.")
        print("Moving on to the swimming pool.")
        print("Swimming the 100 Back.") # He has to swim Nick
        s_stroke = input("Choose a number for the strength of the stroke and hit it hard: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. Someone who knows Quinn knows that he has to swim as fast as possible.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well. Nick is quite filthy in the back.")
            p_ts2 = int(20)
        elif int(s_stroke) < 100 and int(s_stroke) >= 50:
            print("Nice tempo! Quinn still won, but nice effort.") # You just can't beat Quinn here.
            p_ts2 = int(25)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
    # School
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere. Yet also Quinn did well.
            print("You did well, unlike Nick.")
            p_ts3 = int(90) 
        else:
            print("Not enough hours spent on the essay. It's never enough")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
# Parking Lot
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a number of leg rotations! Think on the reasonable side. ") # Quinn only has a bike
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough even with a bike.")
            print("Unfortunately, your legs and his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your biking skills.") # Quinn is just a btter biker
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        print("Moving on to the next location: the school.")
        # School
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere
            print("You didn't do too well. At least you didn't choose 0.")
            p_ts3 = int(60) 
        else:
            print("Not enough hours spent on the essay. It's never enough")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
    # Courts
        print("You will be playing Jay-Ho. This is your final location.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(4) # Quinn cannot really hit the ball too well, shouldn't hit lobs
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(8) # Quinn isn't too great at squash, better than Nick
        else:
            print("You've hit a dropshot!")
            print("Oh no! Jay-Ho has fectched it.")
            print("Time to move on.") #Still, one drop shot
            p_ts1 = int(9)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))
# Scenario 2: Start at courts
    if l_1 == "Courts":
        print("You will be playing Jay-Ho. This is your first location.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(4) # Quinn cannot really hit the ball too well, shouldn't hit lobs
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(8) # Quinn isn't too great at squash, better than Nick
        else:
            print("You've hit a dropshot!")
            print("Oh no! Jay-Ho has fectched it.")
            print("Time to move on.") #Still, one drop shot
            p_ts1 = int(9)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
        # School
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere
            print("You didn't do too well. At least you didn't choose 0.")
            p_ts3 = int(60) 
        else:
            print("Not enough hours spent on the essay. It's never enough")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
        # Parking Lot
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a number of leg rotations! Think on the reasonable side. ") # Quinn only has a bike
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough even with a bike.")
            print("Unfortunately, your legs and his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your biking skills.") # Quinn is just a btter biker
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        # Final: Pool
        print("Here's your final location.")
        print("Moving on to the swimming pool.")
        print("Swimming the 100 Back.") # He has to swim Nick
        s_stroke = input("Choose a number for the strength of the stroke and hit it hard: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. Someone who knows Quinn knows that he has to swim as fast as possible.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well. Nick is quite filthy in the back.")
            p_ts2 = int(20)
        elif int(s_stroke) < 100 and int(s_stroke) >= 50:
            print("Nice tempo! Quinn still won, but nice effort.") # You just can't beat Quinn here.
            p_ts2 = int(25)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))
# Scenario 3. Starting at the lot:
    if l_1 == "Parking lot":
    # Parking Lot
        print("You have to drive against JD. Luckily, JD only has a bicycle. However, Quinn only has his bike.")
        s_vehicle = input("Choose a number for a number of leg rotations! Think on the reasonable side. ") # Quinn only has a bike
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough even with a bike.")
            print("Unfortunately, your legs and his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your biking skills.") # Quinn is just a btter biker
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
    # The pool
        print("Here's your next location, the pool.")
        print("Moving on to the swimming pool.")
        print("Swimming the 100 Back.") # He has to swim Nick
        s_stroke = input("Choose a number for the strength of the stroke and hit it hard: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. Someone who knows Quinn knows that he has to swim as fast as possible.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well. Nick is quite filthy in the back.")
            p_ts2 = int(20)
        elif int(s_stroke) < 100 and int(s_stroke) >= 50:
            print("Nice tempo! Quinn still won, but nice effort.") # You just can't beat Quinn here.
            p_ts2 = int(25)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
    # Courts
        print("You will be playing Jay-Ho. This is your next location.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(4) # Quinn cannot really hit the ball too well, shouldn't hit lobs
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(8) # Quinn isn't too great at squash, better than Nick
        else:
            print("You've hit a dropshot!")
            print("Oh no! Jay-Ho has fectched it.")
            print("Time to move on.") #Still, one drop shot
            p_ts1 = int(9)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
    # Final: School
        print("Here's your final location: the school.")
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere
            print("You didn't do too well. At least you didn't choose 0.")
            p_ts3 = int(60) 
        else:
            print("Not enough hours spent on the essay. It's never enough")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))
# Scenario 4: Final for everyone. Starts at school.
    if l_1 == "School":
        print("Here's your first location: the school.")
        print("Oh no! You have an essay in Ms. Crago's class.")
        s_test = input("Quick! Choose a number of hours to spend on the essay. Don't make it too high or too low. ")
        if int(s_test) > int(0) or int(s_test) < int(100): # Old joke that working Crago's class will get you nowhere
            print("You didn't do too well. At least you didn't choose 0.")
            p_ts3 = int(60) 
        else:
            print("Not enough hours spent on the essay. It's never enough")
            print("Crago is not going to take that.") 
            p_ts3 = int(0)
        print("You received " + str(p_ts3) + " points after the essay.")
    # Courts
        print("You will be playing Jay-Ho. This is your next location.")
        print("Jay-Ho wins the racket spin. He will serve first.")
        print("Jay-Ho hits you with a filthy serve.")
        print("You need to return the serve.")
        s_squash = input("Choose a number for the strength of the return. You don't have a chance against Jay-Ho, so just choose any number: ") # Asking for a strength on the return of the serve.
        if int(s_squash) > 1000:
            print("You returned a lob shot. Way too high.")
            print("You've lost the match.")
            p_ts1 = int(4) # Quinn cannot really hit the ball too well, shouldn't hit lobs
        elif int(s_squash) >= 100:
            print("You've hit a volley.")
            print("Jay-Ho misses, but you've still lost.") # Real squash tips.
            print("You've lost the match. Good effort.")
            p_ts1 = int(8) # Quinn isn't too great at squash, better than Nick
        else:
            print("You've hit a dropshot!")
            print("Oh no! Jay-Ho has fectched it.")
            print("Time to move on.") #Still, one drop shot
            p_ts1 = int(9)
        print("You received " + str(p_ts1) + " points after squash with Jay-Ho.")
# Pool
        print("Here's your next location, the pool.")
        print("Moving on to the swimming pool.")
        print("Swimming the 100 Back.") # He has to swim Nick
        s_stroke = input("Choose a number for the strength of the stroke and hit it hard: ") # Asking for a strength of swimming stroke. The answer to this question really depends on the player. Someone who knows Quinn knows that he has to swim as fast as possible.
        if int(s_stroke) > 1000: # Backstroke, you want as many people
            print("You had an impressive number many strokes without enough leg power. You lose but did well. Nick is quite filthy in the back.")
            p_ts2 = int(20)
        elif int(s_stroke) < 100 and int(s_stroke) >= 50:
            print("Nice tempo! Quinn still won, but nice effort.") # You just can't beat Quinn here.
            p_ts2 = int(25)
        else:
            print("You nearly drowned. You have to swim. That's a DQ. We hate to see that.")
            p_ts2 = int(-20)
        print("You received " + str(p_ts2) + " points after racing with Nick in the 100 back.")
# Final location: Parking lot
        print("You have to drive against JD. Luckily, JD only has a bicycle.")
        s_vehicle = input("Choose a number for a number of leg rotations! Think on the reasonable side. ") # Quinn only has a bike
        from random import *
        s_v = randint(1, 100)
        if int(s_v) < int(s_vehicle):
            print("You won! JD only has a bicycle, so you moved your legs quickly enough even with a bike.")
            print("Unfortunately, your legs and his legs are broken. Still, you are victorious.")
            p_ts4 = int(40)
        else:
            print("You have won! JD was no match for your biking skills.") # Quinn is just a btter biker
            p_ts4 = int(40)
        print("You received " + str(p_ts4) + " points after racing with JD on his bicycle.")
        total_points = int(p_ts1+p_ts2+p_ts3+p_ts4)
        print("These are your total points: " + str(total_points))
            

print("You are done with the game! I hope you enjoyed!")
