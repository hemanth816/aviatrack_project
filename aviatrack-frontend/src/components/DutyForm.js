import React, { useState } from 'react';
import axios from 'axios';

const DutyForm = () => {
  const [formData, setFormData] = useState({
    pilot_id: '',
    flight_id: '',
    duty_start: '',
    duty_end: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    const { pilot_id, flight_id, duty_start, duty_end } = formData;
  
    // ✅ Empty field validation
    if (!pilot_id || !flight_id || !duty_start || !duty_end) {
      alert("All fields are required.");
      return;
    }
  
    // ✅ Time validation
    if (new Date(duty_end) <= new Date(duty_start)) {
      alert("Duty end time must be after duty start time.");
      return;
    }
  
    try {
      const res = await axios.post(`${process.env.REACT_APP_API_URL}/log-duty`, formData);

      alert(res.data.message || 'Logged successfully');
      setFormData({ pilot_id: '', flight_id: '', duty_start: '', duty_end: '' });
    } catch (err) {
      alert('Failed to log duty!');
      console.error(err);
    }
  };
  

  return (
    <form onSubmit={handleSubmit}>
      <h2>Log Duty</h2>
      <input type="text" name="pilot_id" placeholder="Pilot ID" value={formData.pilot_id} onChange={(e) => 
      setFormData({ ...formData, pilot_id: e.target.value.toUpperCase() }) } required />

      <br />
      <input type="text" name="flight_id" placeholder="Flight ID" value={formData.flight_id} onChange={handleChange} required />
      <br />
      <input type="datetime-local" name="duty_start" value={formData.duty_start} onChange={handleChange} required />
      <br />
      <input type="datetime-local" name="duty_end" value={formData.duty_end} onChange={handleChange} required />
      <br />
      <button type="submit">Submit</button>
    </form>
  );
};

export default DutyForm;
