# quick_flask

# 빠른 Flask개발을 위한 모듈

- 가볍고 빠른 flask 개발을 위한 기본적인 모듈

- 간단한 핑테스트 기능(GET, POST)
	+ GET으로 기본 통신 확인
	+ POST로 json값을 제대로 통신하는지 확인
	+ render_template으로 화면이 나오는지 확인
```
GET -x http://localhost:8080/quick_flask/ping_front
```
- 같은 direcotry에 method별 다른 기능
	+ GET인 경우에는 바로 사용자 화면을 보여주고
	+ POST인 경우 회원가입 화면기능
```
GET -x http://localhost:8080/quick_flask/render_page
```

# 기타

- Modeling정보
	+ 빠른 데이터베이스를 위해 HashModel을 사용하였음
	+ 클로저, nonlocal을 이용하여 함수 생성 가능

- Control정보
	+ 유저 이름을 받으면 값이 제대로 됬는지 검증하기
	+ 유저  HashDB에 삽입하고 상태값 반환 

- View정보
	+ 

```
# GET 핑통신확인
GET -x /quick_flask/ping

# POST 핑통신 확인
POST -x /quick_flask/ping-json

# GET으로 프런트페이지 확인
GET -x /quick_flask/ping_front

# HTTP메서드에 따라 다른 결과 반환
# GET인 경우 A/B테스트 페이지 POST인 경우 회원가입
GET,POST -x /quick_flask/render_page
```

# 추가로 다뤄야 할 사항들

- 404에러 핸들러 페이지 관리하기