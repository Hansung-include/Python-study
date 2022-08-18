from ctypes.wintypes import PINT
from difflib import context_diff
from queue import PriorityQueue
from tabnanny import verbose
from unittest import mock


coffee = 10
while True:
    money = int(input('돈을 넣어 주세요 : '))
    if money == 300:
        print('커피를 줍니다')
        coffee = coffee - 1 #coffe -= 1 로 사용 가능
    elif money > 300:
        print('거스름돈 %d를 주고, 커피를 줍니다.' % (money - 300))
        coffee = coffee - 1
    else:
        print('돈을 돌려주고 커피를 주지 않습니다.')
        print('남은 커피의 양은 %d 개 입니다.' % coffee)
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 종료합니다.')
        break