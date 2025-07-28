from models import Enrollment, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def enroll_student(student_id, course_id):
    """Enrolls a student in a course."""
    new_enrollment = Enrollment(student_id=student_id, course_id=course_id, enrollment_date=datetime.date.today())
    session.add(new_enrollment)
    session.commit()
    return new_enrollment

def get_enrollments_for_student(student_id):
    """Retrieves all enrollments for a specific student."""
    return session.query(Enrollment).filter_by(student_id=student_id).all()

def get_students_in_course(course_id):
    """Retrieves all students enrolled in a specific course."""
    return session.query(Enrollment).filter_by(course_id=course_id).all()

def update_grade(enrollment_id, grade):
    """Updates the grade for a student's enrollment."""
    enrollment = session.query(Enrollment).filter_by(enrollment_id=enrollment_id).first()
    if enrollment:
        enrollment.grade = grade
        session.commit()
    return enrollment

def unenroll_student(enrollment_id):
    """Unenrolls a student from a course."""
    enrollment = session.query(Enrollment).filter_by(enrollment_id=enrollment_id).first()
    if enrollment:
        session.delete(enrollment)
        session.commit()
        return True
    return False
