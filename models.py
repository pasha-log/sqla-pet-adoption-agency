from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() 

def connect_db(app): 
    db.app = app 
    db.init_app(app) 

DEFAULT_PHOTO_URL = "https://w7.pngwing.com/pngs/548/122/png-transparent-dog-paw-cat-logo-dog-animals-poster-paw-thumbnail.png"

class Adopt(db.Model): 
    """This models a pet potentially available for adoption"""

    __tablename__ = "pets_for_adoption"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    name = db.Column(db.Text, nullable=False) 
    species = db.Column(db.Text, nullable=False) 
    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT_PHOTO_URL) 
    age = db.Column(db.Text, nullable=True) 
    notes = db.Column(db.Text, nullable=True) 
    available = db.Column(db.Text, nullable=False, default=True)

    def __repr__(self): 
        return f"<Adopt {self.name} {self.species} {self.age} >"


