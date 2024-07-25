# django_todo
 
장고를 이용한 할일 관리 애플리케이션

## 다운로드

```bash
git clone https://github.com/jonghyun-lee/django_todo
```

## 파이썬 가상 환경 만들기

[작업 폴더에 파이썬 가상 환경 만들기](https://note.ibetter.kr/%EC%A7%80%EC%8B%9D%EB%85%B8%ED%8A%B8/%EA%B0%9C%EB%B0%9C+%ED%99%98%EA%B2%BD/%EC%9E%91%EC%97%85+%ED%8F%B4%EB%8D%94%EC%97%90+%ED%8C%8C%EC%9D%B4%EC%8D%AC+%EA%B0%80%EC%83%81+%ED%99%98%EA%B2%BD+%EB%A7%8C%EB%93%A4%EA%B8%B0)를 참고해서 가상 환경 만들기

## 장고 설치

```bash
$ django_todo> pip install django
```

## 데이터베이스 마이그레이션

### makemigrations

```bash
$ django_todo> cd mysite
$ django_todo/mysite> python manage.py makemigrations
```

### migrate

```bash
$ django_todo/mysite> python manage.py migrate
```

## 서버 실행

```bash
$ django_todo/mysite> python manage.py runserver
```