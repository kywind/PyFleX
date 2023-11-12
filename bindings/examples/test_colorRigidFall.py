import numpy as np
import pyflex
import time
import torch


def rand_float(lo, hi):
	return np.random.rand() * (hi - lo) + lo


pyflex.init(False)
n_instance = 3
n_particles = n_instance * 64

scene_params = np.zeros(n_instance * 3 + 1)
scene_params[0] = n_instance

low_bound = 0.09
for i in range(n_instance):
	x = rand_float(0., 0.1)
	y = rand_float(low_bound, low_bound + 0.01)
	z = rand_float(0., 0.1)

	scene_params[i * 3 + 1] = x
	scene_params[i * 3 + 2] = y
	scene_params[i * 3 + 3] = z

	low_bound += 0.21

pyflex.set_scene(3, scene_params, 0)

print("Scene Upper:", pyflex.get_scene_lower())
print("Scene Lower:", pyflex.get_scene_upper())

pp = [[rand_float(0., 0.1), rand_float(0., 0.1), rand_float(0., 0.1), 0.] for i in range(n_particles)]

phases = [i%n_instance for i in range(n_particles)]
print(phases)
pyflex.set_phases(phases)

for i in range(150):
	pyflex.render()
	print(pyflex.get_phases())

	if i == 0:
		time.sleep(1)

pyflex.clean()
