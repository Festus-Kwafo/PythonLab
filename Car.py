class Car:
    def __init__(self, _year_model, _make):
        self._year_model = _year_model
        self._make = _make
        self._speed= 0
    
    def accelerate(self):
        self._speed +=5
        
    def brake(self):
        self._speed -=5
    
    def get_speed(self):
        return self._speed

Mycar = Car("Corolla", "2020")
print(Mycar.get_speed())

    