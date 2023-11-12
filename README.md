# install PyFleX

```
# this follows the instructions in https://github.com/WangYixuan12/dyn-res-pile-manip/
# ensure docker-ce is installed (https://docs.docker.com/engine/install/ubuntu/)
# ensure nvidia-docker is installed. This is by:
# sudo apt-get install -y nvidia-container-toolkit
# sudo systemctl restart docker (docker service name can be found by sudo systemctl list-units --type=service | grep -i docker)
cd third-party
git clone git@github.com:kywind/PyFleX.git
conda install pybind11 -c conda-forge  # or pip install "pybind11[global]"

CURR_CONDA=$CONDA_DEFAULT_ENV
CONDA_BASE=$(conda info --base)
docker pull xingyu/softgym
# make sure ${PWD}/PyFleX is the pyflex root path when re-compiling
docker run \
    -v ${PWD}/PyFleX:/workspace/PyFleX \
    -v ${CONDA_PREFIX}:/workspace/anaconda \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    --gpus all \
    -e DISPLAY=$DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    -it xingyu/softgym:latest bash \
    -c "export PATH=/workspace/anaconda/bin:$PATH; cd /workspace/PyFleX; export PYFLEXROOT=/workspace/PyFleX; export PYTHONPATH=/workspace/PyFleX/bindings/build:$PYTHONPATH; export LD_LIBRARY_PATH=$PYFLEXROOT/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH; cd bindings; mkdir build; cd build; /usr/bin/cmake ..; make -j"

echo '' >> ~/.bashrc
echo '# PyFleX' >> ~/.bashrc
echo "export PYFLEXROOT=${PWD}/PyFleX" >> ~/.bashrc
echo 'export PYTHONPATH=${PYFLEXROOT}/bindings/build:$PYTHONPATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=${PYFLEXROOT}/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH' >> ~/.bashrc
echo '' >> ~/.bashrc

source ~/.bashrc
source $CONDA_BASE/etc/profile.d/conda.sh
conda activate $CURR_CONDA
cd ..
