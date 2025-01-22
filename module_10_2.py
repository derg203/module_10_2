import threading
from time import sleep
class Knight(threading.Thread):

    def __init__(self, name : str , power : int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        day = 1
        units = 100
        while units > 0:
            sleep(1)
            units -= self.power
            print(f'{self.name}, сражается {day} день(дня)..., осталось {units} воинов.')
            if units == 0:
                print(f'{self.name} одержал победу спустя {day} дней(дня)!')
            day += 1




#print(f'{self.name}, сражается {k} день(дня)..., осталось {100 - i} воинов.')


knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight('Sir Galahad', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончены!')