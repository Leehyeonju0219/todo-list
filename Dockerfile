# 기본 이미지 선택
FROM python:3.11-slim
# 작업 디렉토리 설정
WORKDIR /app
# 의존성 파일 복사 및 설치
COPY requirements.txt /app/
RUN pip install -r requirements.txt
# 프로젝트 파일 복사
COPY . /app/
# 포트 설정
EXPOSE 8000
# 컨테이너 시작 시 실행할 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]