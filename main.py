from Car import Car   #import child class
car=Car("Four wheeler","Mahendhra",1000)  #create object for Car classs
car.display_vehicle_details()       #call display vehicle details of car
car.calculate_rent(3)   #call calculate rent methord and pass an atribute days  value



#output
# Vehicle Name:  Mahendhra
# Vehicle Type:  Four wheeler
# Rental Price per day:  1000
# Car rental price including service charge:  3500


from Bike import Bike     #import bike class
bike=Bike("Two wheeler","OLA",500)  #create object for bike classs
bike.display_vehicle_details()  #call display vehicle details of bike
bike.calculate_rent(3)          #call calculate rent methord and pass an atribute days  value


#output
# Vehicle Name:  OLA
# Vehicle Type:  Two wheeler
# Rental Price per one day:  500
# Bike rental price including service charge:  1600