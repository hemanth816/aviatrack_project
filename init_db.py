import sqlite3

conn = sqlite3.connect('duty_logs.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS pilot_duties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pilot_id TEXT NOT NULL,
    flight_id TEXT NOT NULL,
    duty_start TEXT NOT NULL,
    duty_end TEXT NOT NULL,
    is_violation INTEGER DEFAULT 0
)
''')

conn.commit()
conn.close()

print("Database initialized successfully.")
