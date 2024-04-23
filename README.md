# Todo 애플리케이션

Django 프레임워크를 사용하여 간단한 Todo 애플리케이션을 구현하였습니다. 이 애플리케이션을 사용하여 할 일 목록을 만들고 관리할 수 있습니다.

## 기능

- 할 일 목록 보기: 모든 할 일을 목록으로 볼 수 있습니다.
- 할 일 추가: 새로운 할 일을 추가할 수 있습니다.
- 할 일 수정: 기존의 할 일을 수정할 수 있습니다.
- 할 일 삭제: 할 일을 삭제할 수 있습니다.

## 설치 및 실행 방법

1. 이 Repository를 클론합니다.
2. 가상환경을 설정하고 필요한 패키지를 설치합니다.

    ```
    pip install -r requirements.txt
    ```

3. 데이터베이스 마이그레이션을 수행합니다.

    ```
    python manage.py migrate
    ```

4. 개발 서버를 실행합니다.

    ```
    python manage.py runserver
    ```

5. 브라우저에서 http://127.0.0.1:8000/ 에 접속하여 애플리케이션을 확인합니다.

## 개발 환경

- Python 3.x
- Django 3.x

## 기여 방법

이 프로젝트에 기여하고 싶다면, 이슈를 제출하거나 Fork 후 코드를 수정하여 Pull Request를 보내주세요!

## 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다.