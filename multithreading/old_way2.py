import threading
import time

start = time.perf_counter()

def do_something(seconds):
	print(f'sleeping {seconds} sec...')
	time.sleep(seconds)
	print('done sleeping ...')


threads = []

for _ in range(10):
	t = threading.Thread(target=do_something, args =[1.5])
	t.start()
	threads.append(t)

#we need to start all threads and then join them, so we need another loop
for thread in threads:
	thread.join()

end = time.perf_counter()

print(f'Finished in {round(end-start,2)} seconds')