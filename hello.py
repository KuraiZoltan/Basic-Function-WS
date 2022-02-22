print("Hello World")


name = input("What is your name?")
print("Hello,", name)


def hello():
    name = input("What is your name?")
    print("Hello,", name)

name = input("Whats your name?")
def hello(name):
    print("Hello,", name)

hello(name)

def hello(name = "World"):
    print(f"Hello {name} !")

hello()

def hello(send_name, receive_name):
    print(f"{send_name} says hello to {receive_name}")


def hello(*args):
    print(f"Hello, {', '.join(args)}")

hello()
