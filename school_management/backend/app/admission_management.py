from models import AdmissionInquiry, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def new_inquiry(student_name, parent_name, email, phone):
    """Creates a new admission inquiry."""
    new_inquiry = AdmissionInquiry(student_name=student_name, parent_name=parent_name, email=email, phone=phone)
    session.add(new_inquiry)
    session.commit()
    return new_inquiry

def get_all_inquiries():
    """Retrieves all admission inquiries."""
    return session.query(AdmissionInquiry).all()

def process_admission(inquiry_id, status):
    """Updates the status of an admission inquiry."""
    inquiry = session.query(AdmissionInquiry).filter_by(inquiry_id=inquiry_id).first()
    if inquiry:
        inquiry.status = status
        session.commit()
    return inquiry
