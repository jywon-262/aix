# ch05.py (ch05 모듈이라고 함) 자동완성핫키 : ctrl+space
# ctrl + shift p => select interpreter을 이용해서 인터프리터(base) 선택
# 실행 : cmd 터미널(ctrl+j)에서 python ch05.py
def my_hello(cnt): #cnt번 반복
    print(__name__)
    for i in range(cnt):
        print('Hello, Python', end='\t')
        print('Hello, World')
if __name__ == '__main__':
    my_hello(2)



new_lists = []
lists = [[3,4,9] , [2,9,3,44], ['p', 'y', 't']] 

for lst in lists:
  for i in lst:
    new_lists.append(i)
new_lists

new_lists.remove("p")
new_lists
del new_lists[-2:]
sorted(new_lists)





while True:
   answer=int(input("10곱하기 10의 정답은요?"))
   if answer !=100:
      continue
   else:
      print("맞았습니다.")
      break
   


lists = [3, 4, 9, 2, 9, 3, 44, 'p', 'y', 't']
li=lists[:-3]
li














