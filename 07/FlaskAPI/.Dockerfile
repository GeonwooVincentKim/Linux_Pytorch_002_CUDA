FROM nvidia/cuda:9.0-base

"""
    Upload codes that executes 'Linux' only.
"""
# Install Minimum-Package for installing Miniconda.
RUN set -ex \
    && deps='\
        bzip2 \
        ca-certificates \
        curl \
        libgomp1 \
        libgfortran3 \
    ' \
    && apt-get update \
    && apt-get install -y --no-install-recommends $deps \
    && rm -rm /var/lib/apt/lists/*

ENV PKG_URL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
ENV INSTALLER miniconda.sh
