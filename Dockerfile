# Base Image, Python Interpreter
FROM python:3.8-buster AS uk-improv-guide-python-base0
RUN apt-get update
RUN mkdir /tmp/install
COPY /src/requirements_dev.txt /tmp/install/requirements_dev.txt
RUN python -m pip install -r /tmp/install/requirements_dev.txt
RUN apt-get install git
RUN rm -rf /tmp/install

FROM uk-improv-guide-python-base0 AS uk-improv-guide-python-base1
RUN apt-get update && apt-get install -y postgresql-client bash \
    && rm -rf /var/lib/apt/lists/*
COPY /src/requirements.txt /src/
RUN python -m pip install -r /src/requirements.txt
RUN useradd python


FROM uk-improv-guide-python-base1 AS uk-improv-guide
COPY /src /src

ARG IMPROV_GUIDE_VERSION
ARG FOO
ARG DEBUG=True
ENV POSTGRES_PASSWORD=changeme
ENV POSTGRES_USER=improv
ENV POSTGRES_DB=improv
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV SLACK_WEB_HOOK=http://www.example.com

RUN printenv | sort

WORKDIR /src/
RUN python setup.py develop

RUN manage compilescss
RUN manage collectstatic
HEALTHCHECK --interval=30s --timeout=10s CMD curl --fail http://localhost || exit 1
ENTRYPOINT ["./start_prod.sh"]

FROM nginx:latest AS uk-improv-guide-nginx
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get install certbot python-certbot-nginx -y
COPY nginx/config/no_ssl.conf /etc/nginx/no_ssl.conf
COPY nginx/config/ssl.conf /etc/nginx/ssl.conf
#RUN nginx -t -c /etc/nginx/no_ssl.conf
#RUN nginx -t -c /etc/nginx/ssl.conf
COPY --from=uk-improv-guide ./static /usr/share/nginx/html/static/
COPY ./nginx/start.sh /bin/
ENTRYPOINT ["/bin/start.sh"]
WORKDIR /src/uk_improv_guide
HEALTHCHECK --interval=30s --timeout=10s CMD curl --fail http://localhost || exit 1

