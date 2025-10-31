#파일 입출력 관리
import os
#os 모듈을 임포트 
print(os.getcwd()) #현재 위치한 경로가 표시됩니다

os.chdir('C:/work/standard/files') #\를 하나 더 덧붙입니다
# 'C:\\work\standard\\.venv\\Scripts\\python' #주솟값은 실습 환경에 따라 다릅니다.
print(os.getcwd()) #현재 위치한 경로가 표시됩니다

folderFile = os.listdir()
# print(folderFile[0]) #폴더안의 파일 확인하기
# folderFile = os.listdir() #folderFile이라는 객체에os.listdir()의 결괏값을 저장합니다.
# type(folderFile) #folderFile의 타입을 알아봅시다!
# print(folderFile)

# #open()함수 사용법
# #파일 객체 = open('파일 이름',파일 열기 모드)
# open('a.txt' , 'w') #객체 이름을 저장하지 않아도 파일은 열립니다.
# open('a.txt' , 'w').write('abc') #a.txt파일에 abc라는 무자열을 사용함/입력한 문자의 개수가 출력됩니다.
f = open('a.txt' , 'w') #F = open(파일 이름, 파일 열기모드)
# '''
#     파일 열기 모드   |           의미
#          'w'       |파일에 내용을 새로 쓸 떄 사용
#          'r'       | 파일 내용을 읽을떄 사용
#          'a'       | 파일에 내용을 추가할떄 사용
# '''
f.write('Hello World!\n')
f.write('Hello World!')

f.close()

# f.close() #파일 닫기를 잊으면 안됌.
# f.read() #파일을 읽으라는 의미.
# f.seek() #파일 가장 처음으로 커서를 이동하라는 의미 입니다.
# '''
# with 문 사용법
# with open(파일 이름, 파일 열기 모드) as f:
# f에 수행할 명령
# '''
# '''
# 파이썬에서 파일을 열떄 한글파일은 오류가 잘남
# 해결방법:f = open('한글파일.txt', 'r', encoding = 'utf8')
# '''




