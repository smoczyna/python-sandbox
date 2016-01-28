# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Jaja (58128)"
__date__ = "$07-Dec-2015 08:45:28$"

#import requests
#response = requests.get(url, stream=True)


# traverses cells in a workbook,
# calling a callback function on each cell
#from contextlib import closing
#def process_workbook(path, callback=None):
#    if callback is None:
#        def callback(cell):
#            print cell, 
#        
#    with open(path, "rb") as file:
#        with closing(HSSFWorkbook(file)) as workbook:
#            for sheet in workbook:
#                for row in sheet:
#                    for cell in row:
#                        callback(cell)
#
#from org.apache.poi.hssf.usermodel import HSSFWorkbook
#workbook = HSSFWorkbook(open("d:/timesheets/timesheet_template.xls", "rb"))
#process_workbook(workbook)                        

#f = open("d:\TEMP\jython\nov_timesheet.xls", "wb")
#f.writelines(response.iter_content(512))
#f.close()