FROM python:3.9-slim-buster
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN apt-get -y update && apt-get install -y --fix-missing sudo

RUN apt-get install -y --fix-missing \ 
    libsm6 \ 
    libxext6 \
    libxrender-dev \
    libgtk2.0-dev \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev

RUN apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN pip install -r requirements.txt
RUN pip3 install torch==1.7.1+cpu torchvision==0.8.2+cpu -f https://download.pytorch.org/whl/torch_stable.html


RUN mkdir -p /root/.streamlit
USER root
RUN /bin/bash -c 'echo -e "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > /root/.streamlit/credentials.toml'

EXPOSE 8501
SHELL ["/bin/bash", "-c"]
CMD streamlit run app.py
# CMD streamlit run --server.port $PORT app.py
