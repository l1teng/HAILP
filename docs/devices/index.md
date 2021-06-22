## Hardware Settings

<br>

### GPU Servers

- Mul-GPU server

![](https://img.shields.io/badge/Ubuntu-18.04LTS-orange)
![](https://img.shields.io/badge/Intel-I7--9700K-blue)
![](https://img.shields.io/badge/RAM-64 GB-blue)
![](https://img.shields.io/badge/Nvidia-Titan Xp-green)
![](https://img.shields.io/badge/Nvidia-Titan Xp-green)

<br>

### NAS

- Nas server

![](https://img.shields.io/badge/Ubuntu-18.04LTS-orange)
![](https://img.shields.io/badge/Intel-I5--10400f-blue)
![](https://img.shields.io/badge/RAM-8 GB-blue)
![](https://img.shields.io/badge/HDD-WD 4T-black)
![](https://img.shields.io/badge/HDD-Toshiba 3T-red)

<br>

## GPU Server Configuration

<br>

### System initialize

Recommand server system, **Ubuntu-18.04-live-server-amd64**, which can be downloaded [**here**](http://172.18.220.5/_public/softwares/OS/Ubuntu/ubuntu-18.04.5-live-server-amd64.iso).

- **Install docker, details can be checked [here](https://www.runoob.com/docker/ubuntu-docker-install.html)**.

recommand script,

```
curl -sSL https://get.daocloud.io/docker | sh
```

- **Install graphic card driver**

check for the latest available drivers list via,

```
sudo apt install ubuntu-drivers​-common
ubuntu-drivers devices
```

install via,

```
sudo apt install nvidia-driver-xxxx
```

then reboot via,

```
sudo reboot
```

- **Install nvidia-docker, details can be checked [here](https://zhuanlan.zhihu.com/p/76464450)**.

```
#If you have nvidia-docker 1.0 installed: we need to remove it and all existing GPU containers
docker volume ls -q -f driver=nvidia-docker|xargs -r -I{} -n1 docker ps -q -a -f volume={}|xargs -r docker rm -f  
sudo apt-get purge -y nvidia-docker

# Add the package repositories
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update

# Install nvidia-docker2 and reload the Docker daemon configuration
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP docker
```

test install status via, 


```
docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi
```

<br>

### Docker node configuration

- **node with 2 gpus**

```
nvidia-docker run -it -d --name='base_2gpu' -v <data dir>:/workspace -e NVIDIA_VISIBLE_DEVICES=0,1 -p <port>:22 --restart=always terrytengli/ail:torch-1.4-gpu
```

- **node with 1 gpu**

```
nvidia-docker run -it -d --name='base_1gpu' -v <data dir>:/workspace -e NVIDIA_VISIBLE_DEVICES=0 -p <port>:22 --restart=always terrytengli/ail:torch-1.4-gpu
```
