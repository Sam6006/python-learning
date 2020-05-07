# ### 信号量（线程)
from threading import Semaphore, Thread
import time, random
def func(i,sem):
	#异步并发线程
	time.sleep(random.uniform(0.1, 1))
	with sem:
		print(i)
		time.sleep(2)

if __name__ == '__main__':
	sem = Semaphore(5)
	for i in range(20):
		Thread(target=func, args=(i, sem)).start()




















