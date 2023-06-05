from django.test import TestCase
from scholarships.models import Scholarship

class ScholarshipTest(TestCase):
     def setUp(self):
        scholarship = Scholarship()
        return scholarship
     
     def test_scenario_1(self):
        try:
            scholarship = self.setUp()
        except:
            print("Scholarship object didn't create")
        
     def test_scenario_2(self):
            scholarship = self.setUp()
            scholarship.stratum = 5
            scholarship.motivational_letter = "Hola, me gustaria tener beca."
            scholarship.value_period = 15000
            scholarship.icfes_score = 420
            scholarship.period_current = 6
            scholarship.program_adm = "Ingeniería de Sistemas"
            scholarship.application_type = 'A'
            scholarship.state = 'P'
            scholarship.total_periods = 10
            scholarship.active = 'AC'

            self.assertEqual(scholarship.motivational_letter,"Hola, me gustaria tener beca.")

     def test_scenario_3(self):
            scholarship = self.setUp()
            scholarship.stratum = 1
            scholarship.motivational_letter = "Hola, me quisiera hacer parte de estos programas y desarrollarme integramente  ."
            scholarship.value_period = 20000
            scholarship.icfes_score = 350
            scholarship.period_current = 1
            scholarship.program_adm = "Ingeniería de Sistemas"
            scholarship.application_type = 'NI'
            scholarship.state = 'P'
            scholarship.total_periods = 10
            scholarship.active = 'AC'

            
            self.assertNotEqual(scholarship.stratum, 4)

     def test_scenario_4(self):
            scholarship = self.setUp()
            scholarship.stratum = 2
            scholarship.motivational_letter = "Hi, I'm Jenne and I would like to make part of this."
            scholarship.value_period = 23500
            scholarship.icfes_score = 189
            scholarship.period_current = 4
            scholarship.program_adm = "Psicología"
            scholarship.application_type = 'A'
            scholarship.state = 'A'
            scholarship.total_periods = 10
            scholarship.active = 'AC'

            
            self.assertEqual(scholarship.icfes_score, 189)
        
     def test_scenario_5(self):
            scholarship = self.setUp()
            scholarship.stratum = 3
            scholarship.motivational_letter = "Quiero una beca."
            scholarship.value_period = 12000000
            scholarship.icfes_score = 207
            scholarship.period_current = 1
            scholarship.program_adm = "Enfermería"
            scholarship.application_type = 'NI'
            scholarship.state = 'A'
            scholarship.total_periods = 4
            scholarship.active = 'AC'

            
            self.assertNotEqual(scholarship.period_current, 3)

     
     def test_scenario_6(self):
            scholarship = self.setUp()
            scholarship.stratum = 1
            scholarship.motivational_letter = "Me gustaría se becado."
            scholarship.value_period = 9750000
            scholarship.icfes_score = 462
            scholarship.period_current = 9
            scholarship.program_adm = "Medicina"
            scholarship.application_type = 'A'
            scholarship.state = 'A'
            scholarship.total_periods = 12
            scholarship.active = 'AC'

            
            self.assertEqual(scholarship.program_adm, "Medicina")         


     def test_scenario_7(self):
            scholarship = self.setUp()
            scholarship.stratum = 5
            scholarship.motivational_letter = "Mi primo tiene beca asi que yo tambien quiero."
            scholarship.value_period = 1130000
            scholarship.icfes_score = 268
            scholarship.period_current = 1
            scholarship.program_adm = "Comunicaciones"
            scholarship.application_type = 'NI'
            scholarship.state = 'R'
            scholarship.total_periods = 8
            scholarship.active = 'IN'

            
            self.assertNotEqual(scholarship.total_periods, 10)       

            