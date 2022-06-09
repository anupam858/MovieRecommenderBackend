from flask_pymongo import PyMongo

mongo = PyMongo()

def get_paginated_movies_latest(page, sortc, sortd, queryFilter):

    s = (page)*15
    data = None
    if s>0:
        data =  mongo.db.movies.find(queryFilter,{'_id':0}).skip(s).limit(15).sort(sortc,int(sortd))
    else:
        data =  mongo.db.movies.find(queryFilter,{'_id':0}).limit(15).sort(sortc,int(sortd))

    total_count = mongo.db.movies.count_documents(filter=queryFilter)

    return ({"movies": list(data), "count": total_count})