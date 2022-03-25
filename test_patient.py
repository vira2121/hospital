import unittest
import sqlite3

class Patients(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect("Hospital.db")
        self.id = "3"
        self.name = "Ankur"
    def tearDown(self):
        self.id = "0"
        self.name = ""
        self.connection.close()

    def test_pat1(self):
        result = self.connection.execute("SELECT Name FROM patient WHERE PatientCode="+self.id)
        for i in result:
            fetchname = i[0]
        self.assertEqual(fetchname, self.name)


if __name__ == "__main__":
    unittest.main()