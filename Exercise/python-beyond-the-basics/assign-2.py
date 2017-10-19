# coding: utf-8


from assignments import LogFile, DelimFile


log = LogFile('log.txt')
c = DelimFile('text.csv', ',')

log.write('this is a log message')
log.write('this is another log message')

c.write(['a', 'b', 'c', 'd'])
c.write(['1', '2', '3', '4'])

# result:

# log.txt

# 2017-10-11 12:33    this is a log message
# 2017-10-11 12:33    this is another log message

# text.csv

# a,b,c,d
# 1,2,3,4
