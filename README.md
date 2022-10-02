# weather-app
A python flask app to query the weather details of a city using its latititude and longitude.

Description

The user can login into the application via command line and can issue the following queries:
  1. Weather of <location> - each weather query will cost $0.18 - (address should be in the form of latitude longitude)
  2. Last login of current user
  3. List logins of current user 
  4. List all users in the database
  5. Get bill of current user
  6. List all queries made by the current user.

The weather details are fetched from a public weather API: 
  https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

Tech stack used: MongoDB, Flask, Docker

Install dependencies:
  1. Python 3.10.7
  2. Docker
  
How to run the application?
  1. Clone the git repository.
  2. Run below command to create docker containers for mongo and server:
     docker compose up web mongo
  3. Run below command to create docker containers for client:
     docker compose run client
  4. Below users are created in the database while app startup, which can be used for login:
     USER_LIST = {
        'karan' : 'infa@123',
        'arjun' : 'root@456',
        'dummy_user' : 'dummy_pass',
      }
  5. Post login, user can enter a number depending on the task he/she wishes to perform.
  6. Run below command to remove docker containers:
      docker compose down
      

  
  
