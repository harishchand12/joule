import React, { useState, useEffect } from 'react';

const School = () => {
  const [schools, setSchools] = useState([]);

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    const dummySchools = [
      { id: 1, name: 'Greenwood High' },
      { id: 2, name: 'Oakridge International' },
    ];
    setSchools(dummySchools);
  }, []);

  return (
    <div>
      <h2>Schools</h2>
      <ul>
        {schools.map(school => (
          <li key={school.id}>{school.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default School;
