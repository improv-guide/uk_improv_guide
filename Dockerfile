FROM salimfadhley/testpython as python
RUN apt-get update && apt-get install mysql-client -y
COPY ./src /src
RUN python -m pip install -r /src/requirements_dev.txt
RUN python -m pip install -e /src
WORKDIR /src/uk_improv_guide
RUN useradd python
