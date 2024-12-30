try:
    import psycopg2
    conn = psycopg2.connect(
        dbname= "Dalles",
        user="postgresql",
        password="root",
        host="localhost",
        port="5432"
    )
    print("DB connection succesfully")
except BaseException as e:
    print("DB not connected")
    raise e

if 1>2:
    print ("HI this is Rahul")
else:
    print("Hi bye")
