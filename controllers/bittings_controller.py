from flask import Blueprint, Flask, redirect, render_template, request

# import the required model
from models.bitting import Bitting

# import the required repository
from repositories import bitting_repository, zombie_repository, human_repository

bittings_blueprint = Blueprint("bittings", __name__)

# INDEX
@bittings_blueprint.route("/bittings")
def bittings():
    bittings = bitting_repository.select_all()
    return render_template("bittings/index.html", bittings = bittings)


# NEW
@bittings_blueprint.route("/bittings/new")
def new_bitting():
    all_humans = human_repository.select_all()
    all_zombies = zombie_repository.select_all()

    return render_template("/bittings/new.html", humans = all_humans, zombies = all_zombies)


# CREATE
@bittings_blueprint.route("/bittings", methods=["POST"])
def create_bitting():
    # Get the id of both the zombie and the human
    zombie_id = request.form['zombie_id']
    human_id = request.form['human_id']

    # Create an instance of the class Bitting
    new_bitting = Bitting(human_id, zombie_id)
    
    # Save the new bitting into the database
    bitting_repository.save(new_bitting)

    # Redirect back to the url with all the bittings
    return redirect("/bittings")


# EDIT

# UPDATE

# DELETE
