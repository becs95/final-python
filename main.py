import psycopg2

DB_NAME= "PRO_GOL"
DB_USER = "REBECA@DESKTOP-RLU1HL0"
DB_PASSWORD = "ROOT"
DB_HOST = "LOCALHOST"
DB_PORT = "5432"

try: 
    Connection = psycopg2.connect {
        'NAME' = DB_NAME,
        'USER' = DB_USER,
        password =DB_PASSWORD
        host = DB_HOST
        port =DB_PORT
    }
    
    print ("se logro connectar")

except psycopg2.Error as err :
    print ("error al conectarse a la BDD")

    if Connection: 
        Connection.close()
        