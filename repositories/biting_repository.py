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