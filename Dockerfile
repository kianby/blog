FROM nginx:1.19.0-alpine

RUN apk update 
RUN apk add --no-cache bash git python3 make tzdata curl py3-pip libressl-dev musl-dev libffi-dev

# install poetry
ENV POETRY_HOME=/opt/poetry
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install --upgrade pip
RUN $POETRY_HOME/bin/pip install setuptools_rust poetry==1.2.0
RUN $POETRY_HOME/bin/poetry --version

COPY docker/nginx.conf /etc/nginx/nginx.conf

# install locales
ENV MUSL_LOCALE_DEPS cmake make musl-dev gcc gettext-dev libintl 
ENV MUSL_LOCPATH /usr/share/i18n/locales/musl

RUN apk add --no-cache \
    $MUSL_LOCALE_DEPS \
    && wget https://gitlab.com/rilian-la-te/musl-locales/-/archive/master/musl-locales-master.zip \
    && unzip musl-locales-master.zip \
      && cd musl-locales-master \
      && cmake -DLOCALE_PROFILE=OFF -D CMAKE_INSTALL_PREFIX:PATH=/usr . && make && make install \
      && cd .. && rm -r musl-locales-master

# set timezone and locale
RUN cp /usr/share/zoneinfo/Europe/Paris /etc/localtime
RUN echo "Europe/Paris" >  /etc/timezone
ENV TZ Europe/Paris
ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR.UTF-8
ENV LC_ALL fr_FR.UTF-8

COPY docker/docker-init.sh /usr/local/bin/
RUN chmod +x usr/local/bin/docker-init.sh

CMD ["docker-init.sh"]