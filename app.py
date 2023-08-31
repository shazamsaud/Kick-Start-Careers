from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id ': '1',
    'title': 'Graphic Designer',
    'location': 'banglore,india',
    'salary': 'Rs 8,00,000'
  },
  {
    'id ': '2',
    'title': 'Frontend Developer',
    'location': 'banglore,india',
    'salary': 'Rs 10,00,000'
  },
  {
    'id ': '3',
    'title': 'Backend Developer',
    'location': 'banglore,india',
    'salary': 'Rs 12,00,000'
  },
  {
    'id ': '4',
    'title': 'Devops Developer',
    'location': 'banglore,india',
    'salary': 'Rs 15,00,000'
  },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, c_Name="Kick Start")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
