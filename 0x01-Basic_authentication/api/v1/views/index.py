#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def authorized() -> str:
    """ GET /api/v1/unauthorized
    Return:
        - raise a 401 error
    """
    abort(401, description="Unauthorized")
