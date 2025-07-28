from models import Teacher, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_teacher(school_id, first_name, last_name, email, password):
    """Adds a new teacher to the database."""
    new_teacher = Teacher(school_id=school_id, first_name=first_name, last_name=last_name, email=email)
    new_teacher.set_password(password)
    session.add(new_teacher)
    session.commit()
    return new_teacher

def get_teacher(teacher_id):
    """Retrieves a teacher by their ID."""
    return session.query(Teacher).filter_by(teacher_id=teacher_id).first()

def update_teacher(teacher_id, **kwargs):
    """Updates a teacher's information."""
    teacher = get_teacher(teacher_id)
    if teacher:
        for key, value in kwargs.items():
            setattr(teacher, key, value)
        session.commit()
    return teacher

def delete_teacher(teacher_id):
    """Deletes a teacher from the database."""
    teacher = get_teacher(teacher_id)
    if teacher:
        session.delete(teacher)
        session.commit()
        return True
    return False
