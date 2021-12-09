#!/bin/bash
#!/bin/bash
# install_pi.sh

echo "Installing base dependencies"
sudo apt-get update
sudo apt-get install -y \
    python3-pip \
    python3-pil \
    python3-numpy \
    python3-h5py \
    gcc \
    make \
    build-essential \
    libopenjp2-7 \
    libilmbase-dev \
    libopenexr-dev \
    libgstreamer1.0-dev \
    libavcodec-dev \
    libopencv-dev \
    python-opencv \
    python-picamera \
    libhdf5-dev \
    libatlas-base-dev \
    libjasper-dev


cd ../

echo "Installing python dependencies";
python3 -m pip install virtualenv

python3 -m virtualenv -p python3 env
. env/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r src/requirements.txt


echo "Setup complete";
