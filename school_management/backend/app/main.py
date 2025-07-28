from flask import Flask, request, jsonify
from school_management import add_school, get_school, update_school, delete_school
from student_management import add_student, get_student, update_student, delete_student
from teacher_management import add_teacher, get_teacher, update_teacher, delete_teacher
from course_management import add_course, get_course, update_course, delete_course
from enrollment_management import enroll_student, get_enrollments_for_student, get_students_in_course, update_grade, unenroll_student
from homework_management import add_homework, get_homework_for_course, update_homework, delete_homework
from notification_management import create_notification, get_notifications_for_user, mark_notification_as_read
from announcement_management import create_announcement, get_all_announcements, update_announcement, delete_announcement
from id_card_generator import generate_id_card
from result_announcement import announce_result, get_results_for_student
from fee_management import create_fee_demand, get_fee_demands_for_student, record_payment, get_payment_history_for_student
from payment_gateways import instamojo_create_payment_request, razorpay_create_order

app = Flask(__name__)

# School routes
@app.route('/schools', methods=['POST'])
def create_school():
    data = request.get_json()
    school = add_school(data['name'], data['address'])
    return jsonify({'school_id': school.school_id}), 201

# Student routes
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = add_student(data['school_id'], data['first_name'], data['last_name'], data['email'], data['password'])
    return jsonify({'student_id': student.student_id}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def read_student(student_id):
    student = get_student(student_id)
    if student:
        return jsonify({
            'first_name': student.first_name,
            'last_name': student.last_name,
            'email': student.email
        })
    return jsonify({'message': 'Student not found'}), 404

# Teacher routes
# ... (similar routes for teachers)

# Course routes
# ... (similar routes for courses)

# Enrollment routes
# ... (similar routes for enrollments)

if __name__ == '__main__':
    app.run(debug=True)
