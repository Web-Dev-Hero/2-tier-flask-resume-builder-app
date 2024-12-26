from app import db

# Resume Table ka Model
class Resume(db.Model):
    __tablename__ = 'resume'

    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    name = db.Column(db.String(100), nullable=False)  # Name Field
    email = db.Column(db.String(100), nullable=False)  # Email Field
    phone = db.Column(db.String(15), nullable=False)  # Phone Field
    skills = db.Column(db.Text, nullable=False)  # Skills Field

    def __repr__(self):
        return f"<Resume {self.name}>"
