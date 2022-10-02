# weather-app
A python flask app to query the weather details of a city using its latititude and longitude.

# Description

The user can login into the application via command line and can issue the following queries:
  1. Weather of <location> - each weather query will cost $0.18 - (address should be in the form of latitude longitude)
  2. Last login of current user
  3. List logins of current user 
  4. List all users in the database
  5. Get bill of current user
  6. List all queries made by the current user.

The weather details are fetched from a public weather API: 
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

# Tech stack used: MongoDB, Flask, Docker

# Install dependencies:
  1. Python 3.10.7
  2. Docker
  
# How to run the application?
  1. Clone the git repository.
  2. Run below command to create docker containers for mongo and server:
     docker compose up web mongo
  3. Run below command to create docker containers for client:
     docker compose run client
  4. Few users are created in the database while app startup, which can be used for login. 
  Refer forecast.py file (present in src folder) to get the login details of users {USER_LIST}
  5. Post login, user can enter a number depending on the task he/she wishes to perform.
  6. Run below command to remove docker containers:
      docker compose down
      

  # References:

  https://www.learnpython.org/

  https://www.tutorialspoint.com/docker/index.htm

  https://www.educative.io/blog/mongodb-with-docker

  https://www.geeksforgeeks.org/mongodb-python-insert-update-data/

  https://www.youtube.com/watch?v=Aa-F6zqLmig

  https://www.youtube.com/watch?v=prGy9ZxyP-A

  https://docs.docker.com/language/python/build-images/

  https://www.geeksforgeeks.org/mongodb-and-python/?ref=lbp

  https://kb.objectrocket.com/mongo-db/use-docker-and-python-for-a-mongodb-application-1046

  https://www.geeksforgeeks.org/get-post-requests-using-python/

  https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/

  https://github.com/public-apis/public-apis#weather

  https://rapidapi.com/blog/access-global-weather-data-with-these-weather-apis/

  https://openweathermap.org/current

  https://stackoverflow.com/questions/5685406/inconsistent-use-of-tabs-and-spaces-in-indentation



  
