#Benefits of multithreading is mostly when the operation is IO bound
#If the task is CPU bound we are not going to have considerable benefits with multithreading

import threading
import time

start = time.perf_counter()

def do_something():
	print('sleeping 1 sec...')
	time.sleep(1)
	print('done sleeping ...')

t1 = threading.Thread(target = do_something)
t2 = threading.Thread(target = do_something)

t1.start()
t2.start()

#make sure it complete before moving on next line
t1.join()
t2.join()

end = time.perf_counter()

print(f'Finished in {round(end-start,2)} seconds')