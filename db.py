import psycopg2

#connect to the database
con = psycopg2.connect(
    host="localhost",
    database = "Bookstore",
    user = "postgres",
    password="Zaid1999"
)
