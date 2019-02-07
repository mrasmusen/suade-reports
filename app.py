from flask import Flask, request, Response
from database.test_database import TestDatabase
from resources.reports_resource import ReportsResource

app = Flask(__name__)

db = TestDatabase()
reports_resource = ReportsResource(db)

"""
  Only using a single route - whether we're getting an 
  xml file or pdf, it's still ultimately the same resource.
"""
@app.route("/<report_id>")
def get_report(report_id):
  return reports_resource.get_report(request.args.to_dict(), int(report_id))
  
