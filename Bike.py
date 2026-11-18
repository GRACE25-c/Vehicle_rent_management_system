from Vehicle import Vehicle
class Bike(Vehicle):
    def calculate_rent(self,days):
        total_amount=(self.rental_price*days)+100
        print("Bike rental price including service charge: ",total_amount)
        return total_amount
    def  display_vehicle_details(self):
        print("Vehicle Name: ",self.vehicle_name)
        print("Vehicle Type: ",self.vehicle_type)
        print("Rental Price per one day: ",self.rental_price)