from cgi import print_arguments


treehit = 0
while treehit < 10:
    treehit = treehit +1 #treehit += 1 로도 사용 가능
    print('나무를 %d번 찍었습니다' % treehit)
    if treehit ==10:
        print('나무 넘어갑니다.')
