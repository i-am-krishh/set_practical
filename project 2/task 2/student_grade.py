import unittest

class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_student(self, name):
        if name in self.grades:
            raise ValueError(f"Student {name} already exists.")
        self.grades[name] = []

    def add_grade(self, name, grade):
        if name not in self.grades:
            raise ValueError(f"Student {name} does not exist.")
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grades[name].append(grade)

    def get_average(self, name):
        if name not in self.grades:
            raise ValueError(f"Student {name} does not exist.")
        if not self.grades[name]:
            return 0
        return sum(self.grades[name]) / len(self.grades[name])

    def remove_student(self, name):
        if name not in self.grades:
            raise ValueError(f"Student {name} does not exist.")
        del self.grades[name]

# Test Cases
class TestStudentGrades(unittest.TestCase):
    def setUp(self):
        """Test data setup method."""
        self.grades = StudentGrades()
        self.grades.add_student("Alice")
        self.grades.add_student("Bob")
        self.grades.add_grade("Alice", 85)
        self.grades.add_grade("Alice", 90)
        self.grades.add_grade("Bob", 78)

    def test_add_student(self):
        self.grades.add_student("Charlie")
        self.assertIn("Charlie", self.grades.grades)

    def test_add_existing_student(self):
        with self.assertRaises(ValueError):
            self.grades.add_student("Alice")

    def test_add_grade(self):
        self.grades.add_grade("Bob", 88)
        self.assertIn(88, self.grades.grades["Bob"])

    def test_add_grade_invalid(self):
        with self.assertRaises(ValueError):
            self.grades.add_grade("Bob", 150)

    def test_get_average(self):
        self.assertAlmostEqual(self.grades.get_average("Alice"), 87.5)

    def test_get_average_empty(self):
        self.grades.add_student("Charlie")
        self.assertEqual(self.grades.get_average("Charlie"), 0)

    def test_remove_student(self):
        self.grades.remove_student("Bob")
        self.assertNotIn("Bob", self.grades.grades)

    def test_remove_nonexistent_student(self):
        with self.assertRaises(ValueError):
            self.grades.remove_student("Charlie")

if __name__ == "__main__":
    unittest.main()
