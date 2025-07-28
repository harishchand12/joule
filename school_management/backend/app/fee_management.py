from models import FeeDemand, Payment, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_fee_demand(student_id, description, amount, due_date):
    """Creates a new fee demand for a student."""
    new_demand = FeeDemand(student_id=student_id, description=description, amount=amount, due_date=due_date)
    session.add(new_demand)
    session.commit()
    return new_demand

def get_fee_demands_for_student(student_id):
    """Retrieves all unpaid fee demands for a student."""
    return session.query(FeeDemand).filter_by(student_id=student_id, is_paid=False).all()

def record_payment(demand_id, amount, payment_gateway, transaction_id):
    """Records a payment for a fee demand."""
    demand = session.query(FeeDemand).filter_by(demand_id=demand_id).first()
    if demand:
        demand.is_paid = True
        new_payment = Payment(demand_id=demand_id, amount=amount, payment_gateway=payment_gateway, transaction_id=transaction_id)
        session.add(new_payment)
        session.commit()
        return new_payment
    return None

def get_payment_history_for_student(student_id):
    """Retrieves the payment history for a student."""
    return session.query(Payment).join(FeeDemand).filter(FeeDemand.student_id == student_id).all()
