import React, { useEffect, useState } from 'react';
import axios from 'axios';

const BlockchainLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/blockchain-logs');
      setLogs(response.data.logs);
    } catch (error) {
      console.error('Error fetching blockchain logs:', error);
    }
  };

  return (
    <div style={{ marginTop: '40px' }}>
      <h2>📒 Blockchain Ledger</h2>
      {logs.length === 0 ? (
        <p>No blockchain entries yet.</p>
      ) : (
        <table border="1" cellPadding="8" style={{ margin: 'auto' }}>
          <thead>
            <tr>
              <th>Pilot ID</th>
              <th>Flight ID</th>
              <th>Duty Start</th>
              <th>Duty End</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((log, index) => (
              <tr key={index}>
                <td>{log.pilot_id}</td>
                <td>{log.flight_id}</td>
                <td>{new Date(log.duty_start).toLocaleString()}</td>
                <td>{new Date(log.duty_end).toLocaleString()}</td>
                <td>{new Date(log.timestamp).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default BlockchainLogs;
