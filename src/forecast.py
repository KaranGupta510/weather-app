from crypt import methods
import re
from xmlrpc.client import DateTime
from flask import Flask,jsonify,request
import json
import db
import requests

app = Flask(__name__)

'''
Please do not modify the below constants:
	API_KEY 
	BASE_URL
Both are used to fetch the weather details for a given latitude and longitude
'''
API_KEY="674f6c1bc8fae228e6fb4c8417d56697"
BASE_URL="https://api.openweathermap.org/data/2.5"

USER_LIST = {
	'karan' : 'infa@123',
	'arjun' : 'root@456',
	'dummy_user' : 'dummy_pass',
}

'''
HTTP GET /
usage:
    used for database initialization
'''
@app.route('/',methods = ['GET'])
def root():
	db.init_db()
	return "Database connection is succesful."

'''
HTTP POST /login
RequestBody {
    userId: user name of current user
    password: password of current user
}
usage:
    authenticates user
    updates lastLogin and loginHistory of current user    
'''
@app.route('/login',methods = ['POST'])
def login():
	if request.method == 'POST':
		userId = request.form['userId']
		password = request.form['password']
		if(userId in USER_LIST and USER_LIST[userId] == password):
			db.update('Login',userId)
			return "User logged-in successfully.\n"
	response = app.response_class(status = 401)
	return response

'''
HTTP POST /weatherDetailsOfCity
RequestBody {
    userId: user name of current user
    lat: latitude of city
    long: longitude of city
}
usage:
    display the weather of a city by making a call to weather API 
    also, updates the userBill and queryHistory of current user 
'''
@app.route('/weatherDetailsOfCity',methods = ['POST'])
def weatherDetailsOfCity():
	if request.method == 'POST':
		userId = request.form['userId']
		latitude = request.form['lat']
		longitude = request.form['long']
		userQuery = ''.join(['Display weather details for city with latitude= ', 
                    latitude, ' and longitude= ', longitude])
		weatherDetailsResponse = requests.get(
            f"{BASE_URL}/weather?lat={latitude}&lon={longitude}&appid={API_KEY}")
		db.update('Query',userId,userQuery,cost=0.18)
		return weatherDetailsResponse.json()

'''
HTTP POST /lastLoginOfUser
RequestBody {


    userId: user name of current user
}
usage:
    display last login details of current user
    also, update queryHistory of current user
'''
@app.route('/lastLoginOfUser',methods = ['POST'])
def lastLoginOfUser():
	if request.method == 'POST':
		userId = request.form['userId']
		userRecord = db.query(userId)
		userQuery = 'Fetch Last Login Details of current user'
		db.update('Query',userId,userQuery)
		return jsonify(userRecord['loginHistory'][-2])
'''
HTTP POST /loginHistoryOfUser
RequestBody {
    userId: user name of current user
}
usage:
    display login history of current user
    also, update queryHistory of current user
'''
@app.route('/loginHistoryOfUser',methods = ['POST'])
def loginHistoryOfUser():
	if request.method == 'POST':
		userId = request.form['userId']
		userRecord = db.query(userId)
		userQuery = 'Fetch Login History of current user'
		db.update('Query',userId,userQuery)
		return jsonify(userRecord['loginHistory'])

'''
HTTP POST /allUsers
RequestBody {
    userId: user name of current user
}
usage:
    display list of all users in the database
    also, update queryHistory of current user
'''
@app.route('/allUsers',methods = ['POST'])
def allUsers():
	if request.method == 'POST':
		userId = request.form['userId']
		userQuery = 'Display list of users present in the database'
		db.update('Query',userId,userQuery)
	return jsonify(list(USER_LIST.keys()))

'''
HTTP POST /billOfUser
RequestBody {
    userId: user name of current user
}
usage:
    Fetch bill amount of current user
    also, update queryHistory of current user
'''
@app.route('/billOfUser',methods = ['POST'])
def billOfUser():
	if request.method == 'POST':
		userId = request.form['userId']
		userQuery = 'Fetch bill amount of current user'
		db.update('Query',userId,userQuery)
		userRecord = db.query(userId)
		return jsonify(userRecord['bill'])

'''
HTTP POST /queryHistoryOfUser
RequestBody {
    userId: user name of current user
}
usage:
    display query history of current user
    also, update queryHistory of current user
'''
@app.route('/queryHistoryOfUser',methods = ['POST'])
def queryHistoryOfUser():
	if request.method == 'POST':
		userId = request.form['userId']
		userRecord = db.query(userId)
		userQuery = 'Fetch list of all queries made by the current user'
		db.update('Query',userId,userQuery)
		return jsonify(userRecord['queryHistory'])

'''
Starts up flask app
'''
if __name__ == "__main__":
	app.run()