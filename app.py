from re import DEBUG
from flask import Flask, render_template

app = Flask(__name__)

#adding a fake db

JOBS = [
  {
    'id': 1,
    'testType': 'Accounting Records',
    'client': 'TestClient1',
    'entity': 'Entity1',
  },
  {
    'id': 2,
    'testType': 'Employee Costs',
    'client': 'TestClient2',
    'enttiy': 'Entity1',
  },
  {
    'id': 3,
    'testType': 'Property Plant and Equipment',
    'client': 'TestClient3',
    'entity': 'Entity1',
  },
  {
    'id': 4,
    'testType': 'Forensics',
    'client': 'TestClient4',
    'entity': 'Entity1',
  },
  {
    'id': 5,
    'testType': 'Accounting Outsource Services',
    'client': 'TestClient4',
    'entity': 'Entity2',
  }
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)