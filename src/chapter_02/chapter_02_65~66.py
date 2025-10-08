#서비스 가격 출력 프로그램(교재에 있는 방식)




price = [23, 40, 67]


def service_price():
    service = input('서비스 종류를 입력하시오, a/b/c: ')
    valueAdded = input('부과세를 포함합니까? y/n: ')
    if valueAdded == 'y':
        if service == 'a':
            result = 23 * 1.1
        if service == 'b':
            result = 40 * 1.1
        if service == 'c':
            result = 67 * 1.1
    if valueAdded == 'n':
        if service == 'a':
            result = 20
        if service == 'b':
            result == 40
        if service == 'c':
            result = 67
    print(round(result, 1), '만 원 입니다.')
            
                  
service_price()