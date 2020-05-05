# ### 锁
from multiprocessing import Lock, Process
import json, time

'''
创建一把锁
lock = Lock()
#上锁
lock.acquire()
print(123)

#解锁
lock.release()
'''
# 死锁 (只上锁不解锁会差生死锁) 程序添加了阻塞，代码不能往下执行
'''如果上锁一定要解锁，上锁解锁是一对'''
'''
lock.accquire()
lock.accquire()
lock.release()

'''


# 读取票数，更新票数
def wr_info(sign, dic=None):
	if sign == 'r':
		with open('ticket', mode='r', encoding='utf-8') as fp:
			dic = json.load(fp)

		return dic

	elif sign == 'w':
		with open('ticket', mode='w', encoding='utf-8') as fp:
			json.dump(dic, fp)


# print(wr_info('r'), type(wr_info('r')))
# dic = {'count': 2}
# wr_info('w', dic)

# 抢票方法
def get_ticket(person):
	dic = wr_info('r')
	time.sleep(0.1)
	if dic['count'] > 0:
		print('%s抢到票了' % (person))
		dic['count'] -= 1
		# 更新数据库
		wr_info('w', dic)
	else:
		print('%s没有买到票' % person)


#get_ticket('李四')

#用ticket方法来进行统一调用
def ticket(person, lock):
	#先读取票数
	dic = wr_info('r')
	#查询余票
	print('%s 查询余票： %s' %(person, dic['count']))

	lock.acquire()
	#再开始抢票
	get_ticket(person)
	lock.release()


if __name__ == '__main__':
	lock = Lock()
	for i in range(10):
		p = Process(target=ticket, args=('person %s' %(i), lock))
		p.start()

#创建进程的时候是异步程序，再上锁的时候是同步程序