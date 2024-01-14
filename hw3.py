class Bank:
    def __init__(self,name,balanse):
        self._name = name
        self._balanse = balanse

    def moneyX(self):
        print(f"Ваш баланс {self._balanse}")
        user = int(input('Введите сумму которую нужно добавить: '))
        if 0 < user:
            self._balanse += user
            print(f"Теперь ваш баланс: {self._balanse}")
        else:
            print("Вы ввели недопустимое число")

    def _kill(self):
        self._balanse = 0
        print(f"Вы обнулили свой баланс {self._balanse}")

    def __jackpot(self):
        self._balanse *= 10
        print(f"Поздравляю вы получили джекпот {self._balanse}")

    def _join(self):
        self._balanse += self._balanse


