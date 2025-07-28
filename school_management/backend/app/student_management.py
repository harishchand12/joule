from models import Student, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# This is a global session, which is not ideal for testing.
# A better approach would be to use a session factory.
def get_session():
    return session

def add_student(school_id, first_name, last_name, email, password):
    """Adds a new student to the database."""
    new_student = Student(school_id=school_id, first_name=first_name, last_name=last_name, email=email)
    new_student.set_password(password)
    session.add(new_student)
    session.commit()
    return new_student

def get_student(student_id):
    """Retrieves a student by their ID."""
    return session.query(Student).filter_by(student_id=student_id).first()

def update_student(student_id, **kwargs):
    """Updates a student's information."""
    student = get_student(student_id)
    if student:
        for key, value in kwargs.items():
            setattr(student, key, value)
        session.commit()
    return student

def delete_student(student_id):
    """Deletes a student from the database."""
    student = get_student(student_id)
    if student:
        session.delete(student)
        session.commit()
        return True
    return False
