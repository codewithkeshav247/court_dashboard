from flask import Flask, render_template, request
import sqlite3
from court_scraper import scrape_case_data

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    year = request.form['year']

    data = scrape_case_data(case_type, case_number, year)

    # Save in DB
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                 (case_type TEXT, case_number TEXT, year TEXT, parties TEXT)''')
    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?)",
              (case_type, case_number, year, data['parties']))
    conn.commit()
    conn.close()

    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)