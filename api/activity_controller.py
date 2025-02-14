from flask import Blueprint, jsonify
from services.nasa_service import NASAService
from domain.activity import Activity

activity_bp = Blueprint('activity_bp', __name__)

routes = ["CME", "HSS", "WSAEnlilSimulations"]

nasa_service = NASAService()

@activity_bp.route('/activity_ids', methods=['GET'])
def get_activity_ids():
    activity_ids = set()
    for route in routes:
        data = nasa_service.fetch_data(route)
        for event in data:
            activity_id = event.get("activityID", "No especificado")
            activity_ids.add(activity_id)

    result = [{"activity_id": activity_id} for activity_id in activity_ids]
    return jsonify(result)

