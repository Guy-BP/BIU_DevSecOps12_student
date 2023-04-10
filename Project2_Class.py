class MyUser:

    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f'\n ID --> {self.id}\n Name --> {self.name}\n Username --> {self.username}\n Email --> {self.email}'