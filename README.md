# PyFleX

## Install
```
# ensure docker-ce is installed (https://docs.docker.com/engine/install/ubuntu/)
# ensure nvidia-docker is installed. This is by:
# sudo apt-get install -y nvidia-container-toolkit
# sudo systemctl restart docker (docker service name can be found by sudo systemctl list-units --type=service | grep -i docker)

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
echo '' >> ~/.bashrc
echo "export PYFLEXROOT=${PWD}/PyFleX" >> ~/.bashrc
echo 'export PYTHONPATH=${PYFLEXROOT}/bindings/build:$PYTHONPATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=${PYFLEXROOT}/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH' >> ~/.bashrc
echo '' >> ~/.bashrc

# finally, restart the terminal
```

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
|  2 |  ```bindings/scenes/yz_boxbathext.h``` |
|  3 | ```scenes/yz_dambreak.h``` |
|  4 | ```scenes/yz_rigidfall.h``` |
|  5 | ```scenes/yz_ricefall.h``` |
|  6 | ```scenes/yz_softbody.h``` |
|  7 | ```scenes/yz_fluidshake.h``` |
|  8 | ```scenes/yz_fluidiceshake.h``` |
|  9 | ```scenes/yz_massrope.h``` |
| 10 | ```scenes/yz_flag.h``` |
| 11 | ```scenes/yz_softrod.h``` |
| 12 | ```scenes/yz_clothrigid.h``` |
| 13 | ```scenes/yz_granular.h``` |
| 14 | ```scenes/yz_bunnygrip.h``` |
| 15 | ```scenes/yz_clothmanip.h``` |
| 16 | ```scenes/yz_softfall.h``` |
| 17 | ```scenes/yz_fluidpour.h``` |
| 18 | ```scenes/yz_granularmanip.h``` |
| 19 | ```scenes/yz_fluid_and_box.h``` |
| 20 | ```scenes/yx_coffee.h``` |
| 21 | ```scenes/yx_capsule.h``` |
| 22 | ```scenes/yx_carrots.h``` |
| 23 | ```scenes/yx_coffee_capsule.h``` |
| 24 | ```scenes/by_apple.h``` |
| 25 | ```scenes/by_singleycb.h``` |
| 26 | ```scenes/by_softrope.h``` |
| 27 | ```scenes/by_cloth.h``` |
| 28 | ```scenes/by_multiycb.h``` |
| 29 | ```scenes/by_softgym_cloth.h``` |
| 30 | ```scenes/softgym_cloth_2.h``` |
| 31 | ```scenes/by_roperigid.h``` |
| 32 | ```scenes/by_rigidgranular.h``` |
| 33 | ```scenes/adhesion.h``` |
| 34 | ```scenes/armadilloshower.h```  |
| 35 | ```scenes/bananas.h``` |
| 36 | ```scenes/bouyancy.h``` |
| 37 | ```scenes/bunnybath.h``` |
| 38 | ```scenes/ccdfluid.h``` |
| 39 | ```scenes/clothlayers.h```  |
| 40 | ```scenes/dambreak.h``` |
| 41 | ```scenes/darts.h``` |
| 42 | ```scenes/debris.h``` |
| 43 | ```scenes/deformables.h``` |
| 44 | ```scenes/fluidblock.h``` |
| 45 | ```scenes/fluidclothcoupling.h``` |
| 46 | ```scenes/forcefield.h``` |
| 47 | ```scenes/frictionmoving.h```  |
| 48 | ```scenes/frictionramp.h``` |
| 49 | ```scenes/gamemesh.h``` |
| 50 | ```scenes/googun.h``` |
| 51 | ```scenes/granularpile.h``` |
| 52 | ```scenes/granularshape.h```  |
| 53 | ```scenes/inflatable.h``` |
| 54 | ```scenes/initialoverlap.h``` |
| 55 | ```scenes/lighthouse.h``` |
| 56 | ```scenes/localspacecloth.h``` |
| 57 | ```scenes/localspacefluid.h```  |
| 58 | ```scenes/lowdimensionalshapes.h``` |
| 59 | ```scenes/melting.h``` |
| 60 | ```scenes/mixedpile.h``` |
| 61 | ```scenes/nonconvex.h``` |
| 62 | ```scenes/parachutingbunnies.h```  |
| 63 | ```scenes/pasta.h``` |
| 64 | ```scenes/player.h``` |
| 65 | ```scenes/potpourri.h``` |
| 66 | ```scenes/rayleightaylor.h``` |
| 67 | ```scenes/restitution.h```  |
| 68 | ```scenes/rigidfluidcoupling.h``` |
| 69 | ```scenes/rigidpile.h``` |
| 70 | ```scenes/rigidrotation.h``` |
| 71 | ```scenes/rockpool.h``` |
| 72 | ```scenes/sdfcollision.h``` |
| 73 | ```scenes/shapecollision.h``` |
| 74 | ```scenes/shapechannels.h``` |
| 75 | ```scenes/softbody.h``` |
| 76 | ```scenes/spherecloth.h``` |
| 77 | ```scenes/surfacetension.h``` |
| 78 | ```scenes/tearing.h``` |
| 79 | ```scenes/thinbox.h``` |
| 80 | ```scenes/trianglecollision.h``` |
| 81 | ```scenes/triggervolume.h``` |
| 82 | ```scenes/viscosity.h```  |
| 83 | ```scenes/waterballoon.h``` |
