import psycopg2


DB = "swapi"
HOST = "localhost"
USER = "bmate11"
PW = "3dc41885"
DNS = "dbname='{}' user='{}' host='{}' password='{}'".format(DB, USER, HOST, PW)


def excute_sql(query, data=None, method=None):
    conn = None
    try:
        conn = psycopg2.connect(DNS)
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
