#파이썬 비교 연산자
'''
  비교 연산자
x < y  x가 y보다 작다.
x > y  x가 y보다 크다.
x == y x와 y가 같다.
x != y x와 y가 같지 않다.
x >= y x가 y보다 크거나 같다.
x <= y x가 y보다 작거나 같다.
'''


for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if i % 2 is not 0:
        print(i, '홀수')
    else:
        print(i, '짝수')
