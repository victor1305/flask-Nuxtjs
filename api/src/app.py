from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1111@localhost/transporter' #Donde se encuentra la BBDD, viene en la documentación de SQL Alchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Configuración por defecto para que cuando ejecutemos el programa no nos de un warning

cors = CORS(app, resources = {r"/*": {"origins": "http://localhost:3000"}})

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Partner(db.Model): #ORM Crea las tablas en mySql con estos datos: (el id se crea por si mismo)
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70), unique = True)
    address = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    web = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, address, phone, web, created): #definimos los campos
        self.name = name
        self.address = address
        self.phone = phone
        self.web = web
        self.created = created

db.create_all()

class PartnerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'phone', 'web', 'created')

partner_schema = PartnerSchema()
partners_schema = PartnerSchema(many = True) #Con esto habilito la posibilidad de recibir multiples respuestas de la BBDD

# Defino los EP

# CREATE

@app.route('/new', methods = ['POST'])
def create_partner():

    #Guardo los datos en variables:

    name = request.json['name']
    address = request.json['address']
    phone = request.json['phone']
    web = request.json['web']
    created = datetime.now()
    new_partner = Partner(name, address, phone, web, created) #Con esto se crea una nueva tarea que se guarda en la variable "newPartner"

    #El siguiente paso es guardarlo en la BBDD

    db.session.add(new_partner)
    db.session.commit()

    # Despues del proceso el servidor responde mostrando la tarea guardada al cliente

    return partner_schema.jsonify(new_partner)


# READ with querys

@app.route('/', methods = ['POST', 'GET'])
def get_partners():

    if request.json['order'] == 'az':
        query = Partner.query.order_by(Partner.name).all()
        result = partners_schema.dump(query)

    elif request.json['order'] == 'za':
        query = Partner.query.order_by(Partner.name.desc()).all()
        result = partners_schema.dump(query)

    elif request.json['order'] == 'oldFirst':
        query = Partner.query.order_by(Partner.created.desc()).all()
        result = partners_schema.dump(query)

    elif request.json['order'] == 'newFirst':
        query = Partner.query.order_by(Partner.created).all()
        result = partners_schema.dump(query)

    else:
        allPartners = Partner.query.all()
        result = partners_schema.dump(allPartners)

    return jsonify(result) #Jsonify convierte string en json


# DELETE

@app.route('/<id>', methods = ['DELETE'])
def delete_partner(id):

    partner = Partner.query.get(id)

    db.session.delete(partner)
    db.session.commit()

    return partner_schema.jsonify(partner)

if __name__ == "__main__":
    app.run(debug = True)