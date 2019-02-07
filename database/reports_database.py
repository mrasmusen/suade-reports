"""
  Abstract class ReportsDatabase defines the method required 
  by a suade reports database wrapper.
  Also defines some errors for subclasses to raise that can
  be handled by the main app.
"""

from abc import ABC, abstractmethod

# Abstract class

class ReportsDatabase(ABC):

  """
    Gets the 'type' data for a report with the given report_id.
    Returns a python dict containing the parsed data.
  """
  @abstractmethod
  def get_report_type_data(self, report_id):
    pass


# Errors

"""
  Error for when the database is not properly created/connected. (In this case far too
  broad but you get the idea.)
"""
class NoDatabaseError(Exception):
  pass

"""
  The requested resource doesn't exist - effectively a 404
"""
class ResourceNotFoundError(Exception):
  pass

"""
  The method(s) in the ReportsDatabase class return a python dict instead of json. This
  error can be returned if the data exists, but is poorly formed.
"""
class MalformedDataError(Exception):
  pass

"""
  For when the user has input incorrect parameters
"""
class BadRequestError(Exception):
  pass

"""
  Duplicate data - TODO handle duplicates.
"""
class DuplicateDataError(Exception):
  pass