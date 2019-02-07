import dicttoxml

from resources.reports_resource import ReportsResource
from database.test_database import TestDatabase
from test.test_data import test_data

reports_resource = ReportsResource(TestDatabase())

def test_get_xml_basic():
  res = reports_resource.get_report({"fmt": "xml"}, 6)
  assert res[1] == 200
  assert res[2]["Content-Type"] == "text/xml"
  assert res[0] == dicttoxml.dicttoxml(test_data)
