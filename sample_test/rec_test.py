import pytest
import requests
import json
from conftest import args
from collections import defaultdict

report_data=defaultdict(list)

def get_test_params():
    with open("config/config.json","r") as f:
        data=json.load(f)
    l=[]
    for i in data.keys():
        l.append((i,data[i]["api_key"]))
    return l

test_params = get_test_params()

@pytest.mark.parametrize("client_name, api_key", test_params)
def test_evaluate(client_name,api_key):
    response=requests.get("http://qa.richrelevance.com/rrserver/api/user/preference/cpc_automated_user00004?apiKey="+api_key+"&fields=pref_product")    
    c=response.json()
    with open("build/new_data.json","w") as file:
        try:
            assert c["userId"]=="cpc_automated_user"+args["user_id"]
            report_data[client_name]={"status":"passed","user_id":args["user_id"]}
            json.dump(report_data,file)
        except:
            report_data[client_name]={"status":"failed","user_id":args["user_id"]}
            json.dump(report_data,file)
       

    
        
    

