from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Text, Boolean, DateTime, Numeric, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from auth import hash_password
import datetime

Base = declarative_base()

class School(Base):
    __tablename__ = 'schools'
    school_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255))

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('schools.school_id'))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date)
    email = Column(String(100), unique=True)
    phone_number = Column(String(20))
    address = Column(String(255))
    password_hash = Column(String(128))

    def set_password(self, password):
        self.password_hash = hash_password(password)

class Homework(Base):
    __tablename__ = 'homework'
    homework_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    title = Column(String(100), nullable=False)
    description = Column(Text)
    due_date = Column(Date)
    course = relationship("Course")

class Notification(Base):
    __tablename__ = 'notifications'
    notification_id = Column(Integer, primary_key=True)
    user_id = Column(Integer) # Can be student_id or teacher_id
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Announcement(Base):
    __tablename__ = 'announcements'
    announcement_id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('schools.school_id'))
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Result(Base):
    __tablename__ = 'results'
    result_id = Column(Integer, primary_key=True)
    enrollment_id = Column(Integer, ForeignKey('enrollments.enrollment_id'))
    grade = Column(String(2))
    announced_at = Column(DateTime, default=datetime.datetime.utcnow)
    enrollment = relationship("Enrollment")

class FeeDemand(Base):
    __tablename__ = 'fee_demands'
    demand_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    description = Column(String(255))
    amount = Column(Numeric(10, 2))
    due_date = Column(Date)
    is_paid = Column(Boolean, default=False)
    student = relationship("Student")

class Payment(Base):
    __tablename__ = 'payments'
    payment_id = Column(Integer, primary_key=True)
    demand_id = Column(Integer, ForeignKey('fee_demands.demand_id'))
    amount = Column(Numeric(10, 2))
    payment_gateway = Column(String(50))
    transaction_id = Column(String(100))
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)
    demand = relationship("FeeDemand")

class StaffAttendance(Base):
    __tablename__ = 'staff_attendance'
    attendance_id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    date = Column(Date)
    is_present = Column(Boolean)
    teacher = relationship("Teacher")

class Payroll(Base):
    __tablename__ = 'payroll'
    payroll_id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    salary = Column(Numeric(10, 2))
    month = Column(Integer)
    year = Column(Integer)
    is_paid = Column(Boolean, default=False)
    teacher = relationship("Teacher")

class AdmissionInquiry(Base):
    __tablename__ = 'admission_inquiries'
    inquiry_id = Column(Integer, primary_key=True)
    student_name = Column(String(100))
    parent_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    status = Column(String(20), default='pending')

class Timetable(Base):
    __tablename__ = 'timetable'
    timetable_id = Column(Integer, primary_key=True)
    class_id = Column(Integer) # Assuming a classes table exists
    day = Column(String(10))
    start_time = Column(Time)
    end_time = Column(Time)
    subject = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    teacher = relationship("Teacher")

class Exam(Base):
    __tablename__ = 'exams'
    exam_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    exam_name = Column(String(100))
    date = Column(Date)
    course = relationship("Course")

class ExamResult(Base):
    __tablename__ = 'exam_results'
    result_id = Column(Integer, primary_key=True)
    exam_id = Column(Integer, ForeignKey('exams.exam_id'))
    student_id = Column(Integer, ForeignKey('students.student_id'))
    marks = Column(Numeric(5, 2))
    exam = relationship("Exam")
    student = relationship("Student")

class Teacher(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('schools.school_id'))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)
    phone_number = Column(String(20))
    bio = Column(Text)
    password_hash = Column(String(128))

    def set_password(self, password):
        self.password_hash = hash_password(password)

class Course(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('schools.school_id'))
    course_name = Column(String(100), nullable=False)
    course_code = Column(String(20), unique=True)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    teacher = relationship("Teacher")

class Enrollment(Base):
    __tablename__ = 'enrollments'
    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    enrollment_date = Column(Date)
    grade = Column(String(2))
    student = relationship("Student")
    course = relationship("Course")

class Admin(Base):
    __tablename__ = 'admins'
    admin_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128))

    def set_password(self, password):
        self.password_hash = hash_password(password)
