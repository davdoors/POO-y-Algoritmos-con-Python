class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def area (self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self,side):
        #call parent class constructor
        super().__init__(side,side)

class User:
    def __init__(self,name,last_name,job_title):
        self._name = name
        self._last_name = last_name
        self._job_title = job_title
        self._email = ""

    @property
    def email(self):
        return self._name + "." + self._last_name + "@mail.com"

    @property
    def user_name(self):
        return self._name + " " + self._last_name

    # Setter can only take one value, so full_name is a tuple that contains name and last_name
    @user_name.setter
    def set_user_name(self,full_name):
        self._name = full_name[0]
        self._last_name = full_name[1]

class Engineer(User):
    def __init__(self, name, last_name, job_title):
        super().__init__(name, last_name, job_title)

if __name__ == '__main__':
    rectangle = Rectangle(3,4)
    print("rectangle area: " , rectangle.area)

    square = Square(8)

    print("Square area: " , square.area)

    emp1 = Engineer("David","Dorado","Electronic")

    print("Emp name " + emp1.user_name)
    print("emai: " + emp1.email)

    emp1.set_user_name = ("Francisco","Sevilla")

    print("Emp name " + emp1.user_name)
    print("emai: " + emp1.email)
