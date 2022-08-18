#while 문을 사용하여 1부터 1000까지의 수 중 3의 배수의 합 구하기
a = 0
b = 1
while b <= 1000:
    if b % 3 == 0:
        a = a + b
    b = b + 1
print(a)