FROM salimfadhley/testpython AS uk-improv-guide-python-base
RUN apt-get update && apt-get install -y postgresql-client bash \
    && rm -rf /var/lib/apt/lists/*
COPY /src/requirements_dev.txt /src/
RUN python -m pip install -r /src/requirements_dev.txt
COPY /src/requirements.txt /src/
RUN python -m pip install -r /src/requirements.txt
RUN useradd python


FROM uk-improv-guide-python-base AS uk-improv-guide
COPY /src /src
WORKDIR /src/uk_improv_guide
RUN chmod +x *.sh
RUN chmod +x manage.py
RUN python -m pip install -e /src
ENV POSTGRES_PASSWORD=changeme
ENV POSTGRES_USER=improv
ENV POSTGRES_DB=improv
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV SLACK_WEB_HOOK=http://www.example.com
RUN manage compilescss
RUN manage collectstatic
HEALTHCHECK --interval=1m --timeout=10s CMD curl --fail http://localhost || exit 1
ENTRYPOINT ["./start_prod.sh"]

FROM nginx:latest AS uk-improv-guide-nginx
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*
COPY ./nginx/config/default.conf /etc/nginx/conf.d/default.conf
COPY --from=uk-improv-guide ./static /usr/share/nginx/html/static/
COPY ./nginx/start.sh /bin/
ENTRYPOINT ["/bin/start.sh"]
HEALTHCHECK --interval=1m --timeout=10s CMD curl --fail http://localhost || exit 1

