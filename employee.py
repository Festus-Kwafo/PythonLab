class Employee:
    def __init__(self, _employee_name, _employee_number):
        self._employee_name = _employee_name
        self._employee_number = _employee_number
    
    def set_employee_name(self):
        self._employee_name = str(input("Enter Employee name"))
    
    def set_employee_number(self):
        self.set_employee_number = int(input("Enter Employee number"))

    def get_employee_name(self):
        return self._employee_name

    def get_employee_number(self):
        return self._employee_number

class ProductionWorker(Employee):
    def __init__(self, _employee_name, _employee_number, shift_number, hourly_payrate):
        self.shift_number = shift_number
        self.hourly_payrate = hourly_payrate
        super().__init__(_employee_name, _employee_number)
    
    def set_shift_number(self, shift_number):
        if shift_number == 1 or shift_number == 2:
            self.shift_number = shift_number
        else:
            raise ValueError("Invalid shift number")

    def set_hourly_payrate(self, hourly_payrate):
        self.hourly_payrate = hourly_payrate

    def get_shift_number(self):
        if self.shift_number == 1:
            return "Morning Shift"
        else:
            return "Evening shift"
    
    def get_hourly_payrate(self):
        return self.hourly_payrate