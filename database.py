from sqlalchemy import create_engine,text
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

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row))
        return jobs

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs"))

#     result_dicts = []
#     for row in result.all():
#         result_dicts.append(dict(row))

#     print(result_dicts)

    # print("type(result): ", type(result))
    # result_all = result.all()
    # print("type(result.all()): ", type(result_all))
    # first_result =  result_all[0]
    # print("type(first_result): ", type(first_result))
    # first_result_dict = dict(result_all[0])
    # print("type(first_result_dict: ", type(first_result_dict))
    # print(first_result_dict)