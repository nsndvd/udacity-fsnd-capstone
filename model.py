from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
class Developer(db.Model):
  __tablename__ = 'Developer'
  id = Column(Integer, primary_key=True)
  username = Column(String, nullable=False)
  full_name = Column(String, nullable=False)

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def insert_or_update(self):
    db.session.add(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'username': self.username,
      'full_name': self.full_name
  }

class Booking(db.Model):
  __tablename__ = 'Booking'
  id = Column(Integer, primary_key=True)
  developer_id = Column(Integer, ForeignKey('Developer.id'), nullable=False)
  resource_id = Column(Integer, ForeignKey('Resource.id'), nullable=False)
  start_time = Column(DateTime(), default=datetime.utcnow)
  expected_duration_hours = Column(Integer)

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def insert_or_update(self):
    db.session.add(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'developer_id': self.developer_id,
      'resource_id': self.resource_id,
      'start_time': self.start_time,
      'expected_duration_hours': self.expected_duration_hours
    }

class Resource(db.Model):
  __tablename__ = 'Resource'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  note = Column(String)
  img_url = Column(String)

  def insert_or_update(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'note': self.note,
      'img_url': self.img_url,
    }
