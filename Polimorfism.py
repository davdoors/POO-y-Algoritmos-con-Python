class Person:
    def __init__(self, name) -> None:
        self._name = name

    def go(self):
        print("A person Walks")

class Cyclist(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def go(self):
        print("Cyclist pedals along")


def main():
    pip1 = Person("david")
    pip1.go()

    cyc1 = Cyclist("maria")
    cyc1.go()

if __name__ == '__main__':
    main()