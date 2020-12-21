# Project 2 - Moonlander
# Author: Tarini Srikanth 
# Version: Project 2

def showWelcome():
   #prints the welcome message based on the instrubtable file
   print("\nWelcome aboard the Lunar Module Flight Simulator\n")
   print("   To begin you must specify the LM's initial altitude")
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.\n")
   print("   Good luck and may the force be with you!\n")
   
def getFuel():
    #gets the fuel by asking for user input and using user input validation for negative numbers
    value = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    while(value<=0):
        print("ERROR: Amount of fuel must be positive, please try again\n")
        value = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    return value

def getAltitude():
    #gets the altitude by asking for the user input and uses user input validation for altitudes not in between (1-9999(
    altitude = float(input("Enter the initial altitude of the LM (in meters): "))
    while((altitude<1)or(altitude>9999)):
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again\n")
        altitude = float(input("Enter the initial altitude of the LM (in meters): "))
    return altitude

   
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
        #displays the state of the LM
   
	elapsedTimeRound = round(elapsedTime,0)
	fuelRound = round(fuelAmount,2)
	fuelRateRound = round(fuelRate,2)
	altitudeRound = round(altitude,2)
	velocityRound = round(velocity,2)
	#setting variables for rounding the time, altitude, velocity, fuel and fuel rate
	
	altRoundStr = f'{altitudeRound:.2f}'.rjust(7)
	velRoundStr = f'{velocityRound:.2f}'.rjust(7)
	#for the altitude and velocity, using the f% string formatting and left justified to 7 spaced
	
	if(altitude>0):
                #if the altitude is greater than 0, print the following for LM state
           
		print("Elapsed Time:",str(elapsedTimeRound).rjust(4," "), "s")
		print("        Fuel:",str(fuelRound).rjust(4," "),"l")
		#print(f'        Fuel:{fuelRound:.0f}'.rjust(4, " "),"l")
		print("        Rate:",str(fuelRateRound).rjust(4," "),"l/s")
		#print("    Altitude:",str(altitudeRound).rjust(4, " "),"m")
		print("    Altitude:",altRoundStr,"m")
		print("    Velocity:",velRoundStr,"m/s")
	else:
                #print the following for the landing state, if the altitude is less than 0
		print("\nLM state at landing/impact")
		print("Elapsed Time:",str(elapsedTimeRound).rjust(4," "),"s")
		print("        Fuel:",str(fuelRound).rjust(4," "),"l")
		print("        Rate:",str(fuelRateRound).rjust(4," "),"l/s")
		print("    Altitude:",altRoundStr,"m")
		print("    Velocity:",velRoundStr,"m/s")




def getFuelRate(currentFuel):
   
    #gets the fuel rate from the user and performs input validation between 0 and 9
    fuel = int(input("\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    while((fuel<0)or(fuel>9)):
        print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
        fuel = int(input("\nEnter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
        
    #if the fuel amount is greater than the user input, return the less of the 2 values
        
    if(currentFuel<fuel):
        return currentFuel
    else:
        return fuel
 
def updateAcceleration(gravity, fuelRate):

    #updates the accleeration by the provided equation using fuel rate and gravity
    denominator = fuelRate/5
    numerator = gravity
    total = numerator*(denominator-1)
    return total
    
def updateAltitude(altitude, velocity, acceleration):
   
		if(altitude>0):
			newAltitude = altitude+velocity+(acceleration/2)
			if(newAltitude<=0):
				newAltitude=0
		else:
			newAltitude = 0+velocity+(acceleration/2)
			 #might have to change this value, for restricting only positive values
		return newAltitude

def updateVelocity(velocity, acceleration):
   
    #updates the velocity based on the acceleration
    return velocity+acceleration

def updateFuel(fuel, fuelRate):
    #updates the fuel based on the fuel rate
    return fuel-fuelRate


def displayLMLandingStatus(velocity):
   
    #for the landing status, based on the velocity of the LM, display one of three messages
    if((velocity>=-1)and(velocity<=0)):
        print("\nStatus at landing - The eagle has landed!")
        
    elif((velocity>=-10)and(velocity<=-1)):
        print("\nStatus at landing - Enjoy your oxygen while it lasts!")
        
    else:
        print("\nStatus at landing - Ouch - that hurt!")

