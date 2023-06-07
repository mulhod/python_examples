FROM docker.io/library/amazonlinux:latest

RUN set -x \
    && yum install -y wget zip nano less git \
    && wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-$(uname -p).sh" -O miniconda.sh \
    && bash miniconda.sh -b -p miniconda \
    && rm -f miniconda.sh
