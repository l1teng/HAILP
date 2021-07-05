## APT Mirror Help Center

#### Supported Architechtures

- ```Ubuntu 18.04 LTS```

#### Configuration

- **HFUT inner net**
```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb http://172.18.220.5/ubuntu/ bionic main restricted universe multiverse
# deb-src http://172.18.220.5/ubuntu/ bionic main restricted universe multiverse
deb http://172.18.220.5/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src http://172.18.220.5/ubuntu/ bionic-updates main restricted universe multiverse
deb http://172.18.220.5/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src http://172.18.220.5/ubuntu/ bionic-backports main restricted universe multiverse
deb http://172.18.220.5/ubuntu/ bionic-security main restricted universe multiverse
# deb-src http://172.18.220.5/ubuntu/ bionic-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb http://172.18.220.5/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src http://172.18.220.5/ubuntu/ bionic-proposed main restricted universe multiverse
```


- **HFUTAIL inner net**
```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb http://192.168.1.80/ubuntu/ bionic main restricted universe multiverse
# deb-src http://192.168.1.80/ubuntu/ bionic main restricted universe multiverse
deb http://192.168.1.80/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src http://192.168.1.80/ubuntu/ bionic-updates main restricted universe multiverse
deb http://192.168.1.80/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src http://192.168.1.80/ubuntu/ bionic-backports main restricted universe multiverse
deb http://192.168.1.80/ubuntu/ bionic-security main restricted universe multiverse
# deb-src http://192.168.1.80/ubuntu/ bionic-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb http://192.168.1.80/ubuntu/ bionic-proposed main restricted universe multiverse
# deb-src http://192.168.1.80/ubuntu/ bionic-proposed main restricted universe multiverse
```