from Vehicle import Vehicle
class Car(Vehicle):
    def calculate_rent(self,days):
        total_amount=(self.rental_price*days)+500
        print("Car rental price including service charge: ",total_amount)
        return total_amount
    def  display_vehicle_details(self):
        print("Vehicle Name: ",self.vehicle_name)
        print("Vehicle Type: ",self.vehicle_type)
        print("Rental Price per day: ",self.rental_price)