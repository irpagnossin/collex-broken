from jinjaconfig import create_tex
from math import sin, pi

def create():
	def acceleration(m1, m2, m3, φ, r, g):
		angle = φ/180 * pi
		return (m1 - m2 * sin(angle)) * g / (m1 + 3/2 * m2 + 1/2 * m3)

	def torque(m1, m2, m3, φ, r, g):
		a = acceleration(m1, m2, m3, φ, r, g)
		return m3 * r * a / 2

	def format(x):
		return "{:.2e}".format(x)

	def generate_data(m1, m2, m3, φ, r, g):

		# O texto da questão trata do fato de a aceleração (e o torque) serem negativos
		assert(acceleration(m1, m2, m3, φ, r, g) < 0)

		data = {
			'm1': format(m1),
			'm2': format(m2),
			'm3': format(m3),
			'φ': φ,
			'r': format(r),
			'g': format(g),
			'acceleration': acceleration(m1, m2, m3, φ, r, g),
			'torque': torque(m1, m2, m3, φ, r, g),
		    'answer_item_2':format(acceleration(m1, m2, m3, φ, r, g)),
		    'answer_item_3':format(abs(torque(m1, m2, m3, φ, r, g))),
		    'format':format
		}

		return data

	# Parâmetros do problema
	variations = {
		'A': {
			'm1': 1, # kg
			'm2': 4, # kg
			'm3': 4, # kg
			'φ': 30, # graus
			'r': 0.05, # m
			'g': 10, # m/s^2 (aceleração da gravidade)
		},
		'B': {
			'm1': 2,
			'm2': 5,
			'm3': 0.3,
			'φ': 30,
			'r': 0.05,
			'g': 10,
		},
		'C': {
			'm1': 1,
			'm2': 4,
			'm3': 0.3,
			'φ': 30,
			'r': 0.05,
			'g': 10,
		},
		'D': {
			'm1': 2,
			'm2': 4.5,
			'm3': 0.5,
			'φ': 30,
			'r': 0.05,
			'g': 10,
		},
		'E': {
			'm1': 1,
			'm2': 2.5,
			'm3': 0.8,
			'φ': 30,
			'r': 0.05,
			'g': 10,
		},
	}

	for (variation, parameters) in variations.items():
		try:
			create_tex(__file__, generate_data(**parameters), variation)
		except AssertionError:
			print("ERRO: variação {} não é coerente com o texto.".format(variation))

if __name__ == '__main__':
	create()
