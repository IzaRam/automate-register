import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = mydb.cursor()


def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS register_users_db")
    cursor.execute("USE register_users_db")
    cursor.execute("CREATE TABLE IF NOT EXISTS user("
                   "user_id INT PRIMARY KEY AUTO_INCREMENT,"
                   "username VARCHAR(255) NOT NULL,"
                   "email VARCHAR(255) NOT NULL,"
                   "password VARCHAR(255) NOT NULL)")


def get_users_list():
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    users_list = []
    for u in result:
        user = {
            'user_id': u[0],
            'username': u[1],
            'email': u[2]
        }
        users_list.append(user)
    return users_list


def get_user_by_id(user_id):
    sql = f"SELECT * FROM user WHERE user_id='{user_id}'"
    cursor.execute(sql)
    user = cursor.fetchone()
    user_json = {
        "user_id": user[0],
        "username": user[1],
        "email": user[2]
    }
    return user_json


def add_new_user(info):
    sql = "INSERT INTO user (username, email, password) VALUES (%s, %s, %s)"
    val = (info['username'], info['email'], info['password'])
    cursor.execute(sql, val)
    mydb.commit()


def update_user_by_id(user_id, user):
    sql = f"UPDATE user " \
          f"SET username='{user['username']}', email='{user['email']}', password='{user['password']}' " \
          f"WHERE user_id={user_id}"
    cursor.execute(sql)
    mydb.commit()


def delete_user(user_id):
    sql = "DELETE FROM user WHERE user_id = " + user_id
    cursor.execute(sql)
    mydb.commit()


create_database()
