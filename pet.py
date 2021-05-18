class Pet:
    def __init__(self, _name, _animal_type, _age):
        self._name = _name
        self._animal_type = _animal_type
        self._age = _age
    
    def set_name(self, name):
        self._name = name

    def set_animal_type(self, pet_type):
        self._animal_type = pet_type
    
    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_animal_type(self):
        return self._animal_type

    def get_age(self):
        return self._age
