from django.test import TestCase
from rest_framework.test import APITestCase
from games.models import Game

from rent_accounts.models import RentAccount
from users.models import User
from platforms.models import Platform

from rest_framework.views import status

class RentAccountModelTest(APITestCase):
     
    # CRIAR VENDEDOR
    @classmethod    
    def setUpTestData(cls) -> None:
        cls.tester2_data = {
            "nickname" : "Tester2",
            "first_name" : "Tester",
            "last_name" : "Anonimous",
            "cellphone" : "12345678915",
            "email" : "tester2@email.com",
            "password" : "123456"
        }
        
        cls.tester2 = User.objects.create_user(**cls.tester2_data)
    # CRIAR PLATAFORMA 
        cls.platfrom_data = {
            "platform_api_id" : "1",
            "icon" : "testeicon",
            "name" : "xbox",
            "image_url" : "https://files.tecnoblog.net/meiobit/wp-content/uploads/2019/11/20191122god-of-war.jpg"
        }   
       
        
        cls.platform = Platform.objects.create(**cls.platfrom_data)

        # CRIAR GAME 
        cls.game_data = {
            "game_api_id" : "1",
            "name" : "Halo",
            "image_url" : "https://files.tecnoblog.net/meiobit/wp-content/uploads/2019/11/20191122god-of-war.jpg",
            "release_date" : "2022-07-15",
            "platforms" : ["22f9819d-56fc-4258-84b6-03025873795b"]
        }      
        
        cls.games = [Game.objects.create(**cls.game_data)]
        

        # CRIAR RENT ACCOUNT
        cls.rent_account_data = {            
            "login" : "conta1@mail.com",
            "password" : "123456",
            "price_per_day" : "3.50",
            "platform" : cls.platform,
            "owner" : cls.tester2,
            "games" : [cls.games]       
        }
        cls.rent_account = RentAccount.objects.create(**cls.rent_account_data)   

    def test_attr_(self):
        for item in self.games:
            self.rent_account.games.add(item)
        self.assertEquals(self.rent_account.login, self.rent_account_data["login"])
        self.assertEquals(self.rent_account.password, self.rent_account_data["password"])
        self.assertEquals(self.rent_account.price_per_day, self.rent_account_data["price_per_day"])
        self.assertEquals(self.rent_account.platform, self.rent_account_data["platform"])
        self.assertEquals(self.rent_account.owner, self.rent_account_data["owner"])
        self.assertEquals(len(self.games), self.rent_account.games.count())       

# class RentAccountViewTest(APITestCase):    
    # def test_register_user(self):
        # new_user = User.objects.create_user(**self.user)
        # token = self.client.post("/api/login/", {"email": self.tester2.email, "password": self.tester2.password}, format="json").json['access']
        # token = self.client.post("/login/", data=self.tester2, format="json").json['access']       
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        # self.assertEquals(token.status_code, status.HTTP_200_OK)
       
    
    # def test_list_rent_account(self):
    #     response = self.client.get("/api/rent_accounts/")

    #     self.assertEquals(response.status_code, status.HTTP_200_OK)

    # def test_create_rent_account(self):
                
    #     response = self.client.post("/api/rent_accounts/", data=self.rent_account_data, format="json").json['access']

    #     self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.auth_token.key, token.data["token"])
        # {
        #     "platform": {
        #         "id": "222e639c-d318-46c2-b505-f51ab03fee9a",
        #         "platform_api_id": "1",
        #     "name": "Xbox Live",
        #     "image_url": "https://files.tecnoblog.net/meiobit/wp-content/uploads/2019/11/20191122god-of-war.jpg"
        #     },
        # "login": "login@mail.com",
        # "password": "12345",
        # "price_per_day": 2.50,
                
        #     "games": [
        #         {
        #             "game_api_id": 1,
        #             "name": "Jogo TriLegal",
        #             "image_url": "https://files.tecnoblog.net/meiobit/wp-content/uploads/2019/11/20191122god-of-war.jpg",
        #             "release_date": "1990-01-03"
        #         }
        #     ]
        # }
       
        # new_rent_account = self.client.post("/api/rent_accounts/", data=self.client)

    
        
   