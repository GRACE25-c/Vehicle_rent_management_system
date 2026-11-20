from abc import ABC,abstractmethod   #import abstraction method
class Vehicle(ABC):      #perent class
    @abstractmethod
    def  calculate_rent(self,days): #this is an abstract methord
        pass    # pass is used for escape from error
    def  display_vehicle_details(self): #jest defin the function 
        pass    # pass is used for escape from error
    def __init__(self,vehicle_type,vehicle_name,rental_price):   #atributes 
        self.vehicle_type=vehicle_type
        self.vehicle_name=vehicle_name       #constrecter
        self.__rental_price=rental_price
    @property     #encapsulation 
    def rental_price(self):  # conver privert atribute into property . its mean can't modify but its can display where we want
        return self.__rental_price
    


        
