from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speakers')
def speakers():
    return render_template('speakers.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/venue')
def venue():
    return render_template('venue.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
