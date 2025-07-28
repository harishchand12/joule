from models import School, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_school(name, address):
    """Adds a new school to the database."""
    new_school = School(name=name, address=address)
    session.add(new_school)
    session.commit()
    return new_school

def get_school(school_id):
    """Retrieves a school by its ID."""
    return session.query(School).filter_by(school_id=school_id).first()

def update_school(school_id, **kwargs):
    """Updates a school's information."""
    school = get_school(school_id)
    if school:
        for key, value in kwargs.items():
            setattr(school, key, value)
        session.commit()
    return school

def delete_school(school_id):
    """Deletes a school from the database."""
    school = get_school(school_id)
    if school:
        session.delete(school)
        session.commit()
        return True
    return False
