import pytest
from api import app, db
from api.sample.models import SampleData


@pytest.fixture(scope='module')
def new_sample_data():
  sample_data = SampleData(True, "John", "Human", 18, "This is used for testing", "2022-04-03 16:21:11")
  return sample_data


@pytest.fixture(scope='module')
def test_client():
  with app.test_client() as testing_client:
    with app.app_context():
      yield testing_client


@pytest.fixture(scope='module')
def init_database(test_client):
  db.create_all()
  
  sample_data1 = SampleData(True, "John", "Human", 18, "This is used for testing 1", "2022-04-03 16:21:11")
  sample_data2 = SampleData(False, "Arther", "Dog", 4, "This is used for testing 2", "2022-04-03 16:25:19")

  db.session.add(sample_data1)
  db.session.add(sample_data2)

  db.session.commit()

  yield

  db.drop_all()

