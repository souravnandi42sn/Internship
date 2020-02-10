import requests
import pytest
import json

#@pytest.fixture
#def fixturetest1():
#	a=["od_en_US","fd89fba2959239b2"]
#	return a

def testuserid(fixturetest1):
    b=fixturetest1[0]
    api="http://qa.richrelevance.com/rrserver/api/user/preference/cpc_automated_user00004?apiKey="+b+"&fields=pref_product"
    response=requests.get(api)
    data=response.json()
    #print(data)
    k="00004"
    try:
        assert data['userId']=="cpc_automated_user"+k
        data=b+" "+"passed\n"
        #data={"api":b,"result":"passed"}
        #data=json.parse(data)
        with open("data.txt","a") as wrt:
            wrt.write(data)
    except:
        #data={"api":b,"result":"failed"}
        data=b+" "+"failed\n"
        #data=json.parse(data)
        with open("data.txt","a") as wrt:
            wrt.write(data)

def testuserid2(fixturetest1):
    b=fixturetest1[1]
    api="http://qa.richrelevance.com/rrserver/api/user/preference/cpc_automated_user00004?apiKey="+b+"&fields=pref_product"
    response=requests.get(api)
    data=response.json()
   #k=input()
    try:
        assert data['userId']=="cpc_automated_user00004"
        data=b+" "+"passed\n"
        #data={"api":b,"result":"passed"}
        #data=json.parse(data)
        with open("data.txt","a") as wrt:
            wrt.write(data)
    except:
        #data={"api":b,"result":"failed"}
        data=b+" "+"failed\n"
        #data=data.parse(data)
        with open("data.txt","a") as wrt:
            wrt.write(data)
    

