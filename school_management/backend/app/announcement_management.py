from models import Announcement, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_announcement(school_id, title, content):
    """Creates a new announcement for a specific school."""
    new_announcement = Announcement(school_id=school_id, title=title, content=content)
    session.add(new_announcement)
    session.commit()
    return new_announcement

def get_all_announcements():
    """Retrieves all announcements."""
    return session.query(Announcement).all()

def update_announcement(announcement_id, **kwargs):
    """Updates an announcement."""
    announcement = session.query(Announcement).filter_by(announcement_id=announcement_id).first()
    if announcement:
        for key, value in kwargs.items():
            setattr(announcement, key, value)
        session.commit()
    return announcement

def delete_announcement(announcement_id):
    """Deletes an announcement."""
    announcement = session.query(Announcement).filter_by(announcement_id=announcement_id).first()
    if announcement:
        session.delete(announcement)
        session.commit()
        return True
    return False
