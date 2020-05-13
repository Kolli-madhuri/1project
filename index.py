from flask import *

app=Flask(__name__)#object creation for flask


@app.route("/")
@app.route("/home")
def home():
	return render_template("index.html",name="madhuri")


@app.route("/about")
def about_page():
	data=["madhuri","chandini","bhargavi"]
	return render_template("about.html",data=data)


if __name__ =="__main__":
	app.run(debug=True)