from dotenv import load_dotenv
import os

load_dotenv()

test = os.getenv("APP_NAME")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
name = os.getenv("DB_NAME")

print(test,host,port,user,password,name)