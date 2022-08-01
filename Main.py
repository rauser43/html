from flask import Flask, render_template, request

# from hh_json import parce

app = Flask(__name__)

@app.get('/index')
@app.get('/')
def index():
    return render_template('index.html')


app.route('/form/')
def form():
    return render_template('form.html')


@app.post('/result/')
def result():
    vac = request.form
    data = parce(**vac)
    dat = {**data, **vac}
    print(dat)
    return render_template('about.html', res=dat)