#Name: Tarini Srikanth
#Instructor: Turner
#Project 2 - Main moonlander
from landerFuncs import *
def main():
	#create a for loop representing i as each second
	elapsedTime =0
	fuel=0
	rate=0
	altitude=0
	velocity=0
	totalVelocity=0
	rate=0
	acceleration=0
	
	showWelcome()#shows the welcome message
	
	altitude = getAltitude() #gets the user altitude
	
	fuel = getFuel()#gets the user fuel
	
	print("\nLM state at retrorocket cutoff")#prints the display message only once
	
	displayLMState(elapsedTime, altitude, velocity, fuel, rate) #prints the inital LM state


	while(altitude>0):
		elapsedTime=elapsedTime+1
		
		newRate=getFuelRate(fuel)#new rate of fuel
		rate=newRate
		
		newAcceleration = updateAcceleration(1.62,rate)#updating the acceleration
		acceleration=newAcceleration
		
		newAltitude = updateAltitude(altitude,velocity,acceleration)
		altitude=newAltitude
		
		newVelocity=updateVelocity(velocity,acceleration)#calculating the new velocity
		velocity=newVelocity
		totalVelocity=totalVelocity+newVelocity #keeping track of the total velocity
		
		newFuel=updateFuel(fuel,rate) # updating the fuel
		fuel=newFuel
		
		displayLMState(elapsedTime, altitude, velocity, fuel, rate)
		#end of while loop
	displayLMLandingStatus(velocity)#displays the landing status







if __name__ == '__main__':
    main()
    
