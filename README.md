# PyFleX

## Install
```
# 1) install anaconda (https://docs.anaconda.com/free/anaconda/install/linux/)
# 2) install docker-ce (https://docs.docker.com/engine/install/ubuntu/)
# 3) install nvidia-container-toolkit (https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
# 4) restart docker by `sudo systemctl restart docker` (docker service name can be found by `sudo systemctl list-units --type=service | grep -i docker`)

# preparations
cd third-party
git clone git@github.com:kywind/PyFleX.git
conda install pybind11 -c conda-forge  # or pip install "pybind11[global]"
sudo docker pull xingyu/softgym

# compile pyflex in docker image
# re-compile if source code changed
# make sure ${PWD}/PyFleX is the pyflex root path when re-compiling
sudo docker run \
    -v ${PWD}/PyFleX:/workspace/PyFleX \
    -v ${CONDA_PREFIX}:/workspace/anaconda \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --gpus all \
    -e DISPLAY=$DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    -it xingyu/softgym:latest bash \
    -c "export PATH=/workspace/anaconda/bin:$PATH; cd /workspace/PyFleX; export PYFLEXROOT=/workspace/PyFleX; export PYTHONPATH=/workspace/PyFleX/bindings/build:$PYTHONPATH; export LD_LIBRARY_PATH=$PYFLEXROOT/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH; cd bindings; mkdir build; cd build; /usr/bin/cmake ..; make -j"

# run these if you do not have these paths yet in ~/.bashrc
echo '# PyFleX' >> ~/.bashrc
echo "export PYFLEXROOT=${PWD}/PyFleX" >> ~/.bashrc
echo 'export PYTHONPATH=${PYFLEXROOT}/bindings/build:$PYTHONPATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=${PYFLEXROOT}/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH' >> ~/.bashrc
echo '' >> ~/.bashrc

# finally, restart the terminal
```

## Try pre-compiled demo
click on /PyFleX/precompiled_demo/linux64/NvFlexDemoReleaseCUDA_x64 or run `./precompiled_demo/linux64/NvFlexDemoReleaseCUDA_x64` inside /PyFleX.


## Run Examples
```
python examples/test_BoxBath.py
```

## Scenes
**NOTE: Not all scenes are supported yet. (I'm working on this now.) Check example python files under ```examples/``` for supported scenes!**
```
# Example usage
scene_idx = your_scene_idx
scene_params = np.array([your_scene_params])
pyflex.set_scene(scene_idx, scene_params, 0)
```

| scene_idx | Source |
|:-----------:|:-------:|
|  0 | ```bindings/scenes/yz_bunnybath.h``` |
|  1 | ```bindings/scenes/yz_boxbath.h``` |
|  2 | ```bindings/scenes/yz_boxbathext.h``` |
|  3 | ```bindings/scenes/yz_dambreak.h``` |
|  4 | ```bindings/scenes/yz_rigidfall.h``` |
|  5 | ```bindings/scenes/yz_ricefall.h``` |
|  6 | ```bindings/scenes/yz_softbody.h``` |
|  7 | ```bindings/scenes/yz_fluidshake.h``` |
|  8 | ```bindings/scenes/yz_fluidiceshake.h``` |
|  9 | ```bindings/scenes/yz_massrope.h``` |
| 10 | ```bindings/scenes/yz_flag.h``` |
| 11 | ```bindings/scenes/yz_softrod.h``` |
| 12 | ```bindings/scenes/yz_clothrigid.h``` |
| 13 | ```bindings/scenes/yz_granular.h``` |
| 14 | ```bindings/scenes/yz_bunnygrip.h``` |
| 15 | ```bindings/scenes/yz_clothmanip.h``` |
| 16 | ```bindings/scenes/yz_softfall.h``` |
| 17 | ```bindings/scenes/yz_fluidpour.h``` |
| 18 | ```bindings/scenes/yz_granularmanip.h``` |
| 19 | ```bindings/scenes/yz_fluid_and_box.h``` |
| 20 | ```bindings/scenes/yx_coffee.h``` |
| 21 | ```bindings/scenes/yx_capsule.h``` |
| 22 | ```bindings/scenes/yx_carrots.h``` |
| 23 | ```bindings/scenes/yx_coffee_capsule.h``` |
| 24 | ```bindings/scenes/by_apple.h``` |
| 25 | ```bindings/scenes/by_singleycb.h``` |
| 26 | ```bindings/scenes/by_softrope.h``` |
| 27 | ```bindings/scenes/by_cloth.h``` |
| 28 | ```bindings/scenes/by_multiycb.h``` |
| 29 | ```bindings/scenes/by_softgym_cloth.h``` |
| 30 | ```bindings/scenes/softgym_cloth_2.h``` |
| 31 | ```bindings/scenes/by_roperigid.h``` |
| 32 | ```bindings/scenes/by_rigidgranular.h``` |
| 33 | ```bindings/scenes/by_rigidcloth.h``` |
| 34 | ```bindings/scenes/by_ropecloth.h``` |
| 35 | ```bindings/scenes/by_granular.h``` |
| 36 | ```bindings/scenes/by_bowlfluid.h``` |
| 37 | ```bindings/scenes/by_softbody.h``` |
| 38 | ```bindings/scenes/by_ropegranular.h``` |
| 39 | ```bindings/scenes/by_rigidrope.h``` |
<!--
| 40 | ```bindings/scenes/adhesion.h``` |
| 41 | ```bindings/scenes/armadilloshower.h```  |
| 42 | ```bindings/scenes/bananas.h``` |
| 43 | ```bindings/scenes/bouyancy.h``` |
| 44 | ```bindings/scenes/bunnybath.h``` |
| 45 | ```bindings/scenes/ccdfluid.h``` |
| 46 | ```bindings/scenes/clothlayers.h```  |
| 47 | ```bindings/scenes/dambreak.h``` |
| 48 | ```bindings/scenes/darts.h``` |
| 49 | ```bindings/scenes/debris.h``` |
| 50 | ```bindings/scenes/deformables.h``` |
| 51 | ```bindings/scenes/fluidblock.h``` |
| 52 | ```bindings/scenes/fluidclothcoupling.h``` |
| 53 | ```bindings/scenes/forcefield.h``` |
| 54 | ```bindings/scenes/frictionmoving.h```  |
| 55 | ```bindings/scenes/frictionramp.h``` |
| 56 | ```bindings/scenes/gamemesh.h``` |
| 57 | ```bindings/scenes/googun.h``` |
| 58 | ```bindings/scenes/granularpile.h``` |
| 59 | ```bindings/scenes/granularshape.h```  |
| 60 | ```bindings/scenes/inflatable.h``` |
| 61 | ```bindings/scenes/initialoverlap.h``` |
| 62 | ```bindings/scenes/lighthouse.h``` |
| 63 | ```bindings/scenes/localspacecloth.h``` |
| 64 | ```bindings/scenes/localspacefluid.h```  |
| 65 | ```bindings/scenes/lowdimensionalshapes.h``` |
| 66 | ```bindings/scenes/melting.h``` |
| 67 | ```bindings/scenes/mixedpile.h``` |
| 68 | ```bindings/scenes/nonconvex.h``` |
| 69 | ```bindings/scenes/parachutingbunnies.h```  |
| 70 | ```bindings/scenes/pasta.h``` |
| 71 | ```bindings/scenes/player.h``` |
| 72 | ```bindings/scenes/potpourri.h``` |
| 73 | ```bindings/scenes/rayleightaylor.h``` |
| 74 | ```bindings/scenes/restitution.h```  |
| 75 | ```bindings/scenes/rigidfluidcoupling.h``` |
| 76 | ```bindings/scenes/rigidpile.h``` |
| 77 | ```bindings/scenes/rigidrotation.h``` |
| 78 | ```bindings/scenes/rockpool.h``` |
| 79 | ```bindings/scenes/sdfcollision.h``` |
| 80 | ```bindings/scenes/shapecollision.h``` |
| 81 | ```bindings/scenes/shapechannels.h``` |
| 82 | ```bindings/scenes/softbody.h``` |
| 83 | ```bindings/scenes/spherecloth.h``` |
| 84 | ```bindings/scenes/surfacetension.h``` |
| 85 | ```bindings/scenes/tearing.h``` |
| 86 | ```bindings/scenes/thinbox.h``` |
| 87 | ```bindings/scenes/trianglecollision.h``` |
| 88 | ```bindings/scenes/triggervolume.h``` |
| 89 | ```bindings/scenes/viscosity.h```  |
| 90 | ```bindings/scenes/waterballoon.h``` |
-->
