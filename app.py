# Evangelism Tabling Tracker (MVP)

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB = 'evangelism_log.db'

def init_db():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact_info TEXT,
                topic TEXT,
                prayer_request TEXT,
                follow_up_needed BOOLEAN,
                date TEXT
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM conversations ORDER BY date DESC")
        logs = c.fetchall()
    return render_template('index.html', logs=logs)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact_info']
        topic = request.form['topic']
        prayer = request.form['prayer_request']
        follow_up = 1 if 'follow_up_needed' in request.form else 0
        date = datetime.now().strftime('%Y-%m-%d %H:%M')

        with sqlite3.connect(DB) as conn:
            c = conn.cursor()
            c.execute("""
                INSERT INTO conversations (name, contact_info, topic, prayer_request, follow_up_needed, date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, contact, topic, prayer, follow_up, date))
            conn.commit()

        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
