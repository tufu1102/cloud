import Pyro4

@Pyro4.expose
class Calculator:
    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b


def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(Calculator)
    print("Ready. Object uri =", uri)
    daemon.requestLoop()


if __name__ == "__main__":
    main()
