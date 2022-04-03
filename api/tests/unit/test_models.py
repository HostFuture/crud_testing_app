from api import app, db
from api.sample.models import SampleData
from datetime import datetime


def test_new_data():
  data = SampleData(True, "John", "Human", 18, "This is used for testing 1", "2022-04-03 16:21:11")

  assert data.checked == True
  assert data.name == "John"
  assert data.type == "Human"
  assert data.age == 18
  assert data.description == "This is used for testing 1"
  assert data.date == "2022-04-03 16:21:11"
  assert data.__repr__() == "<SampleData 'John'>"


def test_get_page():
  test_client =  app.test_client()
  response = test_client.get('/api/sample/all')
  assert response.status_code == 404
  assert b"error" in response.data
  assert b"status" in response.data
  assert b"data" in response.data
  assert b"message" in response.data


def test_update_id_page():
  test_client =  app.test_client()
  response = test_client.get('/api/sample/1')
  assert response.status_code == 404
  assert b"error" in response.data
  assert b"status" in response.data
  assert b"data" in response.data
  assert b"message" in response.data


def test_delete_id_page():
  test_client =  app.test_client()
  response = test_client.get('/api/sample/1')
  assert response.status_code == 404
  assert b"error" in response.data
  assert b"status" in response.data
  assert b"data" in response.data
  assert b"message" in response.data


def test_get_by_id_page():
  test_client =  app.test_client()
  response = test_client.get('/api/sample/1')
  assert response.status_code == 404
  assert b"error" in response.data
  assert b"status" in response.data
  assert b"data" in response.data
  assert b"message" in response.data
