from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def index():
	user=request.args.get("user")
	return render_template('index.html',user=user)
if __name__=='__main__':
	app.run(host='0.0.0.0')

	

