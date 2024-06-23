import mysql.connector

def register_user(username, name, email, city, experience, skills):
    conn = mysql.connector.connect(
        host="bd29ifufkltzcl7iptht-mysql.services.clever-cloud.com",
        user="uxrjacjjzqdnv51i",
        password="qaz4uLVg4gfP6semxwUg",
        database="bd29ifufkltzcl7iptht"
    )

    cursor = conn.cursor()

    
    SQL_INSERT_QUERY = f"Insert into User ( username,name,email,city,experience,skills) values( \"{username}\", \"{name}\", \"{email}\", \"{city}\", {experience}, \"{skills}\");"
    
    cursor.execute(SQL_INSERT_QUERY)

    conn.commit()

    cursor.close()
    conn.close()

"""
# TODO:
    write a function to check if a username exists
        def is_user_exists(username):
            return true or false
        
    write a function to check if the password matches
        def check_validity(username, password):
            if is_user_exists(username) == True

            username, password 
            
            select * from users where username, password

            return true or false

"""