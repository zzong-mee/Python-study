import requests

# 001
# from asyncio.windows_events import NULL
# from distutils.log import warn
# from hashlib import new


# print("Hello world")

# 002
# print("""Mary's cosmetics""")

# 003
# print("""신씨가 소리질렀다. "도둑이야".""")

# 004
# print("C:\Windows")

# 005
#~~~

# 006
#오늘은 일요일

# 007
# print("naver", "kakao", "sk", "samsung", sep=";")

# 008
# print("naver", "kakao", "sk", "samsung", sep="/")

# 009
#~~~

# 010
# print(5/3)

# 011
# 삼성전자 = 50000
# 총_평가금액 = 삼성전자 * 10
# print(총_평가금액)

# 012
# 시가총액 =  2980000000000
# 현재가 = 50000
# PER = 15.79

# 013
# s = "hello"
# t = "python"

# print(s + "!", t)

# 014
#8

# 015
# a = "132"
# print(type(a))

# 016
# num_str = "720"
# num_int = int(num_str)

# print(num_int + 1, type(num_int))

# 017
# num = 100
# result = str(num)
# print(result, type(result))

# 018
# data = "15.79"
# data = float(data)
# print(data, type(data))

# 019
# year = 2020
# year = int(year)
# print(year - 1)
# print(year - 2)
# print(year - 3)

# 020
# month_payment = 48584
# total_price = month_payment * 36
# print(total_price)

# 021
# latters = 'python'
# print(latters[0], latters[2])

# 022
# license_plate = "24가 2210"
# print(license_plate[4:])

# 023
# string = "홀짝홀짝홀짝"
# print(string[::2])

# 024
# string = "PYTHON"
# print(string[::-1])

# 025
# phone_number = "010-1111-2222"
# print(phone_number.replace("-", " "))

# 026
# phone_number = "010-1111-2222"
# print(phone_number.replace("-", ""))

# 027
# url = "http://sharebook.kr"
# print(url[-2:])

# 028
#~~~

# 029
# string = 'abcdfe2a354a32a'
# print(string.replace("a", "A"))

# 030
#~~~

# 031
#34

# 032
#HiHiHi

# 033
# print('-' * 80)

# 034
# t1 = "python"
# t2 = "java"

# t3 = t1 + " " + t2 + " "
# print(t3 * 4)

# 035
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))

# 036
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# 037
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 038
# 상장주식수 = "5,969,782,550"
# 상장주식수_컴마제거 = 상장주식수.replace(",", "")
# 상장주식수_컴마제거_정수 = int(상장주식수_컴마제거)

# print(상장주식수_컴마제거_정수, type(상장주식수_컴마제거_정수))

# 039
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# 040
# data = "   삼성전자    "
# data = data.replace(" ", "")
# print(data)

# or
# data = "   삼성전자    "
# data = data.strip()
# print(data)

# 041
# ticker = "btc_krw"
# ticker = ticker.upper()

# print(ticker)

# 042
# ticker = "BTC_KRW"
# ticker = ticker.lower()

# print(ticker)

# 043
# a = "hello"
# a = a.capitalize()

# print(a)

# 044
# file_name = "보고서.xlsx"

# if file_name.endswith(("xlsx", "xls")):
#     print("Yes")

# else:
#     print("No")

# 045
# file_name = "보고서.xlsx"

# if file_name.endswith(("xlsx", "xls")):
#     print("Yes")

# else:
#     print("No")

# 046
# file_name = "2020_보고서.xlsx"

# if file_name.startswith("2020"):
#     print("Yes")

# 047
# a = "hello world"
# a.split()

# 048
# ticker = "btc_krw"
# ticker.split("_")

# 049
# date = "2020-05-01"
# date.split("-")

# 050
# data = "039490     "
# data.rstrip()

# 051
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 052
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)

# 053
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# 054
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
# print(movie_rank)

# or
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)

# 055
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# 056
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]

# langs = lang1 + lang2

# print(langs)

# 057
# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max: ", max(nums))
# print("min: ", min(nums))

# 058
# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# 059
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# 060
# nums = [1, 2, 3, 4, 5]
# average = sum(nums) / len(nums)
# print(average)

# 061
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# 062
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# 063
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# 064
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# 065
# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# 066
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))

# 067
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("/".join(interest))

# 068
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))

# 069
# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)

# 070
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

# or
# data = [2, 4, 3, 1, 5, 10, 9]
# data2 = sorted(data)
# print(data2)

# 071
# my_variable = ()
# print(type(my_variable))

# 072
# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
# print(movie_rank)

# 073
# my_tuple = (1, )

# 074
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
#tuple은 원소(element)의 값을 변경할 수 없습니다.

# 075
# ~~~

# 076
# t = ("a", "b", "c")
# t = ("A", "b", "c")

# 077
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# dta = list(interest)
# print(type(interest))

# 078
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# data = tuple(interest)
# print(type(interest))

# 079
# apple banana cake

# 080
# data = tuple(range(2, 100, 2))
# print(data)
# range(start, stop, step)

# range(0, 20, 2)

# 0, 2, 4, 6, 8, 10, 12, 14, 16, 18

# 마지막 인자 step은 숫자의 간격을 나타낸다.

# range(20, 0, -2)

# 20, 18, 16, 14, 12, 10, 8, 6, 4, 2

# step으로 음수를 지정할 수 있다.

# 081
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _= scores
# print(valid_score)

# 082
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score = scores
# print(valid_score)

# 083
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score = scores
# print(valid_score)

# 084
# temp = {}

# 085
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# print(ice)

# 086
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice["죠스바"] = 1200
# ice["월드콘"] = 1500
# print(ice)

# 087
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# print("메로나 가격: ", ice["메로나"])

# 088
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# ice["메로나"] = 1300
# print(ice)

# 089
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# del ice["메로나"]
# print(ice)

# 090
#누가바를 추가하고 속성을 입력하지 않았다

# 091
# inventory = {'메로나': [300, 20],
#              '비비빅': [400, 3],
#              '죠스바': [250, 100]}

# print(inventory)

# 092
# inventory = {"메로나": [300, 20],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}

# print(inventory["메로나"][0], "원")

# 093
# inventory = {"메로나": [300, 20],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}

# print(inventory["메로나"][1], "개")

# 094
# inventory = {"메로나": [300, 20],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}

# inventory["월드콘"] = 500, 7

# print(inventory)

# 095
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# ice = list(icecream.keys())
# print(ice)

# 096
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# ice = list(icecream.values())
# print(ice)

# 097
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = list(icecream.values())

# sum = 0
# i = 0

# for i in range(5):
#     sum += ice[i]
    
# print(sum)

# or
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(sum(icecream.values()))

# # 098
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}

# icecream.update(new_product)

# print(icecream)

# 099
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)

# result = dict(zip(keys, vals))

# print(result)

# 100
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]

# close_table = dict(zip(date, close_price))

# print(close_table)

# 101
# bool 타입

# 102
# False

# 103
# True

# 104
# True

# 105
# True

# 106
# 기호의 순서가 잘못됨

# 107
# 출력 안됨

# 108
# Hi, there.

# 109
# 1
# 2
# 4

# 110
# 3
# 5

# 111
# user = input("입력: ")
# print(user * 2)

# 112
# user = input("숫자를 입력하세요: ")
# print(int(user) + 10)

# 113
# user = input("숫자를 입력해주세요: ")

# if int(user) % 2 == 0:
#     print("짝수입니다.")

# else:
#     print("홀수입니다.")

# 114
# user = input("숫자를 입력해주세요: ")

# if int(user) + 20 > 255:
#     print(255)

# else:
#     print(int(user) + 20)

# 115
# user = input("숫자를 입력해주세요: ")

# if int(user) - 20 > 255:
#     print("255")

# elif int(user) - 20 < 0:
#     print("0")

# else:
#     print(int(user) - 20)

# 116
# user_time = input("현재시간(XX:XX): ")

# if user_time[-2:] == "00":
#     print("정각입니다")

# else:
#     print("정각이 아닙니다")

# 117
# user_fruit = input("좋아하는 과일은?: ")
# fruit = ["사과", "포도", "홍시"]

# if user_fruit in fruit:
#     print("정답입니다.")

# else:
#     print("오답입니다.")

# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# user_investment_name = input("종목명을 입력해주세요: ")

# if user_investment_name in warn_investment_list:
#     print("투자 경고 종목입니다.")

# else:
#     print("투자 경고 종목이 아닙니다.")

# 119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("좋아하는 계절은: ")
# if user in fruit:
#     print("정답입니다.")

# else:
#     ("오답입니다.")

# 120
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# user = input("좋아하는 과일은?: ")
# if user in fruit.values():
#     print("정답입니다.")

# else:
#     print("오답입니다.")

# 121
# user = input("영문자를 입력해주세요: ")

# if user.islower() == True:
#     print(user.upper())

# else:
#     print(user.lower())

# 122
# user_score = input("score: ")
# score = int(user_score)
# if score > 80:
#     print("grade is A")

# elif score > 60:
#     print("socre is B")

# elif score > 40:
#     print("score is C")

# elif score > 20:
#     print("socre is D")

# elif score >= 0:
#     print("score is E")

# 123
# Exchange_Rate = {'달러': 1167, '엔': 1.096, '유로': 1268, '위안': 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * Exchange_Rate[currency], "원")

# 124
# user_num1 = input("첫 번째 수를 입력해주세요: ")
# user_num2 = input("두 번째 수를 입력해주세요: ")
# user_num3 = input("세 번째 수를 입력해주세요: ")

# user_num1 = int(user_num1)
# user_num2 = int(user_num2)
# user_num3 = int(user_num3)

# if user_num1 >= user_num2 and user_num1 >= user_num3:
#     print(user_num1)

# elif user_num2 >= user_num1 and user_num2 >= user_num3:
#     print(user_num2)

# else:
#     print(user_num3)

# 125
# user_phone_num = input("휴대전화 번호를 입력해주세요 (- 포함): ")

# num = user_phone_num.split("-")[0]

# if num == "011":
#     com = "SKT"

# elif num == "016":
#     com = "KT"

# elif num == "019":
#     com = "LGU"

# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")

# 126
# num = input("우편번호를 입력해주세요: ")

# num = num[:3]

# if num in ["010", "011", "012"]:
#     print("강북구")

# elif num in ["013", "014", "015"]:
#     print("도봉구")

# else:
#     print("노원구")

#127
# num = input("주민등록번호를 입력하세요(ex 123456-1234567): ")

# num = num[7:8]

# if num == 1 or 3:
#     print("남자")

# else:
#     print("여자")

# 128
# num = input("주민등록번호: ")
# num = int(num[8:10])
# if 0 <= num <= 8:
#     print("서울입니다")

# else:
#     print("서울이 아닙니다")

# or

# num = input("주민등록번호: ")
# bnum = num.split("-")[1]
# if 0 <= int(bnum[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

# 129
# num = input("주민등록번호: ")
# CALC1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10]) * 3 + int(num[11]) * 4 + int(num[12]) * 5

# CALC2 = str(11 - (CALC1 % 11))

# if CALC2 == num[-1]:
#     print("유효한 주민등록번호입니다")

# else:
#     print("유효하지 않은 주민등록번호입니다")

# 130
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print(btc)

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")



































