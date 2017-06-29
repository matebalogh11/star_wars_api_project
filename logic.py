from werkzeug import security
import db


def save_credentials(username, password):
    password = security.generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    sql = """INSERT INTO users (username, password)
             VALUES (%s, %s);"""
    data = (username, password)
    db.excute_sql(sql, data)


def check_credentials(username, password):
    if username and password:
        return True if len(password) > 5 else False
    return False


def check_username(username):
    sql = """SELECT username FROM users;"""
    users = db.excute_sql(sql, method="column")
    return False if username in users else True


def check_login(username, password):
    sql = """SELECT username FROM users;"""
    users = db.excute_sql(sql, method="column")
    if username in users:
        sql = """SELECT password FROM users WHERE username = %s;"""
        data = (username,)
        hahsed_pw = db.excute_sql(sql, data, method="one")
        if security.check_password_hash(hahsed_pw, password):
            return True
        return False
    return False


def save_votes(pdata, username):
    planet = pdata["planet"]
    planet_id = pdata["id"]
    sql = """SELECT id FROM users WHERE username = %s;"""
    data = (username,)
    user_id = db.excute_sql(sql, data, method="one")
    sql1 = """INSERT INTO planetVotes (planet_id, planet_name, user_id)
              VALUES (%s, %s, %s);"""
    data1 = (planet_id, planet, user_id)
    db.excute_sql(sql1, data1)