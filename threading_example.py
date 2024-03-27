import threading

num = 0
iterations = 100000

lock = threading.Lock()

def increment():
  for i in range(iterations):
    with lock:
        global num 
        num += 1

# Lock.acquire
# Lock.release
    
# Create a list of threads
threads = []

# Create a thread for each argument
t1 = threading.Thread(target=increment)
threads.append(t1)
t2 = threading.Thread(target=increment)
threads.append(t2)

# Start all the threads
for thread in threads:
  thread.start()

# Wait for all the threads to finish
for thread in threads:
  thread.join()

print(num)