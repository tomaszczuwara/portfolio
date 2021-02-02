def startstop(func):
    def decorated_func():
        print("Start")
        func()
        print("Stop")
    return decorated_func

@startstop
def powitaj_rekrutera():
    print(f"Cześć Królowo Rekrutacji")

powitaj_rekrutera()
