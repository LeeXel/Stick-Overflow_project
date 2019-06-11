# Stick-Overflow
capstone design project

This page is about online Data Analysis System.

- - -

### Database

##### 설명

회원가입, 로그인 이후 정보 관리
사용자의 업로드한 데이터 관리
분석 후 데이터 관리

### Table

#### USER
- USER_ID : 사용자 아이디
- PASSWORD : 사용자 패스워드
- USER_NM : 사용자 이름
- EMAIL : 사용자 이메일
- DEPARTMENT : 학과(사용자가 아직 회사가 아니라 학교에서 쓴다는 가정하에 학과라는 명칭을 사용합니다)
- INPUT_ID : 입력자의 ID
- INPUT_IP : 입력자의 IP
- INPUT_DATE : 입력일시
- UPDATE_ID : 수정자의 ID
- UPDATE_IP : 수정자의 IP
- UPDATE_DATE : 수정일시

#### FILE
- USER_ID : 사용자 아이디
- FILE_NO : 파일의 시퀸스 넘버
- FILE_NM : 파일의 이름
- FILE_PATH : 파일의 경로
- FILE_DESC : 파일에 대한 정보

#### RESULT
- USER_ID : 사용자 아이디
- FILE_NO : 파일의 시퀸스 넘버
- RESULT_NO : 결과 파일의 시퀸스 넘버
- ANALY_CD : 분석 코드(상관분석, 평균)
- SAVE_CD : 저장을 파일로 만들건지 DB로 만들어 저장할건지 판단하는 코드
---
DB로 저장 할 경우
- RESULT : 분석한 결과 파일
---
파일로 저장 할 경우
- FILE_NM : 분석한 결과 파일 이름
- FILE_PATH : 분석한 결과 파일 경로
- FILE_DESC : 분석한 결과 파일 설명

이의 있을시 수정요청 
