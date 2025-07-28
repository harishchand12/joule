import unittest
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import student_management
from models import Base, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        student_management.session = self.session


    def test_add_student(self):
        student_management.add_student('Test', 'User', 'test.user@example.com', 'password')
        student = self.session.query(Student).filter_by(email='test.user@example.com').first()
        self.assertIsNotNone(student)
        self.assertEqual(student.first_name, 'Test')

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

if __name__ == '__main__':
    unittest.main()
