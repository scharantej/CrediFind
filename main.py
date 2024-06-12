
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    cibil_score = request.form['cibil_score']
    loan_options = get_loan_options(cibil_score)
    return redirect(url_for('results', loan_options=loan_options))

@app.route('/results')
def results():
    loan_options = request.args.get('loan_options')
    return render_template('results.html', loan_options=loan_options)

def get_loan_options(cibil_score):
    # Placeholder function. Replace this with actual logic to fetch loan options based on cibil score.
    return []

if __name__ == '__main__':
    app.run(debug=True)
