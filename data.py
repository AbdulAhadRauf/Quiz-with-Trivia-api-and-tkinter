import requests
parameters = {
    "type": "boolean",
    "amount": 10,

}
response = requests.get("https://opentdb.com/api.php", params = parameters)
response.raise_for_status()
data = response.json()
question_list = data["results"]
print(question_list)