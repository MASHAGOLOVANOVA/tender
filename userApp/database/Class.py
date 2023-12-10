from userApp import db  # Замените "your_app" на имя вашего приложения

class Sender(db.Model):
    __tablename__ = 'sender'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String)

    def serialize(self):
        return {
            'id': self.id,
            'role': self.role
        }

    def __repr__(self):
        return f'<Sender {self.id}>'


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id'))
    date = db.Column(db.DateTime)
    sender_id = db.Column(db.Integer, db.ForeignKey('sender.id'))
    status = db.Column(db.Boolean, nullable=True)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    content = db.Column(db.String)

    def serialize(self):
        return {
            'id': self.id,
            'chat_id': self.chat_id,
            'date': str(self.date),
            'sender_id': self.sender_id,
            'status': self.status,
            'type_id': self.type_id,
            'content': self.content
        }

    def __repr__(self):
        return f'<Message {self.id}>'

class Type(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)

    def serialize(self):
        return {
            'id': self.id,
            'type': self.type
        }

    def __repr__(self):
        return f'<Type {self.id}>'


class Chat(db.Model):
    __tablename__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=True, default=None)
    ware_chat_id = db.Column(db.Integer, db.ForeignKey('ware_chat.id'), nullable=True, default=None)

    def serialize(self):
        return {
            'id': self.id,
            'field_id': self.field_id,
            'ware_chat_id': self.ware_chat_id
        }

    def __repr__(self):
        return f'<Chat {self.id}>'


class WareChat(db.Model):
    __tablename__ = 'ware_chat'
    id = db.Column(db.Integer, primary_key=True)
    ware_id = db.Column(db.Integer, db.ForeignKey('ware.id'))
    name = db.Column(db.String)

    def serialize(self):
        return {
            'id': self.id,
            'ware_id': self.ware_id,
            'name': self.name
        }

    def __repr__(self):
        return f'<WareChat {self.id}>'

class Field(db.Model):
    __tablename__ = 'field'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    value = db.Column(db.String)
    status_seller = db.Column(db.Boolean)
    status_buyer = db.Column(db.Boolean)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'status_seller': self.status_seller,
            'status_buyer': self.status_buyer,
            'document_id': self.document_id,
        }

    def __repr__(self):
        return f'<Field {self.id}>'


class Ware(db.Model):
    __tablename__ = 'ware'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    okpd2 = db.Column(db.String)
    price_nds = db.Column(db.String)
    quantity = db.Column(db.String)
    units = db.Column(db.String)
    nds = db.Column(db.String)
    sum_nds = db.Column(db.String)
    adress = db.Column(db.String)
    time = db.Column(db.String)
    document_id = db.Column(db.Integer, db.ForeignKey('document.id'))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'okpd2': self.okpd2,
            'price_nds': self.price_nds,
            'quantity': self.quantity,
            'units': self.units,
            'nds': self.nds,
            'sum_nds': self.sum_nds,
            'adress': self.adress,
            'time': self.time,
            'document_id': self
        }

    def __repr__(self):
        return f'<Ware {self.id}>'

class StatusDocument(db.Model):
    __tablename__ = 'status_document'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)

    def serialize(self):
        return {
            'id': self.id,
            'type': self.type
        }

    def __repr__(self):
        return f'<StatusDocument {self.id}>'


class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    status_id = db.Column(db.Integer, db.ForeignKey('status_document.id'))
    restr_number = db.Column(db.String)
    zakup_number = db.Column(db.String)
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'status_id': self.status_id,
            'restr_number': self.restr_number,
            'zakup_number': self.zakup_number
        }

    def __repr__(self):
        return f'<Document {self.id}>'


