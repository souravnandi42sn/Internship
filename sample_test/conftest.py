import pytest
from jinja2 import Environment,FileSystemLoader,select_autoescape
import json
import generate_report 


args={"user_id":""}

def pytest_addoption(parser):
    parser.addoption("--user_id",action="store",dest="user",help="provide a username")

def pytest_configure(config):
    args["user_id"]=config.option.user

def pytest_unconfigure(config):
    generate_report.generate_template()
