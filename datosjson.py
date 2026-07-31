import json 

with open("myfile.json", "r") as json_file: ourjson = json.load(json_file) 
print("Token:") 
print(ourjson["access_token"]) 
 
print("Tiempo restante antes de caducar:") 
print(ourjson["expires_in"])
