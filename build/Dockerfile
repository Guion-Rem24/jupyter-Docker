FROM nvidia/cuda:10.2-cudnn8-devel-ubuntu16.04

ENV HTTP_PROXY=http://proxy.uec.ac.jp:8080/
ENV HTTPS_PROXY=http://proxy.uec.ac.jp:8080/ 
# set UserName
ENV User=mine

# set Passwd if you need
ENV JUPYTER_PASSWD=
# change Port if you want to change
ENV JUPYTER_PORT=8888



USER root
RUN cat /etc/lsb-release
RUN echo 'Acquire::http::Proxy "http://proxy.uec.ac.jp:8080";' >> /etc/apt/apt.conf\
    && echo 'Acquire::https::Proxy "http://proxy.uec.ac.jp:8080";' >> /etc/apt/apt.conf

RUN apt-get update && apt-get install -y && apt-get upgrade -y
RUN useradd -m ${User}
RUN apt-get install -y apt-utils build-essential git bash-completion gnupg2 curl apt-transport-https python
RUN curl -O https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python get-pip.py
COPY sandbox/requirements.txt /root/
RUN pip install -r /root/requirements.txt
RUN jupyter notebook --generate-config
COPY sandbox/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py
# RUN cat /home/${User}/sandbox/jupyter_notebook_config.py > /root/.jupyter/jupyter_notebook_config.py
COPY sandbox/start_jupyter.sh /root/
RUN cd /root && chmod +x start_jupyter.sh 

# ENV TINI_VERSION v0.6.0
# ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
# RUN chmod +x /usr/bin/tini
# ENTRYPOINT ["/usr/bin/tini", "-g", "--"]
# EXPOSE ${JUPYTER_PORT}

# CMD [ "./start_jupyter.sh", "${JUPYTER_PORT}", "${JUPYTER_PASSWD}" ]