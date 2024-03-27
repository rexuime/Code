num = 0

def increment():
    global num 
    num += 1

if __name__ == "__main__":

    increment()
    print(num)