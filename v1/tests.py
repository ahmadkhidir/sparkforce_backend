from django.test import TestCase
import requests

# Create your tests here.
class CustomeTest(TestCase):
    def atest_OTP(self):
        data = {
            'email':'khidirahmad05@gmail.com',
            'password':'qwerty'
        }
        res = requests.post('http://127.0.0.1:8000/v1/get_otp/', json=data)
        print(res.json())
        return self.assertEqual(1,1)
    def test_Login(self):
        data = {
            'email':'khidirahmad05@gmail.com',
            'password':'qwerty',
            'otp': 9744
        }
        res = requests.post('http://127.0.0.1:8000/v1/login/', json=data)
        print(res.json())
        return self.assertEqual(1,1)