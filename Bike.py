from Vehicle import Vehicle #import perant
class Bike(Vehicle):   #child class
    def calculate_rent(self,days):  #polymorphisam . same methord different fuction 
        total_amount=(self.rental_price*days)+100
        print("Bike rental price including service charge: ",total_amount)
        return total_amount #total amount returnd into calculate rent for cunsuming space
    def  display_vehicle_details(self): #polimorphisam 
        print("Vehicle Name: ",self.vehicle_name)
        print("Vehicle Type: ",self.vehicle_type)
        print("Rental Price per one day: ",self.rental_price)