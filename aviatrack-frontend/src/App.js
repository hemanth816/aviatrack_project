import React from 'react';
import DutyForm from './components/DutyForm';
import LogsTable from './components/DutyTable';
import BlockchainLogs from './components/BlockchainLogs';


function App() {
  return (
    <div className="App" style={{ textAlign: 'center', marginTop: '40px' }}>
      <h1>Aviatrack - Pilot Duty Log</h1>
      <DutyForm />
      <LogsTable />
      <BlockchainLogs />

    </div>
  );
}


export default App;
