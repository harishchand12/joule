import unittest
import sys
import os
import datetime

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import result_announcement
from models import Base, Result, Enrollment, Student, Course
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestResultAnnouncement(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        result_announcement.session = self.session

        # Add a student, course, and enrollment for testing
        self.student = Student(first_name='Test', last_name='Student', email='test.student@example.com')
        self.course = Course(course_name='Test Course', course_code='T101')
        self.session.add_all([self.student, self.course])
        self.session.commit()
        self.enrollment = Enrollment(student_id=self.student.student_id, course_id=self.course.course_id, enrollment_date=datetime.date.today())
        self.session.add(self.enrollment)
        self.session.commit()

    def test_announce_result(self):
        result_announcement.announce_result(self.enrollment.enrollment_id, 'A')
        result = self.session.query(Result).filter_by(enrollment_id=self.enrollment.enrollment_id).first()
        self.assertIsNotNone(result)
        self.assertEqual(result.grade, 'A')

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

if __name__ == '__main__':
    unittest.main()
