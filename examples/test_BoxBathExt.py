import os
import numpy as np
import pyflex
import cv2


def rand_float(lo, hi):
    return np.random.rand() * (hi - lo) + lo

x = rand_float(0.15, 0.349)
y = rand_float(0.15, 0.349)
z = rand_float(0.15, 0.299)
px = rand_float(0.45, 1.2 - x)
pz = rand_float(0.02, 0.4 - z)

# x range [3, 7] --> [0.15, 0.399]
# y range [3, 7] --> [0.15, 0.399]
# z range [3, 6] --> [0.15, 0.349]
# x = 0.349
# y = 0.349
# z = 0.299
# px = 1.2 - x
# pz = 0.4 - z

# init pyflex
pyflex.init(headless=False)

scene_idx = 2
scene_params = np.array([x, y, z, px, pz])
pyflex.set_scene(scene_idx, scene_params, thread_idx=0)

# get scene bounds
print("Scene Upper:", pyflex.get_scene_upper())
print("Scene Lower:", pyflex.get_scene_lower())

# display options
screenHeight = 720
screenWidth = 720

cam_X = 0.6
cam_Y = 1.0  # height
cam_Z = 2.0
camPos = np.array([cam_X, cam_Y, cam_Z])
camAngle = np.array([np.deg2rad(0.), np.deg2rad(-15.), 0.])  # 0: yaw, 1: pitch, 2: not used
pyflex.set_camPos(camPos)
pyflex.set_camAngle(camAngle)

light_dir = np.array([5.0, 15.0, 7.5])  # light direction for shadings
light_fov = 0.
pyflex.set_light_dir(light_dir / np.linalg.norm(light_dir)) 
pyflex.set_light_fov(light_fov)

# save dir
des_dir = 'out/test_BoxBathExt'
os.makedirs(des_dir, exist_ok=True)

# main loop
max_time_step = 150
for i in range(0, max_time_step):
    # simulate one step
    pyflex.step()

    # render
    img = pyflex.render(render_depth=True).reshape(screenHeight, screenWidth, 5)  # RGBA + D
    rgb = img[:, :, :3]
    depth = (img[:, :, -1] * 1000).astype(np.uint16)

    # save to file
    cv2.imwrite(os.path.join(des_dir, 'render_%d_rgb.png' % i), cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))
    cv2.imwrite(os.path.join(des_dir, 'render_%d_depth.png' % i), depth)

pyflex.clean()
