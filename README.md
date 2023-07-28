# AICI👨‍🔧

## 베포주소
>**http://52.78.234.62/**   

## 0. 사용 버전   
- python==3.10.11
- Django==4.2.2
- gunicorn==20.1.0
 
## 1. 설치 파일
### KT genie memo
```
$ pip install -c conda-forge portaudio python=3 pyaudio grpcio grpcio-tools
$ python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ktai.proto
```
```
$ pip install -r requirements.txt
```
## 2. 실행 방법
```
$ code .
$ python mange.py runserver
```
