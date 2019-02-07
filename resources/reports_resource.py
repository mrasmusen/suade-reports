"""
  Class handling the reports data, returning a response tuple.
"""

from database.reports_database import NoDatabaseError, ResourceNotFoundError, MalformedDataError
from flask import render_template, send_file
import dicttoxml
import os
import pdfkit

class ReportsResource():
  def __init__(self, database):
    self.db = database
    self.counter = 0 # counter increments so we can be sure to not rename files
    self.pdf_outdir = os.path.join(os.path.dirname(__file__), "temp_pdfs")

    # Clear pdfs directory
    for the_file in os.listdir(self.pdf_outdir):
      file_path = os.path.join(self.pdf_outdir, the_file)
      if os.path.isfile(file_path):
          os.unlink(file_path)

  
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
        html = render_template("pdf_template.html",
                               org_name=data["organization"],
                               reported_time=data["reported_at"],
                               created_time=data["created_at"],
                               inventory=data["inventory"])

        self.counter += 1
        pdffilename = data["organization"] + "-" + str(self.counter) + ".pdf"
        pdfout = os.path.join(self.pdf_outdir, pdffilename)

        pdfkit.from_string(html, pdfout)
                                       
        return send_file(pdfout)
      
    except NoDatabaseError:
      return ("No connection to database.", 503)
    except ResourceNotFoundError:
      return ("Not found.", 404, {})
    except MalformedDataError:
      return ("Could not generate response type - bad data.", 500)