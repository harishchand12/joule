from models import Timetable, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_timetable_entry(class_id, day, start_time, end_time, subject, teacher_id):
    """Adds a new entry to the timetable."""
    new_entry = Timetable(class_id=class_id, day=day, start_time=start_time, end_time=end_time, subject=subject, teacher_id=teacher_id)
    session.add(new_entry)
    session.commit()
    return new_entry

def get_timetable_for_class(class_id):
    """Retrieves the timetable for a specific class."""
    return session.query(Timetable).filter_by(class_id=class_id).all()

def get_timetable_for_teacher(teacher_id):
    """Retrieves the timetable for a specific teacher."""
    return session.query(Timetable).filter_by(teacher_id=teacher_id).all()
