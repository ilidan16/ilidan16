from progressbar import printProgressBar
import time

t0 = 1620680400
aim = 50*24*3600
t = 0
while t <= aim:
    t = time.time() - t0
    printProgressBar(t, aim, decimals = 4,
                     prefix = 'Progress:',
                     suffix = f'{time.strftime("|%d %H:%M:%S", time.gmtime(t))}',
                     length = 50)
    time.sleep(1)
