from models import Homework, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_homework(course_id, title, description, due_date):
    """Adds a new homework assignment to the database."""
    new_homework = Homework(course_id=course_id, title=title, description=description, due_date=due_date)
    session.add(new_homework)
    session.commit()
    return new_homework

def get_homework_for_course(course_id):
    """Retrieves all homework for a specific course."""
    return session.query(Homework).filter_by(course_id=course_id).all()

def update_homework(homework_id, **kwargs):
    """Updates a homework assignment's information."""
    homework = session.query(Homework).filter_by(homework_id=homework_id).first()
    if homework:
        for key, value in kwargs.items():
            setattr(homework, key, value)
        session.commit()
    return homework

def delete_homework(homework_id):
    """Deletes a homework assignment from the database."""
    homework = session.query(Homework).filter_by(homework_id=homework_id).first()
    if homework:
        session.delete(homework)
        session.commit()
        return True
    return False
