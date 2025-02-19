from flask import Blueprint, jsonify, request

event_route_bp = Blueprint("event_route", __name__)

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

@event_route_bp.route("/event", methods=["POST"])
def create_new_event():
    http_request = HttpRequest(body=request.json)

    http_response = HttpResponse(body={ "hello": "world" }, status_code=201)
    
    return jsonify(http_response.body), http_response.status_code
