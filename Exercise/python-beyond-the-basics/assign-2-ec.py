# coding: utf-8

from assignments import WriteFile, CSVFormatter, LogFormatter

writecsv = WriteFile('text.csv', CSVFormatter)
writelog = WriteFile('log.txt', LogFormatter)


writecsv.write(['a', 'b', 'c', 'd'])
writelog.write('this is a log message')


writecsv.write(['1', '2', '3', '4'])
writelog.write('this is another log message')


writecsv.close()
writelog.close()
