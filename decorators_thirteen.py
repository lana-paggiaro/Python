def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Get in loser, we're going shopping.")

hello()