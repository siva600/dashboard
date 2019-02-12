import cx_Oracle
from python_mysql_db_config import read_db_config


def connect():
    db_config = read_db_config()

    try:
        connection = cx_Oracle.connect(**db_config,
                                       connection_timeout=180, )
        if connection.is_connected():
            cursor = connection.cursor()
            return cursor
    except Error as error:
        print("Error while connecting to - ", error)


def prod_history():
    with connect() as conn:
        try:
            conn.execute("select database();")
            record = conn.fetchall()
            return record

        except Error as error:
            print("Error while connecting to - ", error)
        finally:
            conn.close()


def service_history():
    with connect() as conn:
        try:
            conn.execute("select database();")
            record = conn.fetchall()
            return record

        except Error as error:
            print("Error while connecting to - ", error)
        finally:
            conn.close()


if __name__ == "__main__":
    connect()
