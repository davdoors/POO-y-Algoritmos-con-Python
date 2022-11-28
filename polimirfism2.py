class User:
    def __init__(self,name,last_name) -> None:
        self.name = name
        self.last_name = last_name
        self.email = self.get_email
        self.job = ""

    @property
    def get_email(self):
        self.email = self.name+self.last_name+"@work.com"
        return self.email

    @get_email.setter
    def set_fullname(self,full_name):
        self.name = full_name[0]
        self.last_name = full_name[1]

    @property
    def job_title(self):
        return self.job

    @job_title.setter
    def set_job_title(self,job):
        self.job = job

    def access(self):
        print("Undefined access")

class Premium(User):
    def __init__(self, name, last_name) -> None:
        super().__init__(name, last_name)

    def access(self):
        print("Premium user has access to all content")

class Free(User):
    def __init__(self, name, last_name) -> None:
        super().__init__(name, last_name)

    def access(self):
        print(self.name + "" + self.last_name + " : limited access to content")


def main():
    user_1 = Premium("David","Dorado")
    user_2 = Free("Maria","Gutierrez")
    
    user_1.set_job_title = "Automation Engineer"
    print("user 1: \n")
    print(user_1.get_email)
    user_1.access()
    print(user_1.job_title+ "\n")
    print("user_2 \n")
    print(user_2.get_email)
    user_2.access()




if __name__ == '__main__':
    main()