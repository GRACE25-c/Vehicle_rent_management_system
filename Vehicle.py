from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def  calculate_rent(self,days):
        pass
    def  display_vehicle_details(self):
        pass
    def __init__(self,vehicle_type,vehicle_name,rental_price):
        self.vehicle_type=vehicle_type
        self.vehicle_name=vehicle_name
        self.__rental_price=rental_price
    @property    
    def rental_price(self):
        return self.__rental_price
    


        
