import threading

# a function to print number upto a limit
def print_number(limit):
    for i in range(limit):
        print(i)


# a function to print characters
def print_character():
    
    # repeat 'loop' 100 times
    my_string = 'loop'*100

    for i in my_string:
        print(i)


# create thread objects for each function
thread1 = threading.Thread(target=print_number, args=(400, ))
thread2 = threading.Thread(target=print_character)

# start both threads
thread1.start()
thread2.start()

# Optional: wait until the thread1 has been completed
thread1.join()


print('This wont run until thread1 has been completed.')
