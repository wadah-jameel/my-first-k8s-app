from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <h1>Hello from Kubernetes! 🚀</h1>
    <p>Pod Name: {os.environ.get('HOSTNAME', 'Unknown')}</p>
    <p>Version: 1.0</p>
    """

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
