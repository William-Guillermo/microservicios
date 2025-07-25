from flask import Flask, jsonify
from faker import Faker
import itertools

app = Flask(__name__)
faker = Faker()

def random_data():
	profiles = [dict(itertools.islice(faker.profile().items(),6)) for data in range(5)]
	return profiles

@app.route('/crear_registros')
def create_profiles():
	try:
		data_profiles = random_data()
		#imprime los datos en consola
		#print(data_profiles)
		#return{"message:":"Hola desde crear registros"}
		# returna los datos en formato json con  el paquete jsonify
		return jsonify(data_profiles)
	except:
		return{"message:":"Error en el endpoint de crear registros"}

if  __name__ == '__main__':
	app.run(host = '0.0.0.0',port = 3000, debug= True)
