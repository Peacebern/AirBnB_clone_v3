#!/usr/bin/python3
"""index.py connect to api"""
from api.vi.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage

hbnbText = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}

@app_views.route('/status', strict_slashes=False)
def hbnbstatus():
    """hbnb Status"""
    return jsonify({"status": "ok"})

@app_views.route('/stats', strict_slashes=False)
def hbnbstats():
    """hbnbstats"""
    return_dict ={}
    for key, value in hbnbText.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dictdict)

if __name__ =="__main__":
    pass