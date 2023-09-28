PyFleX
======

Install with docker
------------

    docker pull xingyu/softgym
    docker run \
        -v ${PWD}:/workspace/PyFleX \
        -v ${CONDA_PREFIX}:/workspace/anaconda \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        --gpus all \
        -e DISPLAY=$DISPLAY \
        -e QT_X11_NO_MITSHM=1 \
        -it xingyu/softgym:latest bash \
        -c "export PATH=/workspace/anaconda/bin:$PATH; cd /workspace/PyFleX; export PYFLEXROOT=/workspace/PyFleX; export PYTHONPATH=/workspace/PyFleX/bindings/build:$PYTHONPATH; export LD_LIBRARY_PATH=$PYFLEXROOT/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH; cd bindings; mkdir build; cd build; /usr/bin/cmake ..; make -j"

Add following to ~/.bashrc

    export PYFLEXROOT=${PWD}
    export PYTHONPATH=${PYFLEXROOT}/bindings/build:$PYTHONPATH
    export LD_LIBRARY_PATH=${PYFLEXROOT}/external/SDL2-2.0.4/lib/x64:$LD_LIBRARY_PATH
