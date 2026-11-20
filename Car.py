from Vehicle import Vehicle    #import perent class
class Car(Vehicle):  #child class
    def calculate_rent(self,days):  #polymorphisam
        total_amount=(self.rental_price*days)+500
        print("Car rental price including service charge: ",total_amount)
        return total_amount  ##total amount returnd into calculate rent for cunsuming space
    def  display_vehicle_details(self):         #polymorphisam
        print("Vehicle Name: ",self.vehicle_name)
        print("Vehicle Type: ",self.vehicle_type)
        print("Rental Price per day: ",self.rental_price)