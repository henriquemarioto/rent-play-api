from django.test import TestCase
from users.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class UserModelTest(TestCase):
    # USer
    @classmethod
    def setUpTestData(cls) -> None:
        cls.nickname = "Tester1"
        cls.first_name = "Tester"
        cls.last_name = "Anonimous"
        cls.cellphone = "12345678913"
        cls.email = "tester1@email.com"
        cls.password = "123456"

        # CRIAR VENDEDOR
        cls.tester1 = User.objects.create_user(
            nickname = cls.nickname,
            first_name=cls.first_name,
            last_name=cls.last_name,
            cellphone=cls.cellphone,
            email=cls.email,
            password=cls.password,
        )

    # VERIFICAR CAMPOS MODEL USER
    def test_attrs(self):
        self.assertEqual(self.tester1.nickname, self.nickname)
        self.assertEqual(self.tester1.first_name, self.first_name)
        self.assertEqual(self.tester1.last_name, self.last_name)
        self.assertEqual(self.tester1.cellphone, self.cellphone)
        self.assertEqual(self.tester1.email, self.email)
        self.assertNotEqual(self.tester1.password, self.password)  

    

