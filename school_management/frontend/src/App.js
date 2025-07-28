import React from 'react';
import './App.css';
import Student from './components/Student';
import Homework from './components/Homework';
import School from './components/School';
import Results from './components/Results';
import Fees from './components/Fees';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>School Management System</h1>
      </header>
      <main>
        <School />
        <Student />
        <Homework />
        <Results />
        <Fees />
      </main>
    </div>
  );
}

export default App;
