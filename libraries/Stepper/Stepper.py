from bbio import *

class Stepper:
	def __init__(self, number_of_steps, motor_pin_1, motor_pin_2, motor_pin_3, motor_pin_4):
        	self.number_of_steps = number_of_steps
   		self.motor_pin_1 = motor_pin_1
		self.motor_pin_2 = motor_pin_2
		self.motor_pin_3 = motor_pin_3
		self.motor_pin_4 = motor_pin_4
      		self.last_step_time = 0   # time stamp in ms since the last step is taken
      		self.step_number = 0      # keep in account the number of steps moved
      		self.direction = 0	  # direction of rotation of motor

   	def setSpeed(self, whatSpeed):	  # Sets the speen in revolution per minute
		self.whatSpeed = whatSpeed
        	self.step_delay = (60*1000*self.whatSpeed)/number_of_steps	# delay between 2 steps 

      	def step(self, steps_to_move):	#  Moves the motor by steps_to_move steps. If number is negative motor moves in reverse direction
        	self.steps_to_move = steps_to_move
         	steps_left = abs(self.steps_to_move)
         	if(steps_left > 0):
	    		self.direction = 1
         	if(steps_left < 0):
	    		self.direction = 0

      		while(steps_left > 0):
	 		if(millis() - last_step_time >= step_delay):
	    			self.last_step_time = millis()
	    			# now increment or decrement the step number depending on the direction
	    			if (self.direction == 1):
	       				self.step_number+=1
	       				if(self.step_number == number_of_steps):
		  				self.step_number = 0

            		else:
				if(self.step_number == 0):
		   			self.step_number = self.number_of_steps
            			self.step_number-=1
         		self.steps_left-=1
         		stepMotor(step_number%4)

     	def stepMotor(self,thisStep):
		self.thisStep = thisStep
		if(self.thisStep == 0 ):			#  1010 
	   		digitalWrite(self.motor_pin_1, HIGH)
	   		digitalWrite(self.motor_pin_2, LOW)
	   		digitalWrite(self.motor_pin_3, HIGH)
	   		digitalWrite(self.motor_pin_4, LOW)
		elif(self.thisStep == 1):			# 0110
	   		digitalWrite(self.motor_pin_1, LOW)
	   		digitalWrite(self.motor_pin_2, HIGH)
           		digitalWrite(self.motor_pin_3, HIGH)
           		digitalWrite(self.motor_pin_4, LOW)
        	elif(self.thisStep == 2):			# 0101
	   		digitalWrite(self.motor_pin_1, LOW)
	   		digitalWrite(self.motor_pin_2, HIGH)
           		digitalWrite(self.motor_pin_3, LOW)
           		digitalWrite(self.motor_pin_4, HIGH)
       		elif(self.thisStep == 3):			# 1001
	  	 	digitalWrite(self.motor_pin_1, HIGH)
	   		digitalWrite(self.motor_pin_2, LOW)
           		digitalWrite(self.motor_pin_3, LOW)
	   		digitalWrite(self.motor_pin_4, HIGH)
