
import email
from enum import unique
from utils.db import db
import uuid

def User(db.Model):
    user_id = db.Column(db.String(32), primary_key =True, default = str(uuid.uuid4()))

    first_name=db.Column(db.String(255), nullable = False)
    last_name=db.Column(db.String(232), nullable = False)
    email=db.Column(db.String(232), nullable = False, unique = True)
    created_at=db.Column(db.DateTime, nullable = False, default = db.func.now())

    def to_json(self):
        return {
            'user_id' = self.user_id,
            'first_name' = self.first_name,
            'last_name' = self.last_name,
            'email' = self.email
            'created_list' = self.created_at
        }
