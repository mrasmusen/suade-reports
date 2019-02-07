"""
  Implementation of ReportsDatabase that connects to a postgres server.
"""
from database.reports_database import ReportsDatabase, BadRequestError, ResourceNotFoundError, MalformedDataError, DuplicateDataError
import pg8000
import json

class PostgresDatabase(ReportsDatabase):
  def __init__(self, username, password):
    self.user = username
    self.password = password
    # TODO put in a config file or something
    self.dbname = "suade"
    self.host = "candidate.suade.org"
  
  def get_report_type_data(self, report_id):
    conn = pg8000.connect(
      database=self.dbname,
      user=self.user,
      password=self.password,
      host=self.host)
    
    try:
      int(report_id)
    except: 
      raise BadRequestError
    
    cursor = conn.cursor()
    cursor.execute("SELECT type FROM reports where id={}".format(report_id))

    res = cursor.fetchall()

    if len(res) == 0:
      raise ResourceNotFoundError

    if len(res) > 1:
      raise DuplicateDataError
    
    try:
      parsed_data = json.loads(res[0][0])
    except Exception:
      raise MalformedDataError

    return parsed_data