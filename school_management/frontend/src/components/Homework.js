import React, { useState, useEffect } from 'react';

const Homework = () => {
  const [homework, setHomework] = useState([]);

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    const dummyHomework = [
      { id: 1, title: 'Math Homework', description: 'Complete exercises 1-5', due_date: '2024-08-01' },
      { id: 2, title: 'History Reading', description: 'Read chapter 3', due_date: '2024-08-03' },
    ];
    setHomework(dummyHomework);
  }, []);

  return (
    <div>
      <h2>Homework</h2>
      <ul>
        {homework.map(hw => (
          <li key={hw.id}>
            <strong>{hw.title}</strong> (Due: {hw.due_date})
            <p>{hw.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Homework;
