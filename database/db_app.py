from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# for now, we have only dummy data
# TODO create connection to sqlite database

data = {'a': 1, 'b': 2, 'c': 3}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///sensor_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)


class Ds18b20(db.Model):
    db_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, unique=True, nullable=False)
    temperature = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'{self.timestamp}: {self.temperature:02f}'

    @property
    def serialize(self):
        return {'id': self.db_id,
                'timestamp': self.timestamp,
                'temperature': self.temperature}


class Temperature(Resource):

    def get(self):
        return jsonify([x.serialize for x in Ds18b20.query.all()])


api.add_resource(Temperature, '/ds18b20')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
