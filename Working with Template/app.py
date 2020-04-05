from flask import Flask,render_template,redirect

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
if __name__=='__main__':
    app.run(debug=True) 