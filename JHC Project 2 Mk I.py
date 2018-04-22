"""
    Application: JHC Project 2
    Start: 2.6.2018, at 12:26 PM EST
    Author: Jay-Ho Chung
    Purpose: Wind Chill Calculator, Braking Distance Calculator
"""

#Time to make this wind chill program.

#First, save variables.
print("Part 1")
print("")
T = 10.0 #Temperature is degrees
V = 15.0 #Wind speed in MPH
W = 35.74 + 0.6215*(int(T)) - 35.75*((int(V))**0.16) + 0.4275*T*((int(V))**0.16) #Wind chill equation, demo 1 

print("") #Printing our values
print("Temperature (Farenheit): " + str(T))
print("Wind speed (MPH): " + str(V))
print("Wind Chill (Farenheit): " + str(W))

T = 0.0 #Temperature is degrees
V = 25.0 #Wind speed in MPH
W = 35.74 + 0.6215*(int(T)) - 35.75*((int(V))**0.16) + 0.4275*T*((int(V))**0.16) #Wind chill equation, demo 2

print("") #Printing our values down here
print("Temperature (Farenheit): " + str(T))
print("Wind speed (MPH): " + str(V))
print("Wind Chill (Farenheit): " + str(W))

T = -10.0 #Temperature is degrees
V = 35.0 #Wind speed in MPH
W = 35.74 + 0.6215*(int(T)) - 35.75*((int(V))**0.16) + 0.4275*T*((int(V))**0.16)

print("")
print("Temperature (Farenheit): " + str(T))
print("Wind speed (MPH): " + str(V))
print("Wind Chill (Farenheit): " + str(W))

#Time to look for input.
print("")

#General equation which needs to accept floats
T = float(input("Temperature: ")) #By writing float() over all of this, our functions also accepts float values. Could write it a different way too.
#Temperature is degrees
V = float(input("Wind speed: ")) #Wind speed in MPH
W = 35.74 + 0.6215*(int(T)) - 35.75*((int(V))**0.16) + 0.4275*T*((int(V))**0.16)


print("Temperature (Farenheit): " + str(T))
print("Wind speed (MPH): " + str(V))
print("Your Wind Chill (Farenheit): " + str(W)) #Printing the wind chill temperature values that the user inputs.

print("")
print("")
print("")
print("Part 2")
print("")

#First set of values
mu = 0.60 #mu, our coefficient of friction
V = 40 #km/h, need to convert
v = (V*1000)/(60*60) #Equation to convert km/h to m/s
D = (v**2) / (2*mu*9.8) #Our distance equation. 9.8=g.
print("If our coeffcient value is " + str(mu) + " and velocity is "  + str(V) +"km/h, then our braking distance is " + str(D) + " meters.")
print("")
#Second set of values
mu = 0.25
V = 100
v = (V*1000)/(60*60) #Equation to convert it.
D = (v**2) / (2*mu*9.8) #Our distance equation.
print("If our coeffcient value is " + str(mu) + " and velocity is "  + str(V) +"km/h, then our braking distance is " + str(D) + " meters.")

#Time to expand beyond just a few variables.
print("")
mu = float(input("Coefficient of Friction (Negative mu does not exist): ")) #This should technically only accept positive values
V = float(input("Velocity, in km/h: "))
v = (V*1000)/(60*60) #Equation to convert it.
D = (v**2) / (2*mu*9.8) #Our distance equation.
print("If our coeffcient value is " + str(mu) + " and velocity is "  + str(V) +" km/h, then our braking distance is " + str(D) + " meters.")
