from flask import Flask, Blueprint, redirect, request, jsonify, abort, make_response, url_for
from .db import get_paginated_movies_latest
movie_bp = Blueprint('movies_bp', __name__)

@movie_bp.route('/',methods=['GET'])
def home():
    return redirect(url_for('movies_bp.latest_movies', page=0))

@movie_bp.route('/<int:page>', methods=['GET'])
def latest_movies(page):

    sortc = "startYear"
    sortd = -1
    queryFilter = {}
    if 'sortColumn' in request.args:
        sortc  = request.args['sortColumn']
        sortd = request.args['sortDir']
    
    if 'genre' in request.args and len(request.args['genre'])!=0:
        queryFilter['genres'] = request.args['genre']
    if 'runtime' in request.args:
        queryFilter['runtimeMinutes'] = {"$lte":request.args['runtime']}

    l = get_paginated_movies_latest(page,sortc, sortd,queryFilter)
    
    
    return make_response(jsonify(l),200)