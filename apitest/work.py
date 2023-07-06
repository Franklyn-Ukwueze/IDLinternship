import requests, os
from requests.auth import HTTPBasicAuth
token = os.environ.get("ACCESS_TOKEN")

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

def get_api_response(url, request_type, payload=None):
    headers = {"content-type": "text/plain"}
    
    try:
        #Make API call
        if request_type == "get":
            r = requests.get(url=url, auth=HTTPBasicAuth(username, password), headers=headers, json=payload)
        elif request_type == "post":
            r = requests.post(url=url, auth=HTTPBasicAuth(username, password), headers=headers, json=payload)
        elif request_type == "put":
            r = requests.put(url=url, auth=HTTPBasicAuth(username, password), headers=headers, json=payload)

            
        print(f"Status code: {r.status_code}")  #Print status code
        response = r.json()
    except Exception as e:
        return f"Encountered error: {e}"

    print(response)

payload = {}
get_api_response("", "get")

