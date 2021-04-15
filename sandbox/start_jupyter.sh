#!/bin/bash
nohup jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token='' > /dev/null 2>&1 & 