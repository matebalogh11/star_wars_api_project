import psycopg2
import urllib
import os


# DB = "swapi"
# HOST = "localhost"
# USER = "bmate11"
# PW = "3dc41885"
# DNS = "dbname='{}' user='{}' host='{}' password='{}'".format(DB, USER, HOST, PW)


def excute_sql(query, data=None, method=None):
    conn = None
    try:
        urllib.parse.uses_netloc.append('postgres')
        url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
    except psycopg2.OperationalError as error:
        print("Uh oh.. something went wrong!")
        print(error)
    else:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(query, data) if data else cursor.execute(query)
            if method == "column":
                return [row[0] for row in cursor]
            elif method == "one":
                return cursor.fetchone()[0]
            elif method == "all":
                return cursor.fetchall()

    finally:
        if conn:
            conn.close()
