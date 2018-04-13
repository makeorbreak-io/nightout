FROM fedora:27

RUN mkdir /opt/nightout
RUN mkdir /opt/configs

WORKDIR /opt/nightout

RUN dnf install -y \
        gcc \
        git \
        nginx \
        python3 \
        python3-devel \
        python3-pip \
        python3-setuptools \
        python3-mysql \
        supervisor

# setup all the configfiles
COPY configs/supervisord.conf /etc/supervisord.conf

RUN mkdir /etc/nginx/sites-enabled
RUN rm /etc/nginx/nginx.conf
RUN ln -s /opt/configs/nginx/nginx.conf /etc/nginx/
RUN ln -s /opt/configs/nginx/phastload.conf /etc/nginx/sites-enabled/

COPY requirements.txt /opt/nightout/
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN ./manage.py collectstatic -y

COPY ./configs /opt/configs/

EXPOSE 80
EXPOSE 443
CMD ["supervisord", "-n"]
