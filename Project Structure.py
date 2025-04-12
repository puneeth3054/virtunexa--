from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import string
import random
import os

app = Flask(__name__)
DB_FILE = "db.sqlite3"

# --- Utility Functions ---
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original TEXT NOT NULL,
                short TEXT UNIQUE NOT NULL,
                clicks INTEGER DEFAULT 0
            )
        """)
        conn.commit()

def generate_short_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        conn = get_db_connection()
        short_id = generate_short_id()

        # Check for collisions
        while conn.execute("SELECT * FROM urls WHERE short = ?", (short_id,)).fetchone():
            short_id = generate_short_id()

        conn.execute("INSERT INTO urls (original, short) VALUES (?, ?)", (original_url, short_id))
        conn.commit()
        conn.close()

        short_url = request.host_url + short_id
        return render_template("index.html", short_url=short_url)

    return render_template("index.html")

@app.route('/<short_id>')
def redirect_to_url(short_id):
    conn = get_db_connection()
    result = conn.execute("SELECT * FROM urls WHERE short = ?", (short_id,)).fetchone()
    if result:
        conn.execute("UPDATE urls SET clicks = clicks + 1 WHERE short = ?", (short_id,))
        conn.commit()
        conn.close()
        return redirect(result["original"])
    conn.close()
    return "URL not found", 404

@app.route('/analytics')
def analytics():
    conn = get_db_connection()
    urls = conn.execute("SELECT * FROM urls").fetchall()
    conn.close()
    return render_template("analytics.html", urls=urls)

# --- Initialize ---
if __name__ == '__main__':
    if not os.path.exists(DB_FILE):
        init_db()
    app.run(debug=True)

