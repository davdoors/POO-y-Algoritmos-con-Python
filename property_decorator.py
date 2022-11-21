'''create a class to handel employees email'''

class Employee:
    def __init__(self,name,last_name):
        self._name = name
        self._last_name = last_name
        pass
    
    # name getter
    @property
    def get_name(self):
        return self._name

    # name setter
    @get_name.setter
    def set_name(self,name):
        self._name = name

    #last name getter
    @property
    def get_last_name(self):
        return self._last_name

    #last name setter
    @get_last_name.setter
    def set_last_name(self,last_name):
        self._last_name = last_name




if __name__ == "__main__":
    #instance object
    emp1 = Employee("david","dorado")

    #with the @property decorator, getters are called as attributes using dot notation.
    print(emp1.get_last_name + " " +emp1.get_name)

    #set attribute outside the class
    emp1.set_last_name = "sevilla"

    print(emp1.get_last_name + " " +emp1.get_name)