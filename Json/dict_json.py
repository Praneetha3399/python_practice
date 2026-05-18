import json

web = {
    "browser": "chrome",
    "status": "success"
}

json_data = json.dumps(web)

print(json_data)