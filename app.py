from flask import Flask
app = Flask(__name__)


@app.route('/')
def landingpage():
	return "<h2>Go to /user for searching details of users </h2>"



@app.route('/user/<username>')
def userdetails(username):
	if (username == "modi"):
		return { "username" : "Narendra Modi", "Occupation" : "Politician", "Role" : "Prime Minister" }
	elif (username == "nirmala"):
		return { "username" : "Nirmala Sitaraman", "Occupation" : "Politician", "Role" : "Prime Minister" }
	else :
		return "Pick one from [modi, nirmala] and try again"