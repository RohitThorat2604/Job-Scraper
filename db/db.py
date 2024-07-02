import mysql.connector 

def register_user(username, password,name, email, city, experience, skills):
    conn = mysql.connector.connect(
        host="bd29ifufkltzcl7iptht-mysql.services.clever-cloud.com",
        user="uxrjacjjzqdnv51i",
        password="qaz4uLVg4gfP6semxwUg",
        database="bd29ifufkltzcl7iptht",
        port="3306"
    )

    cursor = conn.cursor()

    
    SQL_INSERT_QUERY = f"Insert into User ( username,password,name,email,city,experience,skills) values( \"{username}\",\"{password}\", \"{name}\", \"{email}\", \"{city}\", {experience}, \"{skills}\");"
    
    cursor.execute(SQL_INSERT_QUERY)

    conn.commit()

    cursor.close()
    conn.close()




def validate_login(username, password):
    """ Check if the password matches for a given username."""
    conn = mysql.connector.connect(
            host="bd29ifufkltzcl7iptht-mysql.services.clever-cloud.com",
            user="uxrjacjjzqdnv51i",
            password="qaz4uLVg4gfP6semxwUg",
            database="bd29ifufkltzcl7iptht"
        )

    cursor = conn.cursor()
    query = "SELECT 1 FROM User WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None

def extract_user_info(username):
    conn = mysql.connector.connect(
            host="bd29ifufkltzcl7iptht-mysql.services.clever-cloud.com",
            user="uxrjacjjzqdnv51i",
            password="qaz4uLVg4gfP6semxwUg",
            database="bd29ifufkltzcl7iptht"
    )
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM User WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


"""""
TODO:
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