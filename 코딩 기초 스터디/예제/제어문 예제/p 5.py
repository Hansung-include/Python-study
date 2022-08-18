#for 문을 사용하여 a학급의 평균 점수 구하기
a = [70, 60, 55, 75, 95, 90, 80, 85, 100]
all = 0
for score in a:
    all += score
aver = all / len(a)
print(aver)