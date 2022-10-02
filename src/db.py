from datetime import datetime
from pymongo import MongoClient
import forecast

DB_CLIENT = MongoClient(host= 'weatherDB', port = 27017)
DATABASE = DB_CLIENT["user_tasks_database"]
USER_TASKS = DATABASE['user_tasks']

'''
Used for initializing the database.
Also, used for adding new users to the database
'''
def init_db():
    userRecords = []
    for r in USER_TASKS.find():
            userRecords.append(r['_id'])
    for user in forecast.USER_LIST:
        if not user in userRecords:
            taskRecord = {
                '_id' : user,
                'lastLogin' : datetime.now(),
                'loginHistory' : [datetime.now()],
                'queryHistory':[],
                'bill': 0
            }
            USER_TASKS.insert_one(taskRecord)
    return

'''
Used for updating the records in the database
'''
def update(updateType,userId,userQuery='',cost = 0):
    
    userRecord = USER_TASKS.find({'_id': userId})	
    currentUserBill = 0
    lastLogin = datetime.now()

    for record in userRecord:
        userLoginHistory = record['loginHistory']
        userLoginHistory.append(lastLogin)
        userQueryHistory = record['queryHistory']
        userQueryHistory.append(userQuery)
        currentUserBill = record['bill']
    
    '''
    lastLogin and loginHistory fields are updated when user logs in.
    queryHistory and bill will be updated whenever user queries weather of a city
    '''
    if(updateType == 'Login'):
        USER_TASKS.update_one({'_id': userId},
                                {
                                    '$set': {'lastLogin':lastLogin,
                                             'loginHistory':userLoginHistory
                                            }
                                })
    elif updateType == 'Query':
        currentUserBill = currentUserBill + cost
        USER_TASKS.update_one({'_id': userId},
                                {
                                    '$set': {'queryHistory':userQueryHistory,
                                             'bill':currentUserBill
                                            }
                                })
    
'''
Fetch userRecord using userId
'''
def query(userId):
    userRecord = USER_TASKS.find({'_id': userId})
    for record in userRecord:
        if(record['_id'] == userId):
            return record

'''
Delete all records.
'''
def cleanUp():
    for userId in forecast.USER_LIST.keys():
        USER_TASKS.delete_one({'_id':userId})

'''
Performs cleanUp and database initialization tasks while app startup
'''
if __name__ == "__main__":
    cleanUp()
    init_db()

