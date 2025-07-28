import React, { useState, useEffect } from 'react';

const Results = () => {
  const [results, setResults] = useState([]);

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    const dummyResults = [
      { id: 1, course: 'Math', grade: 'A' },
      { id: 2, course: 'History', grade: 'B' },
    ];
    setResults(dummyResults);
  }, []);

  return (
    <div>
      <h2>Results</h2>
      <ul>
        {results.map(result => (
          <li key={result.id}>{result.course}: {result.grade}</li>
        ))}
      </ul>
    </div>
  );
};

export default Results;
