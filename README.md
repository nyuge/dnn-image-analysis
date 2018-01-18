Image data analysis with OpenCV & DNN tools
==============================

This is my workspace for treating time-series image data with DNN.
`Dockerfile.cpu` in here was inspired from
https://github.com/floydhub/dl-docker and
https://github.com/waleedka/modern-deep-learning-docker .
A lot of apprications !!!


## Specs
+ Ubuntu16.04
+ Python3.5.3
  - opencv
  - tensorflow
  - Keras


## Building environments
This project stands with __docker__ for preparing environmental and running analyses.
The basic usages of __docker__ are guided in https://www.docker.com/ .

First, you type a command to build a docker-image as follows...
```bash
  $ docker build -f Dockerfile.cpu -t nyuge/dnn-image-analysis:cpu .
```

Next, you type a command to generate a docker-container, mount the folder (workspace/) and attach to bash as follows...
```bash
  $ docker run -i -p 8080:8080 -p 8888:8888 -v /$(pwd):/workspace --name nb-server-01 -t nyuge/dnn-image-analysis:cpu bash
```

After you move to shell in docker-container, you type a command to build a jupyter nb. server as follows...
```bash
  $ jupyter notebook --allow-root
```

You can access the jypyter nb. server via "192.168.99.100:8888" by default.

You can escape form docker-container by typing `exit` .

If the container is exhausted by analyses, you type a command for removing it as follows...
```bash
  $ docker rm nb-server-01
```
