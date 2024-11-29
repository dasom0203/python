# csv 파일
# : old.csv(고령화 수) - 고령인구(천명)
# : tp.csv (출산율, 혼인율) - 출생아 수(명), 혼인건수(건)

import csv
import matplotlib.pyplot as plt
# 한국어 사용을 위한 폰트 적용
plt.rcParams['font.family'] ='Malgun Gothic'
# 부호 깨짐 방지
plt.rcParams['axes.unicode_minus'] =False

# 파일 경로 저장
aging_file_path="old.csv" # 고령화 인원 수 파일
marriage_birth_file_path="tp.csv" # 출산, 혼인 수 파일 


# 데이터를 담기 위한 배열 선
aging_years = [] # 고령화 인원 연도
aging_rates = [] # 고령화 인원 수
marriage_years = [] # 출생/혼인 연도
marriage_rates = [] # 혼인 수
birth_rates = [] # 출생아 수


# 고령인구 수 데이터 읽기
with open(aging_file_path,mode='r') as aging_file :
    # csv 파일 읽어오기
    reader = csv.reader(aging_file)

    # 파일 내용 확인
    # 첫 줄은 제목이므로, 먼저 한 줄을 읽는다
    header = next(reader)

    # 반복문!
    for row in reader :
        year = row[0] # 연도
        aging_rate = row[1].replace(',', '')  # 고령화 인원 수

                
        print(type(year))

        # 데이터 추가
        aging_years.append(year) # 연도 저장
        aging_rates.append(int(aging_rate)/10) # 고령화 인원 수 
        
        # 2023년까지 데이터 자르기
        if row[0] == '2023' :
            break

        

# 결혼율과 출산율 데이터 읽기
with open(marriage_birth_file_path,mode='r') as marriage_birth_file :
    # csv 파일 읽어오기
    reader = csv.reader(marriage_birth_file)
    
    # 파일 내용 확인
    # 첫 줄은 제목이므로, 먼저 한 줄을 읽는다
    header = next(reader)
    
    # 반복문!
    for row in reader :
        ## print(row)
        year = row[0] # 연도
        marriage_rate = row[-1] # 혼인 건수(천)
        birth_rate = row[1] # 출산 건수(천)

        # 데이터 저장
        marriage_years.append(year) # 연도
        marriage_rates.append(float(marriage_rate)/1000) # 혼인 건수
        birth_rates.append(float(birth_rate)/1000) # 출생 건



# 데이터 병합 (연도별)
year = sorted(set(marriage_years) & set(aging_years))
print('year타입', type(year))
# year의 각 값을 정수형으로 변환
year_int = [int(y) for y in year]
print('year_int타입', type(year_int[0]),year_int[-1])

# 각 데이터에 대해 그래프 그리기
width = 0.25  # 막대의 폭
##x = range(len(year[-1]))  # 연도별 위치

# x축 데이터(연도)를 특정 간격으로 나오도록
##x = [year[i] for i in range(0, len(year), 2)]
##print(x)

# 각 데이터 선 그래프 추가
plt.plot(year, marriage_rates, label='결혼율', linestyle='-', marker='o', color='lightcoral')
plt.plot(year, birth_rates, label='출산율', linestyle='-', marker='o', color='lightgreen')
plt.plot(year, aging_rates, label='고령화율', linestyle='-',marker='o', color='cornflowerblue')


# plt.xticks(range(0,len(year),5))
plt.title('혼인,출산,고령화 인원에 따른 변화 그래프')  # 그래프 제목

# 2년 단위로 x축에 표시할 연도 설정
##print('year[0] :'+year_int[0]+'타입 : ',type(year_int[0]))
##print('year[0] :'+year_int[-1])
##plt.xticks(range(0, year_int[-1]+1, 2))  # 2년 간격으로 표시
print(type(year_int[0]),type(year_int[1]),year_int[1]+1)
plt.xlabel('연도')  # x축 레이블
plt.ylabel('값')  # y축 레이블

# 범례 표시
plt.legend()

# x축(연도) 범위 설정 (5년 단위)
##plt.xlim(0, 5)

# 그린 그래프를 화면에 출력
plt.show()

