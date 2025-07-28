import React, { useState, useEffect } from 'react';

const Student = () => {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    const dummyStudents = [
      { id: 1, name: 'John Doe', email: 'john.doe@example.com' },
      { id: 2, name: 'Jane Smith', email: 'jane.smith@example.com' },
    ];
    setStudents(dummyStudents);
  }, []);

  return (
    <div>
      <h2>Students</h2>
      <ul>
        {students.map(student => (
          <li key={student.id}>{student.name} - {student.email}</li>
        ))}
      </ul>
    </div>
  );
};

export default Student;
