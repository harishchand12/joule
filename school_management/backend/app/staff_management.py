from models import Teacher, StaffAttendance, Payroll, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def record_staff_attendance(teacher_id, date, is_present):
    """Records attendance for a staff member."""
    new_attendance = StaffAttendance(teacher_id=teacher_id, date=date, is_present=is_present)
    session.add(new_attendance)
    session.commit()
    return new_attendance

def generate_payroll(teacher_id, salary, month, year):
    """Generates a payroll record for a staff member."""
    new_payroll = Payroll(teacher_id=teacher_id, salary=salary, month=month, year=year)
    session.add(new_payroll)
    session.commit()
    return new_payroll

def get_staff_attendance(teacher_id):
    """Retrieves attendance records for a staff member."""
    return session.query(StaffAttendance).filter_by(teacher_id=teacher_id).all()

def get_payroll_for_staff(teacher_id):
    """Retrieves payroll records for a staff member."""
    return session.query(Payroll).filter_by(teacher_id=teacher_id).all()
