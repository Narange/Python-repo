import unittest
from employee import Employee


class EmployeeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("Set Up")
        self.empl_1 = Employee("Nico", "Fera", 50000)
        self.empl_2 = Employee("Denise", "Williams", 75000)

    def tearDown(self):
        print("Tear Down")

    def test_email(self):
        print("test_email")

        self.assertEqual(self.empl_1.email, "Nico.Fera@fakemail.com")
        self.assertEqual(self.empl_2.email, "Denise.Williams@fakemail.com")

        # Changing names, emails should reflect this
        self.empl_1.first = "Nicolas"
        self.empl_2.first = "Jane"

        self.assertEqual(self.empl_1.email, "Nicolas.Fera@fakemail.com")
        self.assertEqual(self.empl_2.email, "Jane.Williams@fakemail.com")

    def test_give_raise(self):
        print("test_give_raise")

        self.empl_1.give_raise()
        self.empl_2.give_raise()

        self.assertEqual(self.empl_1.pay, 55000)
        self.assertEqual(self.empl_2.pay, 82500)


if __name__ == "__main__":
    unittest.main()
