from app import db


class Text(db.Model):
    __tablename__ = 'materials_text'

    id = db.Column(db.Integer, primary_key=True)
    date_and_time = db.Column(db.DateTime, default=db.func.now())
    title = db.Column(db.String(100), nullable=False)
    text_content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=0)

    @property
    def serialized(self):
        return {
            'type': 'text',
            'id': self.id,
            'dateAndTime': self.date_and_time,
            'title': self.title,
            'textContent': self.text_content,
            'rating': self.rating
        }


class Audio(db.Model):
    __tablename__ = 'materials_audio'

    id = db.Column(db.Integer, primary_key=True)
    date_and_time = db.Column(db.DateTime, default=db.func.now())
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=0)

    @property
    def serialized(self):
        return {
            'type': 'audio',
            'id': self.id,
            'dateAndTime': self.date_and_time,
            'title': self.title,
            'url': self.url,
            'rating': self.rating
        }


class Video(db.Model):
    __tablename__ = 'materials_video'

    id = db.Column(db.Integer, primary_key=True)
    date_and_time = db.Column(db.DateTime, default=db.func.now())
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=0)

    @property
    def serialized(self):
        return {
            'type': 'video',
            'id': self.id,
            'dateAndTime': self.date_and_time,
            'title': self.title,
            'url': self.url,
            'rating': self.rating
        }
