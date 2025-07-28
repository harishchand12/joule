import unittest
import sys
import os
import datetime

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import fee_management
from models import Base, FeeDemand, Payment, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestFeeManagement(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        fee_management.session = self.session

        # Add a student for testing
        self.student = Student(first_name='Test', last_name='Student', email='test.student@example.com')
        self.session.add(self.student)
        self.session.commit()

    def test_create_fee_demand(self):
        due_date = datetime.date(2024, 8, 15)
        fee_management.create_fee_demand(self.student.student_id, 'Test Fee', 100.00, due_date)
        demand = self.session.query(FeeDemand).filter_by(description='Test Fee').first()
        self.assertIsNotNone(demand)
        self.assertEqual(demand.amount, 100.00)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

if __name__ == '__main__':
    unittest.main()
