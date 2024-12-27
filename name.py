import psycopg2
conn = psycopg2.connect(
    dbname= "Dalles",
    user="postgresql",
    password="root",
    host="localhost",
    port="5432"
)
print("DB connection succesfully")