import unittest
from main import add_student, search_student, delete_student, students

class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        students.clear()

    def test_add_student(self):
        result = add_student("SYS001", "Juan", "BSIT")
        self.assertEqual(result, "Student added successfully!")

    def test_search_student(self):
        add_student("SYS002", "Maria", "BSCS")
        self.assertEqual(
            search_student("SYS002")["name"], "Maria"
        )

    def test_delete_student(self):
        add_student("SYS003", "Pedro", "BSIT")
        delete_student("SYS003")
        self.assertIsNone(search_student("SYS003"))

if __name__ == "__main__":
    unittest.main()
