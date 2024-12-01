import csv
import matplotlib.pyplot as plt

# 첫 번째 CSV 파일 경로 (출산율, 혼인율)
birth_file_path = "project.csv"
# 두 번째 CSV 파일 경로 (고령화)
old_file_path = "old.csv"

# 데이터 배열 초기화
years = []    # 연도
births = []   # 출생 수
merries = []  # 혼인율
olders = []   # 고령화 비율

# 출산율, 혼인율 데이터 읽기
with open(birth_file_path, mode='r') as file:
    reader = csv.reader(file)  # CSV 파일을 읽기 위한 객체 생성
    header = next(reader)      # 첫 번째 줄은 헤더이므로 건너뜀

    for row in reader:
        a = row[0]  # 첫 번째 값(연도)
        b = row[1]  # 두 번째 값(출생 수)
        c = row[-1]  # 세 번째 값(혼인율)

        years.append(int(a))
        births.append(int(b))     
        merries.append(int(c)) 

# 고령화 비율 데이터 읽기
with open(old_file_path, mode='r') as file:
    reader = csv.reader(file)  # CSV 파일을 읽기 위한 객체 생성
    header = next(reader)      # 첫 번째 줄은 헤더이므로 건너뜀
    header = next(reader)      # 두 번째 줄도 건너뜀 (필요한 데이터 행으로 시작)

    for row in reader:
        a = row[0]  # 첫 번째 값(연도)
        b = row[1]  # 두 번째 값(고령화 비율)

        # 이미 존재하는 연도에 대해서만 추가
        if int(a) in years:
            olders.append(int(b))    # 고령화 비율은 정수로 변환하여 추가

# 시각화를 위한 그래프 설정
fig, ax1 = plt.subplots()  # 하나의 그래프를 그리기 위한 subplot 생성

# 첫 번째 y축을 기준으로 출생 수를 막대그래프(bar chart)로 표시
ax1.bar(years, births, color='tan', width=0.5, label='Births', alpha=0.6)

# 두 번째 y축을 설정 (출생 수와 혼인율, 고령화가 다른 범위의 값을 가지므로)
ax2 = ax1.twinx()

# 두 번째 y축을 기준으로 혼인율을 선 그래프(line plot)로 표시
ax2.plot(years, merries, color='r', marker='o', label='Merries', linewidth=2)

# 세 번째 y축을 기준으로 고령화 비율을 선 그래프(line plot)로 표시
ax3 = ax1.twinx()  # 세 번째 y축 추가
ax3.spines['right'].set_position(('outward', 60))  # 세 번째 y축 위치를 오른쪽으로 이동
ax3.plot(years, olders, color='b', label='Older Population', linewidth=2)

# 첫 번째 y축 레이블 설정
ax1.set_xlabel('Years')   # x축은 연도를 표시
ax1.set_ylabel('Births')   # 첫 번째 y축은 출생 수
ax2.set_ylabel('Merries') # 두 번째 y축은 혼인율
ax3.set_ylabel('Older Population')  # 세 번째 y축은 고령화 비율

# 범례 설정
ax1.legend(loc='upper left')  # 첫 번째 그래프에 대한 범례 위치
ax2.legend(loc='upper right') # 두 번째 그래프에 대한 범례 위치
ax3.legend(loc='lower right') # 세 번째 그래프에 대한 범례 위치

# 그래프 제목 설정
plt.title("Birth Rate, Marriage Rate, and Older Population Over the Years", fontsize=15)

# 그래프 출력
plt.show()
