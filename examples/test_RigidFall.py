import os
import numpy as np
import pyflex
import cv2


# user-configurable params
OUT_DIR = 'out/test_RigidFall'  # output directory
N_INSTANCES = 10000     # number of instances of the object to drop
BOX_WIDTH, BOX_HEIGHT, BOX_DEPTH = 1, 0.5, 1  # box dimensions
SCREEN_HEIGHT, SCREEN_WIDTH = 720, 720  # screen dimensions (CAVEAT: at the moment, only (720, 720) is supported)
CAM_X, CAM_Y, CAM_Z = 0.5, 10.0, 0.5  # camera position
CAM_ROLL, CAM_PITCH, CAM_YAW = 0, -15, 0  # camera orientation (degree)
LIGHT_ROLL, LIGHT_PITCH, LIGHT_YAW = 5, 15, 7.5  # light orientation (rad)
DRAW_MESH = False  # whether to draw the mesh
SIM_HORIZON = 1000  # simulation horizon, i.e., # of steps

# constants
kSCENE_INDEX = 4
kGRAVITY = -9.8

# helper functions
def random_float(lb, ub):
    return lb + (ub - lb) * np.random.rand()

def sample_pos_in_box(box_width=BOX_WIDTH, box_height=BOX_HEIGHT, box_depth=BOX_DEPTH):
    x = random_float(-box_width / 2, box_width / 2)
    y = random_float(0, box_height)
    z = random_float(-box_depth / 2, box_depth / 2)
    return np.array([x, y, z])

# init pyflex
os.makedirs(OUT_DIR, exist_ok=True)
pyflex.init(headless=False)

# setup scene params
scene_params = np.zeros(N_INSTANCES * 3 + 3)
scene_params[0] = N_INSTANCES
scene_params[1] = kGRAVITY
lb = 0.09
for i in range(N_INSTANCES):
    # scene_params[3 * i + 2:3 * i + 5] = sample_pos_in_box()
    scene_params[3 * i + 2] = random_float(0, 0.5)
    scene_params[3 * i + 3] = random_float(lb, lb + 0.01)
    scene_params[3 * i + 4] = random_float(0, 0.5)
    lb += 0.21
scene_params[-1] = DRAW_MESH

# setup scene
pyflex.set_scene(kSCENE_INDEX, scene_params, thread_idx=0)

print("Scene Upper:", pyflex.get_scene_lower())
print("Scene Lower:", pyflex.get_scene_upper())

# setup camera
cam_pos = np.array([CAM_X, CAM_Y, CAM_Z])
cam_angle = np.array([np.deg2rad(CAM_ROLL), np.deg2rad(CAM_PITCH), np.deg2rad(CAM_YAW)])
pyflex.set_camPos(cam_pos)
pyflex.set_camAngle(cam_angle)

# setup light
light_dir = np.array([LIGHT_ROLL, LIGHT_PITCH, LIGHT_YAW])
light_fov = 70.
pyflex.set_light_dir(light_dir / np.linalg.norm(light_dir))
pyflex.set_light_fov(light_fov)

# simulate and render
for i in range(SIM_HORIZON):
    pyflex.step()

    img = pyflex.render(render_depth=True) \
                .reshape(SCREEN_HEIGHT, SCREEN_WIDTH, 5)  # RGBA + D
    rgb = img[..., :3]
    depth = (img[..., -1] * 1000).astype(np.uint16)

    cv2.imwrite(os.path.join(OUT_DIR, f'render_{i:04d}_rgb.png'), cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))
    cv2.imwrite(os.path.join(OUT_DIR, f'render_{i:04d}_depth.png'), depth)

pyflex.clean()