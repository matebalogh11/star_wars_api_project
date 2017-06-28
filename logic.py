from werkzeug import security


def save_credentials():
    pass


def check_credentials(username, password):
    if username and password:
        return True if len(password) > 5 else False
    return False
