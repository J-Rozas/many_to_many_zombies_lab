from flask import Blueprint, Flask, redirect, render_template, request

# import the required model
from models.biting import Biting

# import the required repository
from repositories import biting_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings = bitings)


# NEW

# CREATE

# EDIT

# UPDATE

# DELETE
