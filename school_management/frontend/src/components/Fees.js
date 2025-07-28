import React, { useState, useEffect } from 'react';

const Fees = () => {
  const [feeDemands, setFeeDemands] = useState([]);
  const [paymentHistory, setPaymentHistory] = useState([]);

  useEffect(() => {
    // In a real application, you would fetch this data from your backend API
    const dummyFeeDemands = [
      { id: 1, description: 'Tuition Fee', amount: 5000, due_date: '2024-08-15' },
      { id: 2, description: 'Bus Fee', amount: 1000, due_date: '2024-08-15' },
    ];
    const dummyPaymentHistory = [
      { id: 1, description: 'Tuition Fee - April', amount: 5000, date: '2024-04-10' },
    ];
    setFeeDemands(dummyFeeDemands);
    setPaymentHistory(dummyPaymentHistory);
  }, []);

  return (
    <div>
      <h2>Fee Demands</h2>
      <ul>
        {feeDemands.map(demand => (
          <li key={demand.id}>
            {demand.description}: {demand.amount} (Due: {demand.due_date})
            <button>Pay Now</button>
          </li>
        ))}
      </ul>

      <h2>Payment History</h2>
      <ul>
        {paymentHistory.map(payment => (
          <li key={payment.id}>
            {payment.description}: {payment.amount} (Paid on: {payment.date})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Fees;
