import mariadb as db
import dbcreds as c

# connect to database function
def connect_db():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=c.user,
                          password=c.password,
                          host=c.host,
                          port=c.port,
                          database=c.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print("something went wrong with the DB, please try again in 5 minutes")
    except Exception as e:
        print(e)
        print("Something went wrong!")
    return conn, cursor  

# disconnect from database function
def disconnect_db(conn, cursor):
    try:
        cursor.close()
    except Exception as e:
        print(e)
        print("cursor close error: what happened?")

    try:
        conn.close()
    except Exception as e:
        print(e)
        print("connection close error")

def get_hero_db():
    conn, cursor = connect_db()
    heros = None
    heros_labeled = []
    
    cursor.execute("select id, name, secret_identity, powers, power_rating, image_url from hero")
    heros = cursor.fetchall()

    disconnect_db(conn, cursor)

    for hero in heros:
        hero_dict = {
            "id": hero[0],
            "name": hero[1],
            "secret_identity": hero[2],
            "powers": hero[3],
            "power_rating": hero[4],
            "image_url": hero[5]
        }
        heros_labeled.append(hero_dict)

    return heros_labeled

def get_villian_db():
    conn, cursor = connect_db()
    villians = None
    villians_labeled = []

    
    cursor.execute("select id, name, secret_identity, powers, power_rating, image_url from villian")
    villians = cursor.fetchall()

    disconnect_db(conn, cursor)

    for villian in villians:
        villian_dict = {
            "id": villian[0],
            "name": villian[1],
            "secret_identity": villian[2],
            "powers": villian[3],
            "power_rating": villian[4],
            "image_url": villian[5]
        }
        villians_labeled.append(villian_dict)

    return villians_labeled
