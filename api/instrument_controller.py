from flask import Blueprint, jsonify, request
from domain.nasa_service_interface import NASAServiceInterface
from domain.instrument import Instrument
from services.nasa_service import NASAService

instrument_bp = Blueprint('instrument_bp', __name__)

routes = ["CME", "HSS", "WSAEnlilSimulations"]


nasa_service: NASAServiceInterface = NASAService()


@instrument_bp.route('/instruments', methods=['GET'])
def get_instruments():
    instruments = set()
    for route in routes:
        data = nasa_service.fetch_data(route)
        for event in data:
            for instr in event.get("instruments", []):
                instruments.add(Instrument(instr.get("displayName", "No especificado")))

    
    result = [instrument.to_dict() for instrument in instruments]
    return jsonify(result)


@instrument_bp.route('/instrument_usage', methods=['GET'])
def get_instrument_usage():
    usage = {}
    total_instruments = 0

    for route in routes:
        data = nasa_service.fetch_data(route)
        for event in data:
            for instr in event.get("instruments", []):
                instrument_name = instr.get("displayName", "No especificado")
                usage[instrument_name] = usage.get(instrument_name, 0) + 1
                total_instruments += 1

    for instrument in usage:
        usage[instrument] = usage[instrument] / total_instruments

    return jsonify(usage)


@instrument_bp.route('/instrument_usage_by_activity', methods=['POST'])
def get_instrument_usage_by_activity():
    instrument_name = request.json.get("instrument_name")
    
    if not instrument_name:
        return jsonify({"error": "Falta el nombre del instrumento"}), 400
    
    usage = {}
    total_activities = 0
    
    for route in routes:
        data = nasa_service.fetch_data(route)
        for event in data:
            for instr in event.get("instruments", []):
                if instr.get("displayName") == instrument_name:
                    activity_id = event.get("activityID", "No especificado")
                    usage[activity_id] = usage.get(activity_id, 0) + 1
                    total_activities += 1

    if total_activities == 0:
        return jsonify({"message": "No se encontró el instrumento en ninguna actividad."}), 404
    
    
    for activity_id in usage:
        usage[activity_id] = usage[activity_id] / total_activities

    return jsonify(usage)
