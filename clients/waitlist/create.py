import requests


endpoint = "http://127.0.0.1:8000/v1/waitlist-subscribers/"

data = {
    "fullname": "Ahmad Khidir",
    "country": "Nigeria",
    "phone": "+2349012716734",
    "location": "Bello hall, University of Ibadan, Nigeria",
    "email": "khidirahmad05@gmail.com",
    "field_of_interest": "Software development"
}

response = requests.post(endpoint, json=data)

print(response.json())
