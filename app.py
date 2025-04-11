from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from models import init_db
import sqlite3

from collections import defaultdict
from datetime import datetime, timedelta

import os
import json



app = Flask(__name__)
CORS(app)
init_db()


# Home route (optional)
@app.route('/')
def home():
    return render_template('index.html')  # This needs a templates/index.html file

# POST route to log pilot duty
@app.route('/log-duty', methods=['POST'])
def log_duty():
    data = request.json
    print("Received duty log:", data)

    try:
        pilot_id = data.get('pilot_id')
        flight_id = data.get('flight_id')
        duty_start = data.get('duty_start')
        duty_end = data.get('duty_end')

        # Save to DB
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""
            INSERT INTO duty_logs (pilot_id, flight_id, duty_start, duty_end)
            VALUES (?, ?, ?, ?)
        """, (pilot_id, flight_id, duty_start, duty_end))
        conn.commit()
        conn.close()

        # Compute duration and violation
        start_dt = datetime.fromisoformat(duty_start)
        end_dt = datetime.fromisoformat(duty_end)
        duration = end_dt - start_dt
        violation = duration > timedelta(hours=10)

        # Blockchain part
        from blockchain import Blockchain
        blockchain = Blockchain()
        blockchain.load_chain("blockchain_ledger.json")

        block_data = {
            "pilot_id": pilot_id,
            "flight_id": flight_id,
            "duty_start": duty_start,
            "duty_end": duty_end,
            "duration_hours": round(duration.total_seconds() / 3600, 2),
            "violation": violation
        }

        blockchain.add_block(block_data)
        blockchain.save_chain("blockchain_ledger.json")

        return jsonify({
            "status": "Success",
            "message": "Duty logged and blockchain updated"
        })

    except Exception as e:
        print("❌ ERROR in /log-duty:", str(e))
        return jsonify({
            "status": "Error",
            "message": f"Failed to log duty: {str(e)}"
        }), 500







@app.route('/get-logs', methods=['GET'])
def get_logs():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM duty_logs")
    rows = c.fetchall()
    conn.close()

    logs = []
    for row in rows:
        logs.append({
            'id': row[0],
            'pilot_id': row[1],
            'flight_id': row[2],
            'duty_start': row[3],
            'duty_end': row[4]
        })

    return jsonify({
        'status': 'Success',
        'logs': logs
    })


@app.route('/get-duties', methods=['GET'])
def get_duties():
    conn = sqlite3.connect('database.db')  # ✅ match log route
    c = conn.cursor()
    c.execute('SELECT * FROM duty_logs')   # ✅ match log table
    duties = c.fetchall()
    conn.close()

    # Organize duties per pilot per day
    from collections import defaultdict
    from datetime import datetime, timedelta

    pilot_day_durations = defaultdict(timedelta)
    results = []

    for row in duties:
        id_, pilot_id, flight_id, duty_start, duty_end = row
        start_dt = datetime.fromisoformat(duty_start)
        end_dt = datetime.fromisoformat(duty_end)
        duration = end_dt - start_dt
        duty_date = start_dt.date()

        key = (pilot_id, duty_date)
        pilot_day_durations[key] += duration

        results.append({
            "id": id_,
            "pilot_id": pilot_id,
            "flight_id": flight_id,
            "duty_start": duty_start,
            "duty_end": duty_end,
            "duration_hours": round(duration.total_seconds() / 3600, 2),
            "is_violation": pilot_day_durations[key] > timedelta(hours=10)
        })
        

    return jsonify(results)






if __name__ == '__main__':
    app.run(debug=True)
