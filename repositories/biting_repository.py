# import run_sql to be able to use SQL queries in Flask
## Perhaps this is not needed because run_sql is also being imported from human_repository and zombie_repository
from db.run_sql import run_sql

# import all the needed classes
from models.biting import Biting
from models.human import Human
from models.zombie import Zombie

# import all the needed repositories
from repositories import human_repository
from repositories import zombie_repository

def select_all():
    # Initialize a list to store all the bittings
    list_of_bitings = []

    # SQL query to select all the bittings
    sql = "SELECT * FROM bitings"

    # Run the SQL query and store the result in the variable all_bitings. The return value is a list of dictionaries
    all_bitings = run_sql(sql)

    # Iterate through 
    for bite in all_bitings:
        # zombie that performed the bite
        zombie = zombie_repository.select(bite['zombie_id'])

        # human that was bitten
        human = human_repository.select(bite['human_id'])

        list_of_bitings.append(Biting(human, zombie))

    # return a list of instances of Biting that is then looped through in the template in order to show each element
    return list_of_bitings

def save(biting):
    # SQL query to insert a new biting into the table bitings
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s, %s) returning id"

    # Values that are to be passed into the SQL query, which come from the argument passed into the function
    values = [biting.human, biting.zombie]

    # Run the SQL query and store what the function returns (a list of dictionaries) into a variable called results
    results = run_sql(sql, values)

    # Take the value of the "id" key of the first dictionary of the list stored in the variable results and store it in the variable id
    id = results[0]["id"]

    # Store the value kept in the variable id in the attribute "id" of the object biting of class Biting that what passed into the function
    biting.id = id