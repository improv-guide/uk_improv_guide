FROM salimfadhley/testpython AS uk_improv_guide_python_base
RUN apt-get update && apt-get install mysql-client bash -y
COPY /src/requirements_dev.txt /src/
RUN python -m pip install -r /src/requirements_dev.txt
COPY /src/requirements.txt /src/
RUN python -m pip install -r /src/requirements.txt

FROM uk_improv_guide_python_base AS uk_improv_guide
COPY /src /src
RUN python -m pip install -e /src
WORKDIR /src/uk_improv_guide
RUN chmod +x *.sh
RUN chmod +x manage.py
RUN useradd python
