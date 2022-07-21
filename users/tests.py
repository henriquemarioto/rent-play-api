from django.test import TestCase
from users.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.views import status
from rest_framework.authtoken.models import Token


class UserModelTest(APITestCase):
    # USERS 
    @classmethod
    def setUpTestData(cls) -> None:
        cls.nickname = "Tester1"
        cls.first_name = "Tester1"
        cls.last_name = "Anonimous"
        cls.cellphone = "12345678913"
        cls.email = "tester1@email.com"
        cls.password = "123456"

        # CRIAR TESTER 1
        cls.tester1 = User.objects.create_user(
            nickname = cls.nickname,
            first_name=cls.first_name,
            last_name=cls.last_name,
            cellphone=cls.cellphone,
            email=cls.email,
            password=cls.password,
        )

        cls.user1 = {
            "nickname": "Tester2",
            "first_name": "Tester2",
            "last_name":  "Anonimous",
            "password": "123456",
            "cellphone": "12345678914",
            "email": "tester2@email.com"
        }

        cls.user2 = {
            "nickname": "Tester1",
            "first_name": "Tester1",
            "last_name":  "Anonimous",
            "password": "123456",
            "cellphone": "12345678913",
            "email": "tester1@email.com"
        }

  

    # VERIFICAR CAMPOS MODEL USER
    def test_attributos(self):
        self.assertEqual(self.tester1.nickname, self.nickname)
        self.assertEqual(self.tester1.first_name, self.first_name)
        self.assertEqual(self.tester1.last_name, self.last_name)
        self.assertEqual(self.tester1.cellphone, self.cellphone)
        self.assertEqual(self.tester1.email, self.email)
        self.assertNotEqual(self.tester1.password, self.password)  

    def test_create_user(self):
        response = self.client.post("/users/", data=self.user1)        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 


    def test_create_duplicate_user(self):
        response = self.client.post("/users/", data=self.user2)        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["nickname"][0], "user with this nickname already exists.")
        self.assertEqual(response.data["cellphone"][0], "user with this cellphone already exists.")
        self.assertEqual(response.data["email"][0], "user with this email already exists.") 


    def test_create_user_no_data(self):
        user = {}

        response = self.client.post("/users/", data=user)      
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["nickname"][0], "This field is required.")
        self.assertEqual(response.data["first_name"][0], "This field is required.")
        self.assertEqual(response.data["last_name"][0], "This field is required.")
        self.assertEqual(response.data["cellphone"][0], "This field is required.")
        self.assertEqual(response.data["email"][0], "This field is required.")
        self.assertEqual(response.data["password"][0], "This field is required.")


    def test_login_user(self):       
        
        res = self.client.post("/login/", data={"email": self.email, "password": self.password})
        token = Token.objects.get(user=self.tester1)

       
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(token.key, res.data["token"])


    def test_update_user(self):

        self.client.force_authenticate(user=self.tester1)

        update = {"nickname": "update1",
            "cellphone": 499125678,
            "wallet": 30,
        }

        response = self.client.patch(f"/users/{self.tester1.id}/", data=update) 
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(response.data["nickname"], "update1") 
        self.assertEqual(response.data["cellphone"], "499125678")
        self.assertEqual(response.data["wallet"], "30.00")

    def test_list_users(self):
        self.client.force_authenticate(user=self.tester1)
        response = self.client.patch(f"/users/{self.tester1.id}/") 
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertGreater(len(response.data), 0 )






