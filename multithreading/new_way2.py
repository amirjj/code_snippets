#Thread pool executer added to python 3.2
import concurrent.futures
import time


start = time.perf_counter()

def do_something(seconds):
	print(f'Sleeping {seconds} seconds ...')
	time.sleep(seconds)
	return f'Done sleeping ... {seconds}'

with concurrent.futures.ThreadPoolExecutor() as executer:
	secs = [5, 4, 3, 7, 2, 1]
	results = [executer.submit(do_something, sec) for sec in secs]

	for f in concurrent.futures.as_completed(results):
		print(f.result())




end = time.perf_counter()
print(f'finished in {round(end - start, 2)} seconds')

