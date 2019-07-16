from user import User
from database import Database

#initialize connection pool when you want to do so!
#Choose where you want to connect to
Database.initialize(database="learning", host="localhost", user="postgres", password="1234")

my_user = User("useremail_2@randomemail.com", "Another", "User", None)

my_user.save_to_db()

print(my_user)

user2 = User.load_from_db_by_email("charles123@randomemail.com")

print(user2)