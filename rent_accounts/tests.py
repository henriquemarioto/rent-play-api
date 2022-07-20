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

    @classmethod    
    def setUpTestData(cls) -> None:
        #CRIAR SUPER USER
        cls.super_user = {
            "nickname": "Admin",
            "first_name": "Admin",
            "last_name":  "Admin",
            "password": "12345678",
            "cellphone": "55999999991",
            "email": "admin@rentandplay.com.br"
        }
        cls.admin = User.objects.create_superuser(**cls.super_user) 

        #CRIAR USER 1
        cls.tester1_data = {
            "nickname" : "Tester1",
            "first_name" : "Tester1",
            "last_name" : "Anonimous",
            "cellphone" : "12345678916",
            "email" : "tester1@email.com",
            "password" : "123456",
        }

        cls.tester1 = User.objects.create_user(**cls.tester1_data) 

        #CRIAR USER 2
        cls.tester2_data = {
            "nickname" : "Tester2",
            "first_name" : "Tester2",
            "last_name" : "Anonimous",
            "cellphone" : "12345678915",
            "email" : "tester2@email.com",
            "password" : "123456"
        }

        cls.tester2 = User.objects.create_user(**cls.tester2_data)

       
        # BUSCAR PLATAFORMAS 
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

    #TESTE ATRIBUTOS MODEL RENT_ACCOUNT
    def test_attr_(self):         
        for item in self.platforms:
            self.games[0].platforms.add(item)
        for item in self.games:
            self.rent_account.games.add(item)        
        self.assertEquals(self.rent_account.login, self.rent_account_data["login"])
        self.assertEquals(self.rent_account.password, self.rent_account_data["password"])
        self.assertEquals(self.rent_account.price_per_day, self.rent_account_data["price_per_day"])
        self.assertEquals(self.rent_account.platform, self.rent_account_data["platform"])
        self.assertEquals(self.rent_account.owner, self.rent_account_data["owner"])
        self.assertEquals(len(self.games), self.rent_account.games.count())       

    
    # LOGIN USERS
    def test_login_user(self):       
        
        res = self.client.post("/login/", data={"email": self.tester2_data.get("email"), "password": self.tester2_data.get("password")})
        token = Token.objects.get(user=self.tester2) 

        res1 = self.client.post("/login/", data={"email": self.tester1_data.get("email"), "password": self.tester1_data.get("password")})
        token1 = Token.objects.get(user=self.tester1) 


       
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

    def test_update_user_wallet(self):
        self.client.force_authenticate(user=self.tester1)
        wallet = {"wallet": 500.00}
        response = self.client.patch(f"/users/{self.tester1.id}/", data=wallet, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)  



       
    def test_create_rents_history(self):
        self.tester1.wallet = 500
        self.client.force_authenticate(user=self.tester1)        
        account = self.rent_account.id       
       
        rents_days = {
            "rented_days": 3
        }        

        response = self.client.patch(f"/rent_accounts/{account}/rent/", data=rents_days, format='json')      
        

        self.assertEqual(response.status_code, status.HTTP_200_OK)  
   
    def test_list_rents_history(self):
        self.client.force_authenticate(user=self.tester2)
        response = self.client.get("/rent_histories/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)
    

    def test_list_rents_history_by_owner(self):
        self.client.force_authenticate(user=self.tester1)           
        response = self.client.get(f"/rent_histories/owner/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_list_rents_history_by_owner(self):
        self.client.force_authenticate(user=self.tester2)           
        response = self.client.get(f"/rent_histories/rented/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)