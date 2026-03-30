from models.models import Event, db

class EventService:

    def get_all(self):
        return Event.query.all()

    def add(self, title, genre):
        event = Event(title=title, genre=genre)
        db.session.add(event)
        db.session.commit()

    def delete(self, id):
        event = Event.query.get(id)
        if event:
            db.session.delete(event)
            db.session.commit()

    def get_by_id(self, id):
        return Event.query.get(id)

    def update(self, id, title, genre):
        event = Event.query.get(id)
        if event:
            event.title = title
            event.genre = genre
            db.session.commit()