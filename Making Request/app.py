from flask import Flask,render_template,redirect,request

app=Flask(__name__)
friends=["Pappu","Paji","Murda","Bhalla"]
nums=15

@app.route('/')
def hello():
    return render_template("index.html",my_friends=friends,number=nums)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/home')
def home():
    return redirect('/')

# @app.route('/submit' ,methods=["POST"])
# def submit():
#     if request.method=="POST":
#         user_name=request.form['username']
#         no1 = int(request.form['no1'])
# 		no2 = int(request.form['no2'])
#     return "HELLO {} ans is ".format(user_name,str(no1+no2))
    
@app.route('/submit' ,methods=["POST"])
def submit_num():
	if request.method == 'POST':
		no1 = int(request.form['no1'])
		no2 = int(request.form['no2'])
	return str(no1+no2)

    


if __name__=='__main__':
    app.run(debug=True) 