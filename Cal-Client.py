import Pyro4

def main():
    uri = input("Enter the URI from the server: ")
    cal = Pyro4.Proxy(uri)

    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))

    res1 = cal.add(a, b)
    res2 = cal.mul(a, b)

    print("Addition result:", res1)
    print("Multiplication result:", res2)


if __name__ == "__main__":
    main()
