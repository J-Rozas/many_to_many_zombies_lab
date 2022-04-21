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

    zombie_object = zombie_repository.select(zombie_id)
    human_object = human_repository.select(human_id)

    # Create an instance of the class Bitting
    new_bitting = Bitting(human_object, zombie_object)
    
    # Save the new bitting into the database
    bitting_repository.save(new_bitting)

    # Redirect back to the url with all the bittings
    return redirect("/bittings")


# EDIT
@bittings_blueprint.route("/bittings/<id>/edit")
def edit_bitting(id):
    all_humans = human_repository.select_all()
    all_zombies = zombie_repository.select_all()
    bitting = bitting_repository.select(id)

    return render_template("/bittings/edit.html", bitting = bitting, humans = all_humans, zombies = all_zombies)

# UPDATE
@bittings_blueprint.route("/bittings/<id>", methods=["POST"])
def update_bitting(id):
    # Request both the id for the human and the id for the zombie from the form
    human_id = request.form["human_id"]
    zombie_id = request.form["zombie_id"]

    # Get the object of classes Human and Zombie that match the previous ids
    human = human_repository.select(human_id)
    zombie = zombie_repository.select(zombie_id)

    # Put together all the information to create a new object of class Bitting
    bitting = Bitting(human, zombie, id)

    # Update the bitting
    bitting_repository.update(bitting)

    # Redirect to bittings
    return redirect("/bittings")
    

# DELETE
@bittings_blueprint.route("/bittings/<id>/delete", methods=["POST"])
def delete_bitting(id):
    bitting_repository.delete(id)
    return redirect("/bittings")