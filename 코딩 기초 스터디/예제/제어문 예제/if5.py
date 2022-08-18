from cgi import print_arguments
from unittest import mock


poket = ['paper', 'cellphone', 'money']
if 'money' in poket:
    print('택시를 타고 가라')
else:
    print('걸어 가라')
    