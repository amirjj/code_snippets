#Thread pool executer added to python 3.2
import concurrent.futures
import time


start = time.perf_counter()

def do_something(seconds):
	print(f'Sleeping {seconds} seconds ...')
	time.sleep(seconds)
	return f'Done sleeping ... {seconds}'

with concurrent.futures.ThreadPoolExecutor() as executer:
	secs = [5, 4, 3, 2, 1]
	results = executer.map(do_something, secs)

	for res in results:
		print(res)




end = time.perf_counter()
print(f'finished in {round(end - start, 2)} seconds')

