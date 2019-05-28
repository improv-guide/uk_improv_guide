FROM salimfadhley/testpython as python
COPY . /project
RUN python -m pip install -r /project/src/requirements_dev.txt
RUN python -m pip install -e /project/src
RUN useradd python
