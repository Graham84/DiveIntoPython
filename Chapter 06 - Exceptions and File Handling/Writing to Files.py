# >>> logfile = open('test.log', 'w')
# >>> logfile.write('test succeeded')
# >>> logfile.close()
# >>> print file('test.log').read()
# test succeeded
# >>> logfile = open('test.log', 'a')
# >>> logfile.write('line 2')
# >>> logfile.close
# <built-in method close of file object at 0x02285860>
# >>> logfile.close()
# >>> print file('test.log').read()
# test succeededline 2
# >>> logfile = open('test.log', 'a')
# >>> logfile.write('\nline 3')
# >>> logfile.close()
# >>> print file('test.log').read()
# test succeededline 2
# line 3
# >>>
