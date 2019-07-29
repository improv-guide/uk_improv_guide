FROM nginx:latest AS uk-improv-guide-nginx
COPY ./nginx/config/default.conf /etc/nginx/conf.d/default.conf


FROM salimfadhley/testpython AS uk-improv-guide-python-base
RUN apt-get update && apt-get install mysql-client bash -y \
    && rm -rf /var/lib/apt/lists/*
COPY /src/requirements_dev.txt /src/
RUN python -m pip install -r /src/requirements_dev.txt
COPY /src/requirements.txt /src/
RUN python -m pip install -r /src/requirements.txt
RUN useradd python


FROM uk-improv-guide-python-base AS uk-improv-guide
COPY /src /src
COPY /static /src/uk-improv-guide/static
WORKDIR /src/uk_improv_guide
RUN chmod +x *.sh
RUN chmod +x manage.py
RUN python -m pip install -e /src
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:80", "uk_improv_guide.wsgi"]

