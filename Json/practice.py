import json
# 1
data = '{"status": "success", "code": 200}'

p_data = json.loads(data)

print(p_data["status"])
# 2
emp= {
    "user": {
        "name": "Praneetha",
        "role": "SDET"
    }
}
emp_data = json.dumps(emp)

print(emp["user"]["name"])
# 3

fruit = {
    "fruits": ["apple", "banana", "orange"]
}

print(fruit["fruits"][1])

# 4

python= {
    "browser": "chrome",
    "version": 120
}

py_data = json.dumps(python)

print(py_data)

# 5
json_data = {
    "response": {
        "token": "abc123",
        "status": "success"
    }
}

token = json_data["response"]["token"]

print(token)




