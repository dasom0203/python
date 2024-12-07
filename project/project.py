import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# 첫 번째 CSV 파일 경로 (출산율)
birth_file_path = "BirthAndMarriage.csv"
# 두 번째 CSV 파일 경로 (유소년 인구 수, 노령화 지수)
old_file_path = "agingIndex.csv"
# 한국어 사용을 위한 폰트 적용
plt.rcParams['font.family'] ='Malgun Gothic'

# 데이터 배열 초기화
years = []    # 연도
births = []   # 출생 수
olders = []   # 노령화 지수
yangs = [] # 유소년 인구


# 출산율 데이터 읽기
with open(birth_file_path, mode='r') as file:
    reader = csv.reader(file)  # CSV 파일을 읽기 위한 객체 생성
    header = next(reader)      # 첫 번째 줄은 헤더이므로 건너뜀

    for row in reader:
        a = row[0]  # 첫 번째 값(연도)
        b = row[1]  # 두 번째 값(출생 수)

        years.append(int(a))
        births.append(int(b)/1000) # 단위 조정 (천)  

# 노령화 지수, 유소년 인구 데이터 읽기
with open(old_file_path, mode='r') as file:
    reader = csv.reader(file)  # CSV 파일을 읽기 위한 객체 생성
    header = next(reader)      # 첫 번째 줄은 헤더이므로 건너뜀

    for row in reader:
        a = row[0]  # 첫 번째 값(연도)
        b = row[-4]  # 두 번째 값(노령화 지수), 노령화지수=고령인구/유소년인구 * 100
        c = int(row[4]) / int(row[1]) *100  # 유소년 비율 (유소년 수/전체인구*100)

        # 이미 존재하는 연도에 대해서만 추가
        if int(a) in years:
            olders.append(float(b)) # 노령화 지수
            yangs.append(c) # 유소년 인구 비율

# 시각화를 위한 그래프 설정
fig, ax1 = plt.subplots()  # 하나의 그래프를 그리기 위한 subplot 생성

# 첫 번째 y축을 기준으로 출생 수를 막대그래프(bar chart)로 표시
ax1.bar(years, births, color='tan', width=0.5, label='출생 수', alpha=0.6)

# 두 번째 y축을 설정 (출생 수와 유소년 비율, 노령화 지수가 다른 범위의 값을 가지므로)
ax2 = ax1.twinx()
# 두 번째 y축을 기준으로 유소년 비율을 선 그래프(line plot)로 표시
ax2.plot(years, yangs, color='r', marker='o', label='유소년 인구 비율', linewidth=2)
# y축을 백분율로 표시
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))


# 세 번째 y축을 기준으로 노령화 지수를 선 그래프(line plot)로 표시
ax3 = ax1.twinx()  # 세 번째 y축 추가
ax3.spines['right'].set_position(('outward', 60))  # 세 번째 y축 위치를 오른쪽으로 이동
ax3.plot(years, olders, color='b', label='노령화 지수', linewidth=2)


# 축 레이블 설정
ax1.set_xlabel('연도')   # x축은 연도를 표시
ax1.set_ylabel('출생 수 (단위 : 천)')   # 첫 번째 y축은 출생 수
ax2.set_ylabel('유소년 인구 비율') # 두 번째 y축은 유소년 인구 비율
ax3.set_ylabel('노령화 지수')  # 세 번째 y축은 노령화 지수


# 통합된 범례 설정
fig.legend(loc='upper center',  bbox_to_anchor=(0.5, 0.87),ncol=3)


# 그래프 제목 설정
plt.title("출산율 및 유소년 비율의 감소로 인한 노령화 지수 상승", fontsize=15)

# 그래프 출력
plt.show()


