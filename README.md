# OpenAPI-Test
강의 후 실습 및 테스틀 위해서 작성되었습니다.

OAuth 2.0 테스트 시 플라스크 실행 코드
~~~python
flask --debug --app oauth run --port 5003
~~~

webhook 테스트 시 플라스크 실행 코드
~~~python
flask --debug --app webhook run --port 5003
~~~

이 후 ngrok 으로 외부 접속 준비
(mac 환경에서 5000 포트가 안되는 경우가 있어서 5003 으로 변경)