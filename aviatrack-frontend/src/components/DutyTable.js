import React, { useEffect, useState } from 'react';
import axios from 'axios';

const LogsTable = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_API_URL}/get-duties`);


      setLogs(response.data);
    } catch (error) {
      console.error('Error fetching logs:', error);
    }
  };

  return (
    <div style={{ marginTop: '40px' }}>
      <h2>Logged Pilot Duties</h2>
      {logs.length === 0 ? (
        <p>No logs found.</p>
      ) : (
        <table border="1" cellPadding="8" style={{ margin: 'auto' }}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Pilot ID</th>
              <th>Flight ID</th>
              <th>Duty Start</th>
              <th>Duty End</th>
              <th>Duration (hrs)</th>
              <th>Status</th>

            </tr>
          </thead>
          <tbody>
            {logs.map((log) => (
              <tr key={log.id} style={{ backgroundColor: log.is_violation ? 'red' : 'white' }}>

                <td>{log.id}</td>
                <td>{log.pilot_id}</td>
                <td>{log.flight_id}</td>
                <td>{new Date(log.duty_start).toLocaleString()}</td>
                <td>{new Date(log.duty_end).toLocaleString()}</td>
                <td>{log.duration_hours}</td>
                <td>
                  {log.is_violation ? <strong>🚨 Violation</strong> : '✅ Safe'}
                </td>

              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default LogsTable;
