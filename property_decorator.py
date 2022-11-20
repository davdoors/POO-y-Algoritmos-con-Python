'''create a class to handel employees email'''

class Employee:
    def __init__(self,name,last_name):
        self._name = name
        self._last_name = last_name
        pass

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self,name):
        self._name = name

    @property
    def get_last_name(self):
        return self._last_name

    @get_last_name.setter
    def set_last_name(self,last_name):
        self._last_name = last_name




if __name__ == "__main__":
    emp1 = Employee("david","dorado")

    print(emp1.get_last_name + " " +emp1.get_name)

    emp1.set_last_name = "sevilla"

    print(emp1.get_last_name + " " +emp1.get_name)