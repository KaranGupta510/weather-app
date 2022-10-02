import json
from urllib import response
import requests
BASE_URL = "http://weather-app:5000"

'''
usage: 
    validates connection to weather app, 
    If connection is successful, 
        prints response recieved, and makes call to loginUser API
    If connection failure occurs,
        prints response status code
'''
def validateConnection():
    response = requests.get(f"{BASE_URL}/")
    if(response.status_code == 200):
        print(response.text)
        loginUser(0)
    else:
        print(response.status_code)

'''
params:
    attempts: no. of login attempts made by the user

usage:
    Asks for login credentials, if no. of login attempts is valid.
    Makes call to weatherAppQueryService in case of successful login.
    Exits in case, no. of login attempts excceds 3.
'''
def loginUser(attempts):
    if(attempts > 3):
        print("No more login attempts left, exiting..")
        return
    if(attempts != 0):
        print("Retry login by providing correct login credentials")
    else:
        print("Please provide your login credentials:")
    userId = input("Username:")
    password = input("Password:")
    userDetails = {'userId': userId, 'password': password}
    response = requests.post(f"{BASE_URL}/login",data=userDetails)
    if(response.status_code != 200):
        print(response.text)
        loginUser(attempts=attempts+1)
    else:
        print(response.text)
        weatherAppQueryService(userId)

'''
params: 
    userId: user name of current logged-in user.

usage:
    Displays a list of queries that can be performed by the logged-in user.
    Depending upon the query, respective API endpoint is triggered to fetch the response.
    This process is repeated until user quits the application.
'''
def weatherAppQueryService(userId):
    choice = '0'
    while(choice != '7'):
        userDetails = {"userId":userId}
        print('''Enter a number depending on the task you want to perform?
        1. Get weather details of city 
        2. Last login of current user
        3. Login history of current user
        4. List of all users in the database
        5. Get Bill of current user
        6. List all previous queries made by the current user
        7. Exit weather application\n''')
        
        choice = input("Enter number:\n")
        match choice:
            case '1':
                latitude = input("Enter Latitude of city: ")
                longitude = input("Enter Longitude of city: ")
                geoLocationDetails = {
                    "lat": latitude,
                    "long": longitude,
                    }
                geoLocationDetails.update(userDetails)
                response = requests.post(f"{BASE_URL}/weatherDetailsOfCity",data=geoLocationDetails)
                if(response.status_code == 200):
                    print(json.dumps(response.json(),indent = 3))
                else:
                    print(response.status_code)
                con = input("Do you wish to perform any other task?(yes/no)")
                if(con == 'no'):
                    print("Goodbye, exiting...")
                    choice = '7'
            
            case '2':
                response = requests.post(f"{BASE_URL}/lastLoginOfUser",data=userDetails)
                if(response.status_code == 200):
                    print(response.text)
                else:
                    print(response.status_code)
                con = input("Do you wish to perform any other task?(yes/no)")
                if(con == 'no'):
                    print("Goodbye, exiting...")
                    choice = '7'

            case '3':
                response = requests.post(f"{BASE_URL}/loginHistoryOfUser",data=userDetails)
                if(response.status_code == 200):
                    print(response.text)
                else:
                    print(response.status_code)
                con = input("Do you wish to perform any other task?(yes/no)")
                if(con == 'no'):
                    print("Goodbye, exiting...")
                    choice = '7'

            case'4':
                response = requests.post(f"{BASE_URL}/allUsers",data=userDetails)
                if(response.status_code == 200):
                    print(response.text)
                else:
                    print(response.status_code)
                con = input("Do you wish to perform any other task?(yes/no)")
                if(con == 'no'):
                    print("Goodbye, exiting...")
                    choice = '7'

            case '5':
                response = requests.post(f"{BASE_URL}/billOfUser",data=userDetails)
                if(response.status_code == 200):
                    print("$"+response.text)
                else:
                    print(response.status_code)
                con = input("Do you wish to perform any other task?(yes/no)")
                if(con == 'no'):
                    print("Goodbye, exiting...")
                    choice = '7'
        
            case '6':
                response = requests.post(f"{BASE_URL}/queryHistoryOfUser",data=userDetails)
                if(response.status_code == 200):
                    print(response.text)
                else:
                    print(response.status_code)
                con = input("Do you wish to perform any other task?(yes/no)")
                if(con == 'no'):
                    print("Goodbye, exiting...")
                    choice = '7'
                    
            case '7':
                print("Goodbye, exiting...")

            case _:
                print("Incorrect input, please enter one of the values from 1 to 7")
        
'''
client execution triggers from here.
'''
if __name__ == "__main__":
    validateConnection()
    
