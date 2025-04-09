from datetime import datetime
import sqlite3
import uuid
import bcrypt

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

with open('create_table.txt', 'r') as readfile:
    cursor.executescript(readfile.read())


class Users:
    def __init__(self, first_name, last_name, city, state, email, password, address, phone):
        self.user_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.date_created = datetime.now().strftime('%x')
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"""User ID:      {self.user_id}
First Name:   {self.first_name}
Last Name:    {self.last_name}
City:         {self.city}
State:        {self.state}
Email:        {self.email}
Password:     {self.password}
Date Created: {self.date_created}
Address:      {self.address}
Birth Date:   {self.phone}"""

    def _check_password(self):
        old_password = input("Verify previous password: ")
        while not bcrypt.checkpw(old_password.encode('utf-8'), self.password):
            print(self.password)
            old_password = input("Passwords do not match, try again: ")

    def change_password(self):
        self._check_password()
        new_password = input("Enter new password: ")
        self.password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

    def update_email(self, new_email):
        self.email = new_email
        print("Email Address updated to:",new_email)

    def view_user(self):
        print(f"User ID:      {self.user_id}")
        print(f"First Name:   {self.first_name}")
        print(f"Last Name:    {self.last_name}")
        print(f"City:         {self.city}")
        print(f"State:        {self.state}")
        print(f"Email:        {self.email}")
        print(f"Password:     {self.password}")
        print(f"Date Created: {self.date_created}")
        print(f"Address:      {self.address}")
        print(f"Birth Date:   {self.phone}")

    def load_user(self, user_id):
        query = "SELECT * FROM Users WHERE user_id = ?"
        result = cursor.execute(query, (user_id,)).fetchone()

        if not result:
            print("No user found.")
            return
        self.user_id = result[0]
        self.first_name = result[1]
        self.last_name = result[2]
        self.city = result[3]
        self.state = result[4]
        self.email = result[5]
        self.password = result[6]
        self.date_created = result[7]
        self.address = result[8]
        self.phone = result[9]

    # def add_user(self):
    #     query = "INSERT INTO Users (user_id, first_name, last_name, city, state, email, password, date_created, address, phone) VALUES (?,?,?,?,?,?,?,?,?,?)"
    #     values = (self.user_id, self.first_name, self.last_name, self.city, self.state, self.email, self.password, self.date_created, self.address, self.phone)
    #     cursor.execute(query,values)
    #     connection.commit()

    def save_user(self):
        if cursor.execute("SELECT * FROM Users WHERE user_id = ?", (self.user_id,)).fetchone():
            query = "UPDATE Users SET user_id=?, first_name=?, last_name=?, city=?, state=?, email=?, password=?, date_created=?, address=?, phone=? WHERE user_id=?"
            values = (self.user_id, self.first_name, self.last_name, self.city, self.state, self.email, self.password, self.date_created, self.address, self.phone, self.user_id)
        else:
            query = "INSERT INTO Users (user_id, first_name, last_name, city, state, email, password, date_created, address, phone) VALUES (?,?,?,?,?,?,?,?,?,?)"
            values = (self.user_id, self.first_name, self.last_name, self.city, self.state, self.email, self.password, self.date_created, self.address, self.phone)
        cursor.execute(query,values)
        connection.commit()




user_1 = Users("George", "Jungle", "The", "Jungle", "george@jungle.com", "Bananas1!", "123 Vine Ave", "??/??/????")
# user_1.save_user()

user_2 = Users('', '', '', '', '', '', '', '')
user_2.load_user('a535bde0-304a-4972-bd35-c772c394e872')

# user_2.update_email("george2@jungle.com")

print(user_2)
# user_2.change_password()
# user_2.view_user()
# user_2.save_user()