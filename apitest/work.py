import requests, os
from requests.auth import HTTPBasicAuth
token = os.environ.get("ACCESS_TOKEN")

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

def get_api_response(url, request_type, bearer_token, payload=None):
    headers = {"content-type": "application/json", "Authorization": f"Bearer {bearer_token}"}
    
    try:
        #Make API call
        if request_type == "get":
            r = requests.get(url=url, headers=headers, json=payload)
        elif request_type == "post":
            r = requests.post(url=url, headers=headers, json=payload)
        elif request_type == "put":
            r = requests.put(url=url, headers=headers, json=payload)

            
        print(f"Status code: {r.status_code}")  #Print status code
        response = r.json()

        # save_path = "equity_file.xlsx"
        # if response.status_code == 200:
        #     with open(save_path, 'wb') as file:
        #         file.write(response.content)
        #     print("File downloaded successfully.")
        # else:
        #     print(f"Failed to download file. Status code: {response.status_code}")

    except Exception as e:
        return f"Encountered error: {e}"

    print(response)

payload = {}
get_api_response("", "get", bearer_token="")

