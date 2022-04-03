from pydoc import describe
from unicodedata import name
from api import db, ma


## Defining the Model for the table SampleData
class SampleData(db.Model):
  __tablename__ = 'SampleData'
  id = db.Column(db.Integer, primary_key=True)
  checked = db.Column(db.Boolean, default=False)
  name = db.Column(db.String(500), nullable=False)
  type = db.Column(db.String(100), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  description = db.Column(db.Text, nullable=False)
  date = db.Column(db.DateTime, nullable=False)

  def __init__(self, checked, name, type, age, description, date) -> None:
    self.checked = checked
    self.name = name
    self.type = type
    self.age = age
    self.description = description
    self.date = date

  def __repr__(self):
    return '<SampleData %r>' % self.name


## Configuring the output schema for the table SampleData
class SampleDataView(ma.SQLAlchemySchema):
  class Meta:
    fields = ('id', 'checked', 'name', 'type', 'age', 'description', 'date')
    model = SampleData
    strict = True
    load_instance=True

SingleSampleDataView = SampleDataView(many=False)
MultipleSampleDataView = SampleDataView(many=True)