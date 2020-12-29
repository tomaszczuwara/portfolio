def startstop(func):
    def decorated_func():
        print("Start")
        func()
        print("Stop")
    return decorated_func

@startstop
def powitaj_trenera():
    print(f"Cześć Maciek")

powitaj_trenera()
