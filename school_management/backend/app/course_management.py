from models import Course, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_course(school_id, course_name, course_code, teacher_id):
    """Adds a new course to the database."""
    new_course = Course(school_id=school_id, course_name=course_name, course_code=course_code, teacher_id=teacher_id)
    session.add(new_course)
    session.commit()
    return new_course

def get_course(course_id):
    """Retrieves a course by its ID."""
    return session.query(Course).filter_by(course_id=course_id).first()

def update_course(course_id, **kwargs):
    """Updates a course's information."""
    course = get_course(course_id)
    if course:
        for key, value in kwargs.items():
            setattr(course, key, value)
        session.commit()
    return course

def delete_course(course_id):
    """Deletes a course from the database."""
    course = get_course(course_id)
    if course:
        session.delete(course)
        session.commit()
        return True
    return False
