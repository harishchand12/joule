import unittest
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import school_management
from models import Base, School
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestSchoolManagement(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
        school_management.session = self.session

    def test_add_school(self):
        school_management.add_school('Test School', '123 Test St')
        school = self.session.query(School).filter_by(name='Test School').first()
        self.assertIsNotNone(school)
        self.assertEqual(school.address, '123 Test St')

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

if __name__ == '__main__':
    unittest.main()
