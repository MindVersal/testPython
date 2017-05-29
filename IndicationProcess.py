import sys
import time

for i in range(5, 101, 5):
    sys.stdout.write("\r ... %s%%" % i)
    sys.stdout.flush()
    time.sleep(1)
sys.stdout.write("\rProcess is ended.\n")