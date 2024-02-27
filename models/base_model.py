import uuid
from datetime import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        d = self.__dict__.copy()
        d['__class__'] = self.__class__.__name__
        d['created_at'] = d['created_at'].isoformat()
        d['updated_at'] = d['updated_at'].isoformat()
        return d
