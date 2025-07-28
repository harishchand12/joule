from models import Exam, ExamResult, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def schedule_exam(course_id, exam_name, date):
    """Schedules a new exam."""
    new_exam = Exam(course_id=course_id, exam_name=exam_name, date=date)
    session.add(new_exam)
    session.commit()
    return new_exam

def record_exam_result(exam_id, student_id, marks):
    """Records the result for a student's exam."""
    new_result = ExamResult(exam_id=exam_id, student_id=student_id, marks=marks)
    session.add(new_result)
    session.commit()
    return new_result

def get_exams_for_course(course_id):
    """Retrieves all exams for a course."""
    return session.query(Exam).filter_by(course_id=course_id).all()

def get_results_for_exam(exam_id):
    """Retrieves all results for an exam."""
    return session.query(ExamResult).filter_by(exam_id=exam_id).all()
