# [데이터 시각화]
## 3번째 일시 >> [2]
## 4번째 평균기온 >> [3]
## import는 상단배치
import csv
import matplotlib.pyplot as plt
# cmd 설치 >> pip install matplotlib


# 파일을 어디서 읽어올지 경로를 저장시킨다
# java식 filePath = "test.csv" 카멜이 더 보편적
# 파이썬에선 언더바 많이 사용
# 파일 절대경로로 불러도 되지만, 상대경로로 부른
file_path = "test.csv"

# x축, y축에 넣기 위한 데이터를 list로 만들어준다.
dates = []
temps = []


# with open(파일명,mode='어떤 모드로 읽을지', encoding="인코딩") as 객체명 :
# mode는 읽어올 땐 read, 쓸 땐 writer
# 아래 코드는 파이썬 내로 로드한 것임!
with open(file_path,mode='r') as file :
    # 가지고 왔으면 읽어야 함
    # reader는 open()이나, print(), input() 함수 처럼 보라색이 아님
    # >> 내장함수 (기본 함수가 아니다) : csv라는 패키지의 것임 (import 필요)
    # 자바에서는 패키지, 파이썬에서는 모듈이라고 
    reader = csv.reader(file)

    # 파일 내용 확인
    # for v in 집합명 (향상된 for문)
    # reader 안의 내용을 한 줄씩 불러줘~

    # 첫 줄을 읽어버리고
    header = next(reader) # 한 줄 읽기
    

    # 시작해~~~~
    # i = 0
    for row in reader :
        a = row[2] # 12월이 데이터만 출력하고 싶다~~~~
        b = row[-2] # 최저기

        # if a가 Dec로 시작하면 : 
        # 파이썬에서는 java와 다르게 문자열을 더해줄땐 +가 아닌 ,로 구분
        if a.startswith("Dec") : 
            print(a, b) ## row가 list 타입이라는 사실도 확인 가능!
            dates.append(a)
            # b가 str 타입이므로 형변환해준다.
            temps.append(float(b))
            """
            #데이터를 자르기 위해 데이터 추가될 때마다 1씩 +
            i += 1
            # 10개만 보기 위함
            if i == 10 :
                break
            """


# plt의 경우에도 내장 함수가 아님, 모듈이다! import 해야
# 그래프를 그리고
plt.plot(dates,temps,marker='o',color='r',linestyle=':',linewidth=10, markersize=5)
# 도표이기 때문에 뭘 표현했는지 달아줘야 함
plt.title("Temperature in December", fontsize=15)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Temperature", fontsize=10)
# 그린 그래프를 화면에 출력해줘()
plt.show()
























