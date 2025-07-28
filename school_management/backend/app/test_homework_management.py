import unittest
import sys
import os
import datetime

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import homework_management
from models import Base, Homework, Course
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestHomeworkManagement(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        homework_management.session = self.session

        # Add a course to associate homework with
        self.course = Course(course_name='Math', course_code='M101')
        self.session.add(self.course)
        self.session.commit()

    def test_add_homework(self):
        due_date = datetime.date(2024, 8, 1)
        homework_management.add_homework(self.course.course_id, 'Test Homework', 'Test Description', due_date)
        homework = self.session.query(Homework).filter_by(title='Test Homework').first()
        self.assertIsNotNone(homework)
        self.assertEqual(homework.description, 'Test Description')

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

if __name__ == '__main__':
    unittest.main()
