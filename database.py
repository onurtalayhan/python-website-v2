from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://3045quxmoqf6w5nxog6j:pscale_pw_OfqqsJ6cAnrhNfy4AjDs5SJxAhYxJQAVmCMUYmwvCe8@eu-west.connect.psdb.cloud/pythonwebsite?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca": "/etc/sll/cert.pem"
    }                      
  })
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
    
    jobs = []
    
    for row in result.all():
      jobs.append(dict(zip(column_names, row)))
    return jobs



    
 


  
  