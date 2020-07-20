from flask import render_template,Flask
app=Flask(__name__)
@app.route('/hola/')
@app.route('/hello/<name>')
@app.route('/user/<name>')
def user(name):
	return '<h1>Hola, {}!</h1>'.format(name)
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__=='__main__':
	app.run(host='0.0.0.0')

