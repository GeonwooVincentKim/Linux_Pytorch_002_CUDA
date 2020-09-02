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