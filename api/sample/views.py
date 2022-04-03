from crypt import methods
import re
from api import db
from datetime import datetime
from flask import Blueprint, request, jsonify
from api.sample.models import SampleData, SingleSampleDataView, MultipleSampleDataView


sample_blueprint = Blueprint('sample_blueprint', __name__)


def validate_input(req):
  try:
    if not req.data:
      return False, "Type Mismatched"

    req = req.get_json(force=True)
    dateFormat = "^(20[0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]) (0[1-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"

    if (('checked' not in req or type(req['checked']) != bool) 
      or ('name' not in req or type(req['name']) != str or len(req['name']) > 500 or len(req['name']) <= 0)
      or ('type' not in req or type(req['type']) != str or len(req['type']) > 100 or len(req['type']) <= 0)
      or ('age' not in req or type(req['age']) != int)
      or ('description' not in req or type(req['description']) != str)
      or ('date' not in req or not re.match(dateFormat, req['date']))
    ):
      return False, "Type Mismatched"
    return True, req
  except BaseException as e:
    return False, str(e)

def validate_data(id):
  try:
    sample_data = SampleData.query.get(id)
    if not sample_data:
      return False, "No data available"
    return True, sample_data
  except BaseException as e:
    return False, str(e)


@sample_blueprint.route('/api/sample/all', methods=['GET'])
def get_all_data():
  try:
    sample_data = SampleData.query
    if sample_data.count() > 0:
      return jsonify({"message": f"There are { sample_data.count() } records available in the database!", "count": sample_data.count(), "status": 200, "data": MultipleSampleDataView.dump( sample_data.all() )}), 200
    return jsonify({"message": "There is no records available in the database", "status": 404, "data": [], "error": "No data available"}), 404
  except BaseException as e:
    return jsonify({"message": "We encounted an error while creating the record. Please read the API guide to proceed further.", "status": 500, "data": [], "error": str(e)}), 500


@sample_blueprint.route('/api/sample/<int:id>', methods=['GET'])
def get_data_by_id(id):
  try:
    is_data, sample_data = validate_data(id)
    if not is_data:
      return jsonify({"message": "There is no records available associated with the id", "status": 404, "data": [], "error": sample_data}), 404
    return jsonify({"message": f"The requested record is found in the database", "status": 200, "data": SingleSampleDataView.dump( sample_data )}), 200
  
  except BaseException as e:
    return jsonify({"message": "We encounted an error while creating the record. Please read the API guide to proceed further.", "status": 500, "data": [], "error": str(e)}), 500


@sample_blueprint.route('/api/sample/create', methods=['POST'])
def create_data():
  try:
    is_valid, req = validate_input(request)

    if not is_valid:
      return jsonify({"message": "We encounted an error while creating the record. Please read the API guide to proceed further.", "status": 400, "data": [], "error": req}), 400

    sample_data = SampleData(
      checked=req['checked'],
      name=req['name'],
      type=req['type'],
      age=req['age'],
      description=req['description'],
      date=datetime.strptime(req['date'], "%Y-%m-%d %X")
    )
    db.session.add(sample_data)
    db.session.commit()

    return jsonify({"message": "A new record is added successfully", "status": 201, "data": SingleSampleDataView.dump(sample_data)}), 201
  except BaseException as e:
    return jsonify({"message": "We encounted an error while creating the record. Please read the API guide to proceed further.", "status": 500, "data": [], "error": str(e)}), 500


@sample_blueprint.route('/api/sample/<int:id>/update', methods=['PUT'])
def update_data_by_id(id):
  try:
    is_data, sample_data = validate_data(id)

    if not is_data:
      return jsonify({"message": "There is no records available associated with the id", "status": 404, "data": [], "error": sample_data}), 404

    is_valid, req = validate_input(request)

    if not is_valid:
      return jsonify({"message": "We encounted an error while creating the record. Please read the API guide to proceed further.", "status": 400, "data": [], "error": req}), 400

    sample_data.checked=req['checked']
    sample_data.name=req['name']
    sample_data.type=req['type']
    sample_data.age=req['age']
    sample_data.description=req['description']
    sample_data.date=datetime.strptime(req['date'], "%Y-%m-%d %X")

    db_session = db.session.object_session(sample_data)
    db_session.commit()

    return jsonify({"message": "The record is updated successfully", "status": 200, "data": SingleSampleDataView.dump(sample_data)}), 200
  except BaseException as e:
    return jsonify({"message": "We encounted an error while creating the record. Please read the API guide to proceed further.", "status": 500, "data": [], "error": str(e)}), 500


@sample_blueprint.route('/api/sample/<int:id>/delete', methods=['DELETE'])
def delete_data_by_id(id):
  try:
    is_data, sample_data = validate_data(id)

    if not is_data:
      return jsonify({"message": "There is no records available associated with the id", "status": 404, "data": [], "error": sample_data}), 404

    db_session = db.session.object_session(sample_data)
    db_session.delete(sample_data)
    db_session.commit()

    return jsonify({"message": "The record is deleted successfully", "status": 200}), 200
  except BaseException as e:
    return jsonify({"message": "We encounted an error while creating the record. Please read the API guide to proceed further.", "status": 500, "data": [], "error": str(e)}), 500
