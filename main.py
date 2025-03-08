import time

if __name__ == "__main__":
    # Get initial time
    start = time.time()

    import os 
    os.system('python -m pytest tests/')

    # Get the time after the execution is done
    end = time.time()

    time_ = end - start
    print("Execution time: {:.4f}".format(time_))