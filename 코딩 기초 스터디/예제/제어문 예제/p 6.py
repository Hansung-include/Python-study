#아래 코드를 리스트 내포를 이용하여 표현
'''
numbers = [1, 2, 3, 4, 5]
result =  []
for n in numbers:
    if n %2 == 1:
        result.append(n*2)
print(result)
'''

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)