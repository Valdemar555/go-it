from datetime import datetime
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField, DateField

class Phone(EmbeddedDocument):
    value = StringField(default=False)

class Contacts(Document):
    first_name = StringField(max_length=20, null=False)
    last_name = StringField(max_length=20, null=False)
    phone = ListField(EmbeddedDocumentField(Phone))
    birthday = DateField(null=True)
    email = StringField(max_length=30, null=True)
    address = StringField(max_length=30, null=True)
    
class Tag(EmbeddedDocument):
    name = StringField()


class Record(EmbeddedDocument):
    description = StringField()
    done = BooleanField(default=False)


class Note(Document):
    name = StringField()
    created = DateTimeField(default=datetime.now())
    records = ListField(EmbeddedDocumentField(Record))
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {'allow_inheritance': True}
    
    
