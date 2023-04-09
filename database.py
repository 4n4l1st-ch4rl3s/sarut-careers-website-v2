import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import config

username = config.username
password = config.password
host = config.host
database = config.database

db_connection_string = "mysql+pymysql://"+username+":"+password+"@"+host+"/"+database+"?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/certs/cert.pem"
    }
    })

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    print(result.all())
