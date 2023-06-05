from django.contrib.auth import get_user_model
from django.test import TestCase
from users.models import User

    
class UserTest(TestCase):
     def setUp1(self):
        user = User()
        return user
     
     def setUp2(self):
        user =  User.objects.create_user(email="esteban@gmail.com",name="Esteban Romero", idType = 2, numID=1234567890, role=3)
        return user
     def test_scenario_1(self):
        try:
            user = self.setUp1()
        except:
            print("User object didn't create")
            self.assertEqual(user.email,"")
        
     def test_scenario_2(self):
            user = self.setUp1()
            user.email = "john@example.com"
            user.password = "johndoe1"
            user.name = "John Doe"
            user.idType = 1
            user.numID = "112508374"
            user.role = 1

            self.assertEqual(user.email,"john@example.com")

     def test_scenario_3(self):
            user = self.setUp1()
            self.assertEqual(user.email,"")
            user.email = "test@test.com"
            user.password = "janesmith"
            user.name = "Jane Smith"
            user.idType = 1
            user.numID = "1234567890"
            user.role = 1

            self.assertNotEqual(user.email,"john@example.com")

     def test_scenario_4(self):
         user = self.setUp2()
         user.email = "romero123@gmail.com"
         self.assertNotEqual(user.email, "esteban@gmail.com")

       

