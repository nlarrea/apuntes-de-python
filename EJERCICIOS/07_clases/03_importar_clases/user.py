class User:
    def __init__(self, first:str, last:str, age:int, username:str):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.username = username

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Age: {self.age}\n")

    def greet_user(self):
        print(f"Hi {self.username}! Have a nice day!\n")


class Admin(User):
    def __init__(self, first: str, last: str, age: int, username: str):
        super().__init__(first, last, age, username)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"These are the privileges of the admin:")

        for privilege in self.privileges:
            print(f"\t- {privilege}")