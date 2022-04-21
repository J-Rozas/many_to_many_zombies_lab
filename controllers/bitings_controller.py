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

# EDIT

# UPDATE

# DELETE
