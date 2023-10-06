# 한 줄 짜리 주석
""" 여러 줄의 주석 """

"""

코드 작성 일자 : 2023년 10월 06일
코드 작성자 : 김예준
코드 이름 : utils.py
코드 목적 : 유용한 함수를 따로 저장하여 두고 나중에 보러와 사용하기 위함

파이썬 함수 선언시 위에 두 줄이 있어야한다

"""


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)


def gugudan(x):
    for i in range(9):
        print((i + 1) * x)
