FROM nvcr.io/nvidia/tensorflow:21.03-tf1-py3

ENV HTTP_PROXY=http://proxy.uec.ac.jp:8080/
ENV HTTPS_PROXY=http://proxy.uec.ac.jp:8080/ 

ARG User

# set Passwd if you need
ENV JUPYTER_PASSWD=
# change Port if you want to change
ENV JUPYTER_PORT=8888

EXPOSE ${JUPYTER_PORT}


USER root
RUN echo ${User}
RUN cat /etc/lsb-release
RUN echo 'Acquire::http::Proxy "http://proxy.uec.ac.jp:8080";' >> /etc/apt/apt.conf\
    && echo 'Acquire::https::Proxy "http://proxy.uec.ac.jp:8080";' >> /etc/apt/apt.conf
RUN echo 'export JUPYTER_PORT=${JUPYTER_PORT}' >> /root/.bashrc
RUN echo 'export JUPYTER_PASSWD=${JUPYTER_PASSWD}' >> /root/.bashrc

RUN apt-get update && apt-get install -y && apt-get upgrade -y
RUN useradd -m ${User}
RUN apt-get install -y apt-utils build-essential git bash-completion gnupg2 curl apt-transport-https nano tree bzip2-doc libncurses-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev zlib1g-dev wget llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev sudo 
RUN gpasswd -a ${User} sudo
RUN groupadd wheel
RUN gpasswd -a ${User} wheel
RUN gpasswd -a root wheel

USER ${User}
RUN pip install jupyter
RUN jupyter notebook --generate-config
USER root
COPY sandbox/jupyter_notebook_config.py /home/${User}/.jupyter/jupyter_notebook_config.py
COPY sandbox/start_jupyter.sh /home/${User}
RUN chmod +x /home/${User}/start_jupyter.sh 

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