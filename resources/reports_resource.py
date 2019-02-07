"""
  Class handling the reports data, returning a response tuple.
"""

from database.reports_database import NoDatabaseError, ResourceNotFoundError, MalformedDataError
import dicttoxml

class ReportsResource():
  def __init__(self, database):
    self.db = database
  
  def get_report(self, request_args, report_id):
    try:
      format = request_args["fmt"]
      if format not in ["xml", "pdf"]:
        return ("Must include a report type of xml or pdf", 400)
      
      data = self.db.get_report_type_data(report_id)

      if format == "xml":
        xml = dicttoxml.dicttoxml(data)
        return (xml, 200, {"Content-Type": "text/xml"})  
      else:
        return ("OK", 200)
      
    except NoDatabaseError:
      return ("No connection to database.", 503)
    except ResourceNotFoundError:
      return ("Not found.", 404, {})
    except MalformedDataError:
      return ("Could not generate response type - bad data.", 500)