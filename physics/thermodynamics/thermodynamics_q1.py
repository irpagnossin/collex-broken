from jinjaconfig import create_tex

def create():

	def heat_item_1(V, c, T, T1, ρ):
		return ρ * V * c * abs(T1 - T)

	def answer_item_1(V, c, T, dt, T1, ρ):
		return heat_item_1(V, c, T, T1, ρ) / dt

	def answer_item_2(V, c, T, dt, T1, L, ρ):
		return V * L / answer_item_1(V, c, T, dt, T1, ρ)

	def format(x):
		return "{:.2e}".format(x)

	def latent_heat(m, L):
		return m * L

	def generate_data(V, T, dt):
		# Propriedades da água
		c = 4.19e3 # J/kg.K (calor específico)
		L = 2.26e6 # J/kg (calor latente de ebulição)
		Te = 373 # K (temperatura de ebulição)
		ρ = 0.999 # kg/l (densidade)

		# Informações derivadas
		m = ρ * V

		data = {
			'V':V,
			'T':T,
			'dt':dt,
			'c':c,
			'L':L,
			'Te':Te,
			'ρ':ρ,
			'heat_item_1': format(heat_item_1(V, c, T, Te, ρ)),
			'vaporization_heat': format(latent_heat(m,L)),
			'answer_item_1':format(answer_item_1(V, c, T, dt, Te, ρ)),
		    'answer_item_2':format(answer_item_2(V, c, T, dt, Te, L, ρ)),
		    'format':format
		}

		return data

	# Parâmetros do problema
	variations = {
		'A': {
			'V': 700e-3, # l (volume de água)
			'T': 288, # K (temperatura ambiente)
			'dt': 6 # min (intervalo de tempo)
		},
		'B': {
			'V': 100e-3,
			'T': 300,
			'dt': 1
		}
	}

	for (variation, parameters) in variations.items():
		create_tex(__file__, generate_data(**parameters), variation)

if __name__ == '__main__':
	create()
