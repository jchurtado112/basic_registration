from database import CursorFromConnectionPool

class User:
    def __init__(self, email, first_name, last_name, id):
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.id=id

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        #with connection_pool.getconn() as connection:   #########
        #connection = connection_pool.getconn()   ######
        #with ConnectionFromPool() as connection:   ######
        with CursorFromConnectionPool() as cursor:
            cursor.execute("INSERT INTO public.users(email,first_name,last_name) VALUES(%s,%s,%s);",(self.email, self.first_name, self.last_name))


    #Load specific profile by email from DB (filtering data)
    @classmethod
    def load_from_db_by_email(cls, email):
        #with connection_pool.getconn() as connection:  ####
        #with ConnectionFromPool() as connection:  #####
        with CursorFromConnectionPool() as cursor:
            cursor.execute("SELECT * FROM users WHERE users.email=%s ;", (email,))
            user_data = cursor.fetchone()   #Used to Retieve first row in table
            return cls(email=user_data[1], first_name=user_data[2] , last_name=user_data[3], id=user_data[0])







