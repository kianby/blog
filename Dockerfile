FROM nginx:1.27.3-alpine

RUN apk update 
RUN apk add --no-cache build-base bash git python3 make tzdata curl py3-pip libressl-dev musl-dev libffi-dev python3-dev cargo

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN mv /root/.local/bin/uv /usr/local/bin
RUN mv /root/.local/bin/uvx /usr/local/bin

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