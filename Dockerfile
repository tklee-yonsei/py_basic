# 베이스 이미지로 Ubuntu 22.04 사용
FROM ubuntu:22.04

# 기본 패키지 업데이트 및 Python 3.10 설치
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-venv python3.10-dev python3-pip && \
    apt-get clean

# 심볼릭 링크를 설정하여 python3 명령어가 Python 3.10을 가리키도록 설정
RUN ln -sf /usr/bin/python3.10 /usr/bin/python3 && \
    ln -sf /usr/bin/python3.10 /usr/bin/python

# 작업 디렉토리 설정
WORKDIR /app

# 필요하다면 패키지 설치 (예: requirements.txt가 있다면)
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# 컨테이너에서 사용할 포트 설정 (선택사항, 예: Flask 등을 사용할 경우)
# EXPOSE 5000

# Python 스크립트 실행 명령어 설정 (필요 시 주석 해제)
# CMD ["python", "my_main.py"]

# 기본 명령어 설정 (옵션, 필요 시 주석 해제)
# CMD ["tail", "-f", "/dev/null"]
