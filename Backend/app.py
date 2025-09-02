from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
           template_folder='../Templates',
           static_folder='../Static')

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard_route():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('../Frontend', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)