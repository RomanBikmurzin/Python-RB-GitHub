import time
import random


class LoopPracticeClass():
    def __init__(self):
        self.numbers = list(range(1,8))
        self.words = [f"str{i}" for i in range(10)]

    def print_nth_number(self, loop_number:int):
        """Печатает числа до 5, затем прерывается"""
        for n in self.numbers:
            if n == 5: 
                break
            print(n)
            
    def print_all_words(self):
        for word in self.words:
            print(word)

    def imitate_roctics_load(self):
        i = 0
        while i < 10:
            load = random.randint(0, 100)
            if load > 85:
                print(f"Итеграция {i}: Крылышки в опасности! Нагрузка — {load}%")
            else:
                print(f"Итеграция {i}: Стабильная нагрузка в {load}%")
            time.sleep(0.2) # пауза для реализма
            i += 1


def main():
    homework = LoopPracticeClass()
    homework.print_all_words()
    homework.print_nth_number(10)
    homework.imitate_roctics_load()


if __name__ == "__main__":
    main()