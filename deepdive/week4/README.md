# 환경변수와 설정관리(Environment Variables & Configuration)

## 환경변수(Environment Variables)
- 운영체제라는 환경에 존재하는 변수, 파이썬 코드 바깥에서 프로그램을 읽어올 수 있는것
 <br> -> 프로그램 실행 전에 운영체제가 미리 알려주는 설정 메모
 <br> -> 프로그램이 매번 계산하거나 물어보지 않아도, 바로 꺼내쓰는 설정값
<br> Ex) PATH - 프로그램을 찾는 기본 경로

**환경변수를 코드 밖에 두는 이유**
- **보안 문제** -> 민감한 값은 코드가 아니라 서버(운영체제)쪽 설정에 둠
- **환경이 다르기 때문** -> 코드는 하나, 설정은 장소마다 다르게
- **유지보수/배포가 편해짐**

 **.env파일**
- 키(key)-값(value) 쌍으로 환경 변수를 정의 하는 간단한 택스트 파일
  <br> -> 응용프로그램에 삽입될 환경변수를 담아놓은 설정 파일 
- 이 파일을 사용하면 코드 내에 민감한 정보를 직접 작성 하지않고도 환경변수를 쉽게 관리할 수 있다
- **민감한 정보가 포함될 수 있으므로 .gitignore파일에 추가하는게 일반적**

**dotenv**
- 환경변수를 읽어와서 python프로젝트 내애서 사용할 수 있게 해주는 라이브러리
- 환경변수는 보통 운영체제에서 관리되지만, dotenv를 사용하면 .env파일에 환경 변수를 정의 하고 이를 코드에서 쉽게 불러올수있다.

**.env파일을 python-dotenv로 불러오는 방법**
- dotenv라이브러리설치 방법 `pip install python-dotenv`
- .env파일 만들기<br>
```
API_KEY=your_api_key-here
DATABASE_URL=your_database_url_here
```
- dotenv적용
```
from dotenv import load_dotenv
import os
 #.env 파일 로드
load_dotenv()

#환경 변수 읽기
api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')

print(f"API_KEY: {api_key}")
print(f"DATABASE_URL: {database_url}")
```

**배포환경**

개발환경(localhost) - Development
<br>배포환경(AWS, GCP 같은 클라우드 서버) - Production

이 두 환경의 설정을 다르게 가져가려면 어떻게 해야하는가?

개발환경-> 외부에 노출되지않아 상대적으로 관리가 쉬워 .env파일 안의 값을 따로 처리하지않고 주입시킴

배포환경 -> 보안에 신경을 써야하기에 AWS같은 배포환경에서 자체적으로 .env값을 다른 값으로 대체시켜서 주입함 


   

