from models import Notification, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_notification(user_id, message):
    """Creates a new notification for a user."""
    new_notification = Notification(user_id=user_id, message=message)
    session.add(new_notification)
    session.commit()
    return new_notification

def get_notifications_for_user(user_id):
    """Retrieves all unread notifications for a user."""
    return session.query(Notification).filter_by(user_id=user_id, is_read=False).all()

def mark_notification_as_read(notification_id):
    """Marks a notification as read."""
    notification = session.query(Notification).filter_by(notification_id=notification_id).first()
    if notification:
        notification.is_read = True
        session.commit()
    return notification
