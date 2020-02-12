import pytest
from jinja2 import Environment,FileSystemLoader,select_autoescape
import json
import generate_report 
import os

args={"user_id":""}

def pytest_addoption(parser):
    parser.addoption("--user_id",action="store",dest="user",help="provide a username")

def pytest_configure(config):
    args["user_id"]=config.option.user
    #report_data_path=os.path.join(os.getcwd(),"build","new_data.json")
    report_html_path=os.path.join(os.getcwd(),"report_summary.html") 
    #if(os.path.exists(report_data_path)):
        #os.remove(report_data_path) 
    print("===========================")
    print(report_html_path)
    print("=================================")       
    if(os.path.exists(report_html_path)):
        os.remove("report_summary.html")

    

def pytest_unconfigure(config):
    generate_report.generate_template()
