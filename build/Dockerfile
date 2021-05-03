FROM nvcr.io/nvidia/tensorflow:21.03-tf1-py3

ENV HTTP_PROXY=http://proxy.uec.ac.jp:8080/
ENV HTTPS_PROXY=http://proxy.uec.ac.jp:8080/ 

ARG User
ARG JUPYTER_PASSWD
ARG JUPYTER_PORT
ARG JUPYTER_WORK_DIR

EXPOSE ${JUPYTER_PORT}

ENV JUPYTER_PORT=${JUPYTER_PORT}


USER root
RUN echo ${User}
RUN cat /etc/lsb-release

# synbolic link to avoid hanging
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Comment out below RUN If not use Proxy
RUN echo 'Acquire::http::Proxy "http://proxy.uec.ac.jp:8080";' >> /etc/apt/apt.conf\
    && echo 'Acquire::https::Proxy "http://proxy.uec.ac.jp:8080";' >> /etc/apt/apt.conf


RUN apt-get update && apt-get install -y && apt-get upgrade -y
RUN apt install -y tzdata software-properties-common
RUN useradd -m ${User}
RUN apt-get install -y apt-utils build-essential git bash-completion gnupg2 curl apt-transport-https nano tree bzip2-doc libncurses-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev zlib1g-dev wget llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev sudo 
RUN gpasswd -a ${User} sudo
RUN groupadd wheel
RUN gpasswd -a ${User} wheel
RUN gpasswd -a root wheel

RUN echo 'export JUPYTER_PORT=${JUPYTER_PORT}' >> /root/.bashrc
RUN echo 'export JUPYTER_PASSWD=${JUPYTER_PASSWD}' >> /root/.bashrc
RUN echo 'export JUPYTER_PORT=${JUPYTER_PORT}' >> /home/${User}/.bashrc
RUN echo 'export JUPYTER_PASSWD=${JUPYTER_PASSWD}' >> /home/${User}/.bashrc
RUN echo 'export PATH=/home/${User}/.local/bin:$PATH' >> /home/mine/.bashrc

ENV PATH /home/${User}/.local/bin:$PATH
# Jupyter Config
USER ${User}
RUN pip install jupyter
RUN jupyter notebook --generate-config
USER root
COPY sandbox/jupyter_notebook_config.py /home/${User}/.jupyter/jupyter_notebook_config.py
COPY sandbox/start_jupyter.sh /home/${User}
RUN chmod +x /home/${User}/start_jupyter.sh 
# -- write configuration into jupyter_notebook_config.py
RUN echo '' >> /home/${User}/.jupyter/jupyter_notebook_config.py
RUN echo 'c.NotebookApp.port = '${JUPYTER_PORT} >> /home/${User}/.jupyter/jupyter_notebook_config.py
RUN echo -n 'c.NotebookApp.token = "' >> /home/${User}/.jupyter/jupyter_notebook_config.py
RUN echo -n ${JUPYTER_PASSWD} >> /home/${User}/.jupyter/jupyter_notebook_config.py
RUN echo '"' >> /home/${User}/.jupyter/jupyter_notebook_config.py
RUN echo -n 'c.NotebookApp.notebook_dir = "' >> /home/${User}/.jupyter/jupyter_notebook_config.py
RUN echo -n ${JUPYTER_WORK_DIR} >> /home/${User}/.jupyter/jupyter_notebook_config.py
RUN echo '"' >> /home/${User}/.jupyter/jupyter_notebook_config.py

# Kaggle API setting --->
# USER root
# RUN pip install kaggle
# USER ${User}
# RUN mkdir /home/${User}/.kaggle
# COPY sandbox/kaggle.json /home/${User}/.kaggle/kaggle.json
# RUN chmod 600 /home/${User}/.kaggle/kaggle.json
# RUN kaggle config set -n proxy -v http://proxy.uec.ac.jp:8080/
# ---> to this point

RUN echo '%wheel    ALL=(ALL)   NOPASSWD:ALL' >> /etc/sudoers
RUN echo 'Defaults timestamp_timeout = 0' >> /etc/sudoers


# If you do not need PASSWORD, please comment out below lines ---->
RUN echo -n 'export LINE=`sudo cat /etc/shadow | grep ' >> /home/${User}/.bashrc
RUN echo -n "${User}" >> /home/${User}/.bashrc
RUN echo '`' >> /home/${User}/.bashrc
RUN echo 'if [ ` echo \$LINE  | grep "!" ` ]; then' >> /home/${User}/.bashrc
RUN echo 'echo "register password..."' >>/home/${User}/.bashrc
RUN echo 'while :; do' >> /home/${User}/.bashrc
RUN echo "sudo passwd ${User}" >> /home/${User}/.bashrc
RUN echo 'if [ $? -eq 0 ];then' >> /home/${User}/.bashrc
RUN echo '  sudo sed -i -e "s/%wheel    ALL=(ALL)   NOPASSWD:ALL/#%wheel    ALL=(ALL)   NOPASSWD:ALL/" /etc/sudoers' >> /home/${User}/.bashrc
RUN echo '  break' >> /home/${User}/.bashrc
RUN echo 'echo "Retry... "' >> /home/${User}/.bashrc
RUN echo 'fi' >> /home/${User}/.bashrc
RUN echo 'done' >> /home/${User}/.bashrc
RUN echo 'fi' >> /home/${User}/.bashrc
# --------->   to this point