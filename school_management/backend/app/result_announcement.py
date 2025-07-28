from models import Result, Base, Enrollment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def announce_result(enrollment_id, grade):
    """Announces the result for a student's enrollment."""
    # First, update the grade in the enrollments table
    enrollment = session.query(Enrollment).filter_by(enrollment_id=enrollment_id).first()
    if enrollment:
        enrollment.grade = grade
        session.commit()

        # Then, create a new result entry
        new_result = Result(enrollment_id=enrollment_id, grade=grade)
        session.add(new_result)
        session.commit()
        return new_result
    return None

def get_results_for_student(student_id):
    """Retrieves all announced results for a student."""
    return session.query(Result).join(Enrollment).filter(Enrollment.student_id == student_id).all()
