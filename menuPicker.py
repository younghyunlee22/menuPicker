# -*- coding: utf-8 -*-
import random
import time

lunch = ["된장찌개", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("추가할 메뉴를 입력하세요: ")
    if (item == "q"):
        break
    else:
        lunch.append(item)

set_lunch = set(lunch)

while True:
    item = input("삭제할 메뉴를 입력하세요: ")
    if (item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item])
        print(list(set_lunch))

print(set_lunch, "중에서 선택합니다.")
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print(random.choice(list(set_lunch)))
