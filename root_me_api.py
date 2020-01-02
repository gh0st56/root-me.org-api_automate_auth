import requests
import json

def login():
    while True:
        login_api = input("Please type your Username: ")
        if len(login_api) != 0:
            passwd_api = input("Please type your Password: ")
            if len(passwd_api) != 0:
                login_url_root = requests.get("https://api.www.root-me.org/login?login="+login_api+"&password="+passwd_api+"", verify=False)
                api_login_response = login_url_root.json()
                print(json.dumps(api_login_response, indent=4, sort_keys=True))
                if login_url_root.status_code == 200:
                    break
        else:
            print("Please provide your user/pass")
login()
msg = """
 ___ _                                                           ___ ___ ___ ___   _            _ 
 | _ \ |___ __ _ ___ ___   __ ___ _ __ _  _   _  _ ___ _  _ _ _  / __| _ \_ _| _ \ | |_____ _  _| |
 |  _/ / -_) _` (_-</ -_) / _/ _ \ '_ \ || | | || / _ \ || | '_| \__ \  _/| ||  _/ | / / -_) || |_|
 |_| |_\___\__,_/__/\___| \__\___/ .__/\_, |  \_, \___/\_,_|_|   |___/_| |___|_|   |_\_\___|\_, (_)
                                 |_|   |__/   |__/                                          |__/   

"""
print(msg)
spip_input = input("Please provide your SPIP key: ")
print("Your spip key is: "+spip_input+"/r/n")
session = {"spip_session": spip_input}
api_request = requests.get("https://api.www.root-me.org/challenges?lang=en", cookies=session, verify=False)
response = api_request.json()
print(json.dumps(response, indent=4, sort_keys=True))
while True:
    id_select = input("Type the challenge ID: ")
    if id_select != 0:
        id_select = str(id_select)
        api_request = requests.get("https://api.www.root-me.org/challenges/"+id_select+"/r/n", cookies=session, verify=False)
        response = api_request.json()    
        print(json.dumps(response, indent=4, sort_keys=True))
