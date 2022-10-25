FROM quay.io/centos/centos:stream8

RUN dnf -y module install python39 && dnf --setopt=tsflags=nodocs -y install python39 python39-pip && dnf clean all
RUN mkdir /app
ADD https://raw.githubusercontent.com/arcalot/arcaflow-plugins/main/LICENSE /app/
ADD utilities_plugin.py /app/
ADD test_utilities_plugin.py /app/
ADD poetry.lock pyproject.toml /app/
WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --without dev

RUN mkdir /htmlcov
RUN pip3 install coverage
RUN python3 -m coverage run test_utilities_plugin.py
RUN python3 -m coverage html -d /htmlcov --omit=/usr/local/*

VOLUME /config

ENTRYPOINT ["python3", "/app/utilities_plugin.py"]
CMD []

LABEL org.opencontainers.image.source="https://github.com/arcalot/arcaflow-plugin-utilities"
LABEL org.opencontainers.image.licenses="Apache-2.0+GPL-2.0-only"
LABEL org.opencontainers.image.vendor="Arcalot project"
LABEL org.opencontainers.image.authors="Arcalot contributors"
LABEL org.opencontainers.image.title="Python Plugin For Utility Functions"
LABEL io.github.arcalot.arcaflow.plugin.version="1"
