def addprint(a, b):
    print(a + b)
#a + b연산 값을 출력합니다.
def addReturn(a, b):
    return a + b
#a + b연산 값을 반환합니다.
addprint(1, 2)
addReturn(1, 2)

print('The result is', addprint(1, 2))
#문장이 제대로 출력되지 않습니다.
print('The result is', addReturn(1, 2))
#문장이 제대로 출력됩니다.
