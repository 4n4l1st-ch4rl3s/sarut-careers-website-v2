from flask import Flask, jsonify,render_template

app = Flask(__name__)


JOBS = [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Mombasa, Kenya',
    'salary': '$90,000'
    },
    {
    'id': 2,
    'title': 'Data Scientists',
    'location': 'Kisumu, Kenya',
    'salary': '$75,000'
    },
    {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
    },
    {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, California',
    'salary': '$120,000'
    },
]

@app.route('/')
def hello_sarut():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Sarut')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)