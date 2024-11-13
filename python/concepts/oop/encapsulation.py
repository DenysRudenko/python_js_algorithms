class Human():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    # public method
    def walking(self):
        return f"{self.name} {self.surname} is walking!"
    
    # public method
    def talking(self):
        return f"{self.name} {self.surname} is talking!"
    
    # private method
    def __coding(self):
        return f"{self.name} {self.surname} is coding!"
    
    # private method
    def __drawing(self):
        return f"{self.name} {self.surname} is drawing!"
    

jerry = Human("Jerry", "Pickachu", 25)

print(jerry.walking())
# print(jerry.coding())
# print(jerry.drawing())
print(jerry.talking())
print("-" * 30)


class User():

    def __init__(self, username, password, id):
        self.__username = username
        self.__password = password
        self.__id = id

    def get_username(self):
        return self.__username
    
    def set_username(self, new_username):
        self.__username = new_username
    
    def set_password(self, new_password):
        self.__password = new_password

    def get_id(self):
        return self.__id
    
    def get_password(self):
        return self.__password
    

alex = User("Alex", "password", 1)

print(alex.get_username())
print(alex.get_id())
print(alex.get_password())
alex.set_password("new_password")
print(alex.get_password())
alex.set_username("Denys")
print(alex.get_username())


class Database():

    def __init__(self, url, port, username, password, tables = None):
        self.__url = url
        self.__port = port
        self.__username = username
        self.__password = password
        self.__tables = tables if tables is not None else []

    def get_url(self):
        return self.__url
    
    def get_port(self):
        return self.__port
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_tables(self):
        return self.__tables
    
    def add_table(self, table_name):
        if table_name not in self.__tables:
            self.__tables.append(table_name)

    def remove_table(self, table_name):
        if table_name in self.__tables:
            self.__tables.remove(table_name)


db = Database("localhost", 5432, "admin", "password", ["users", "orders"])

print(db.get_tables())
db.add_table("price")

print(db.get_tables())

db.remove_table("users")

print(db.get_tables())