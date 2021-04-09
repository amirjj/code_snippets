#Thread pool executer added to python 3.2
import concurrent.futures
import time


start = time.perf_counter()

def do_something(seconds):
	print(f'Sleeping {seconds} seconds ...')
	time.sleep(seconds)
	return 'Done sleeping ...'

with concurrent.futures.ThreadPoolExecutor() as executer:
	f1 = executer.submit(do_something, 1)
	f2 = executer.submit(do_something, 1)
	print(f1.result())
	print(f2.result())




end = time.perf_counter()
print(f'finished in {round(end - start, 2)} seconds')

