# Todo 애플리케이션

Django 프레임워크를 사용하여 간단한 Todo 애플리케이션을 구현하였습니다. 이 애플리케이션을 사용하여 할 일 목록을 만들고 관리할 수 있습니다.

## 주요 기능

- **할 일 목록 보기**: 모든 할 일을 목록 형태로 볼 수 있습니다.
- **할 일 추가**: 새로운 할 일을 추가할 수 있습니다.
- **할 일 수정**: 기존의 할 일을 수정할 수 있습니다.
- **할 일 삭제**: 할 일을 삭제할 수 있습니다.

## 설치 및 실행 방법

### Docker를 사용한 설치 및 실행

1. 이 Repository를 클론합니다.
   ```bash
   git clone [your-repository-url]
   cd [repository-name]
2. Docker 이미지를 빌드하고 컨테이너를 실행합니다.
   ```bash
   docker-compose up --build
3. 브라우저에서 `http://localhost:8000/`로 접속하여 애플리케이션을 사용합니다.

### 전통적인 방법으로 설치 및 실행

1. 이 Repository를 클론합니다.
   ```bash
   git clone https://github.com/Leehyeonju0219/todo-list.git
   cd todo-list
2. 가상환경을 설정하고 필요한 패키지를 설치합니다.
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS and Linux
   pip install -r requirements.txt
3. 데이터베이스 마이그레이션을 수행합니다.
   ```bash
   python manage.py migrate
4. 개발 서버를 실행합니다.
   ```bash
   python manage.py runserver
5. 브라우저에서 `http://127.0.0.1:8000/`로 접속하여 애플리케이션을 확인합니다.

## 개발 환경

- **언어**: Python 3.9 이상
- **프레임워크**: Django 3.2 이상
- **컨테이너**: Docker

## 기여 방법

이 프로젝트에 기여하고 싶다면, 이슈를 제출하거나 Fork 후 코드를 수정하여 Pull Request를 보내주세요!

## 라이센스

이 프로젝트는 MIT 라이센스에 따라 사용이 허가되어 있습니다. 라이센스 전문은 프로젝트 내 LICENSE 파일에서 확인할 수 있습니다.
