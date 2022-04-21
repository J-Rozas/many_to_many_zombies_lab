from flask import Blueprint, Flask, redirect, render_template, request

# import the required model
from models.biting import Biting

# import the required repository
from repositories import biting_repository, zombie_repository, human_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings = bitings)


# NEW
@bitings_blueprint.route("/bitings/new")
def new_biting():
    all_humans = human_repository.select_all()
    all_zombies = zombie_repository.select_all()

    return render_template("/bitings/new.html", humans = all_humans, zombies = all_zombies)


# CREATE
@bitings_blueprint.route("/bitings", methods=["POST"])
def create_biting():
    # Get the id of both the zombie and the human
    zombie_id = request.form['zombie_id']
    human_id = request.form['human_id']

    # Create an instance of the class Biting
    new_biting = Biting(human_id, zombie_id)
    
    # Save the new biting into the database
    biting_repository.save(new_biting)

    # Redirect back to the url with all the bitings
    return redirect("/bitings")


# EDIT

# UPDATE

# DELETE
