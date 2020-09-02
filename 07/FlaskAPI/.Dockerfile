FROM nvidia/cuda:9.0-base

# Install Minimum-Package for installing Miniconda.
RUN set -ex \
    && deps='\
        bzip2 \
        ca-certificates \
        curl \
        libgomp1 \
        libgfortran3 \
    ' \