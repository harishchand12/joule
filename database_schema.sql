-- Schools Table
CREATE TABLE schools (
    school_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255)
);

-- Students Table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    school_id INT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    FOREIGN KEY (school_id) REFERENCES schools(school_id)
);

-- Teachers Table
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    school_id INT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    bio TEXT,
    FOREIGN KEY (school_id) REFERENCES schools(school_id)
);

-- Courses Table
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    school_id INT,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    teacher_id INT,
    FOREIGN KEY (school_id) REFERENCES schools(school_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Enrollments Table
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Homework Table
CREATE TABLE homework (
    homework_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    due_date DATE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Notifications Table
CREATE TABLE notifications (
    notification_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT, -- Can be student_id or teacher_id
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Announcements Table
CREATE TABLE announcements (
    announcement_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Results Table
CREATE TABLE results (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT,
    grade VARCHAR(2),
    announced_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);

-- Fee Demands Table
CREATE TABLE fee_demands (
    demand_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    description VARCHAR(255),
    amount DECIMAL(10, 2),
    due_date DATE,
    is_paid BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Payments Table
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    demand_id INT,
    amount DECIMAL(10, 2),
    payment_gateway VARCHAR(50), -- e.g., 'instamojo', 'razorpay'
    transaction_id VARCHAR(100),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (demand_id) REFERENCES fee_demands(demand_id)
);

-- Staff Attendance Table
CREATE TABLE staff_attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_id INT,
    date DATE,
    is_present BOOLEAN,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Payroll Table
CREATE TABLE payroll (
    payroll_id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_id INT,
    salary DECIMAL(10, 2),
    month INT,
    year INT,
    is_paid BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Admission Inquiries Table
CREATE TABLE admission_inquiries (
    inquiry_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100),
    parent_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    status VARCHAR(20) DEFAULT 'pending' -- e.g., pending, accepted, rejected
);

-- Timetable Table
CREATE TABLE timetable (
    timetable_id INT PRIMARY KEY AUTO_INCREMENT,
    class_id INT, -- Assuming a classes table exists
    day VARCHAR(10), -- e.g., Monday, Tuesday
    start_time TIME,
    end_time TIME,
    subject VARCHAR(50),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Exams Table
CREATE TABLE exams (
    exam_id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    exam_name VARCHAR(100),
    date DATE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Exam Results Table
CREATE TABLE exam_results (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    exam_id INT,
    student_id INT,
    marks DECIMAL(5, 2),
    FOREIGN KEY (exam_id) REFERENCES exams(exam_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
