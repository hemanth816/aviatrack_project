import sqlite3

# Create DB and table if not exists
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Create duty_logs table
    c.execute('''
        CREATE TABLE IF NOT EXISTS duty_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pilot_id TEXT NOT NULL,
            flight_id TEXT NOT NULL,
            duty_start TEXT NOT NULL,
            duty_end TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
