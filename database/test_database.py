"""
  Dummy implementation of the ReportsDatabase class to test the routing and error
  handling in the main app. Certain pre-defined inputs will cause the dummy 
  database to return errors, ensuring that the app handles them gracefully.
"""
from database.reports_database import ReportsDatabase, ResourceNotFoundError, MalformedDataError, NoDatabaseError
from test.test_data import test_data

class TestDatabase(ReportsDatabase):

  """
    Returns some dummy data for the report type. If the id is 1 raise 
    a ResourceNotFoundError, if it's 2 raise a MalformedDataError and
    if it's 3 return a NoDatabaseError. 
  """
  def get_report_type_data(self, report_id):
    if report_id == 1:
      raise ResourceNotFoundError
    elif report_id == 2:
      raise MalformedDataError
    elif report_id == 3: 
      raise NoDatabaseError
    else:
      return test_data