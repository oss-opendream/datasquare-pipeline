# 베이스 이미지로 python 3.11.9 사용
FROM python:3.11.9

# 환경 변수 설정
ENV DEBIAN_FRONTEND=noninteractive

# 필수 패키지 설치
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    curl \
    git \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    ca-certificates \
    expect 


# Git 리포지토리 클론s
WORKDIR /root
RUN git clone https://github.com/oss-opendream/datasquare.git
WORKDIR /root/datasquare
RUN git fetch && git checkout dev

# poetry 다운
SHELL ["/bin/bash", "-c"]
RUN curl -sSL https://install.python-poetry.org | python3 - 
RUN echo PATH="/root/.local/bin:$PATH" >> ~/.bashrc
RUN /root/.local/share/pypoetry/venv/bin/poetry install && \
    python3 ./app/utils/key_scribe.py "$@"

# 폴더 생성 및 권한 부여
RUN mkdir -p /data/fastapi_log && \
    chmod 777 -R /data