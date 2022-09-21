from . import db
from datetime import datetime


class Destination(db.Model):

    __tablename__ = "destinations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True, nullable=False)
    description = db.Column(db.String(512), nullable=False)
    image = db.Column(db.String(512))
    currency = db.Column(db.String(100), nullable=False)
    # Aggregation/Relationship/Foreign Keys
    comments = db.relationship("Comment", backref="dest")

    # def set_comments(self,comment):
    #     self.comments.append(comment)

    # def __repr__(self):
    #     str = 'Name {0} , Currency {1}'
    #     str.format(self.name, self.currency)
    #     return str


class Comment(db.Model):

    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(512), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now())
    # Foreign Keys
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    destination = db.Column(db.Integer, db.ForeignKey("destinations.id"))

    # def __repr__(self):
    #     str = 'User {0}, \n Text {1}'
    #     str.format(self.user, self.text)
    #     return str


class User(db.Model):
    __tablename__ = "users"  # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    # password is never stored in the DB, an encrypted password is stored
    # the storage should be at least 255 chars long

    # relation to call user.comments and comment.created_by
    comments = db.relationship("Comment", backref="user")
