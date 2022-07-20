from platform import platform
from django.test import TestCase
from rest_framework.test import APITestCase
from games.models import Game
from rest_framework.authtoken.models import Token
import pdb

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
    # BUSCAR PLATAFORMA 
        # cls.platfrom_data = {
        #     "platform_api_id" : "1",
        #     "icon" : "testeicon",
        #     "name" : "xbox",
        #     "image_url" : "https://files.tecnoblog.net/meiobit/wp-content/uploads/2019/11/20191122god-of-war.jpg"
        # }   
       
        
        cls.platform1 = Platform.objects.get(platform_api_id=1)
        cls.platform2 = Platform.objects.get(platform_api_id=2)
        cls.platforms = [cls.platform1, cls.platform2]

        # CRIAR GAME 
        cls.game_data = {
            "game_api_id" : "1",
            "name" : "Halo",
            "image_url" : "https://files.tecnoblog.net/meiobit/wp-content/uploads/2019/11/20191122god-of-war.jpg",
            "release_date" : "2022-07-15",
            # "platforms": []        
        }      
        
        cls.games = [Game.objects.create(**cls.game_data)]
        
        

        # CRIAR RENT ACCOUNT
        cls.rent_account_data = {            
            "login" : "conta1@mail.com",
            "password" : "123456",
            "price_per_day" : "3.50",
            "platform" : cls.platform1,
            "owner" : cls.tester2,
            # "games" : [cls.games]       
        }
        cls.rent_account = RentAccount.objects.create(**cls.rent_account_data)   

    def test_attr_(self):
        print("PLATFORMMMMMMMMMM", self.platform1.__dict__)
        # print("AQUIIIIII PLATFOMMMMMMMMMMMMMM", self.platforms[0].__dict__)                    
        for item in self.platforms:
            # print("ITEMMMMMMMMMMM", item)
            self.games[0].platforms.add(item)
        for item in self.games:
            self.rent_account.games.add(item)        
        self.assertEquals(self.rent_account.login, self.rent_account_data["login"])
        self.assertEquals(self.rent_account.password, self.rent_account_data["password"])
        self.assertEquals(self.rent_account.price_per_day, self.rent_account_data["price_per_day"])
        self.assertEquals(self.rent_account.platform, self.rent_account_data["platform"])
        self.assertEquals(self.rent_account.owner, self.rent_account_data["owner"])
        self.assertEquals(len(self.games), self.rent_account.games.count())       

# class RentAccountViewTest(APITestCase):    
    def test_login_user(self):       
        
        res = self.client.post("/login/", data={"email": self.tester2_data.get("email"), "password": self.tester2_data.get("password")})
        token = Token.objects.get(user=self.tester2)             
       
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(token.key, res.data["token"])
           

    def test_login_missing_fields(self):   
        
        res = self.client.post("/login/", data={})                  
       
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("email", res.data)
        self.assertIn("password", res.data)
        
       
    
    def test_list_rent_account(self):
        self.client.force_authenticate(user=self.tester2)
        response = self.client.get("/rent_accounts/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_rent_account(self):
        self.client.force_authenticate(user=self.tester2)
        platform2 = Platform.objects.get(platform_api_id=3)
        games2 = {"game_api_id": "2", 
        "name": "Jogo Tri", 
        "image_url": "https://files.tecnoblog.net/meiobit/wp-content/uploads/2019/11/20191122god-of-war.jpg", 
        "release_date": "1990-01-03", 
        "platforms": [self.platform1.id]}
       
        rent_account2 = {
            "platform": platform2.id,
            "login": "login@mail.com",
            "password": "12345",
            "price_per_day": "2.50",                
            "games": [games2]
        }     
       
                     
        response = self.client.post("/rent_accounts/", data=rent_account2, format='json')
        


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)       
        
       
        # new_rent_account = self.client.post("/api/rent_accounts/", data=self.client)

  
   