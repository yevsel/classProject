from itertools import permutations
import matplotlib.pyplot as plt
import numpy as np


class Passwords:
    __upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, password_length):
        self.__password_lenght = password_length

    def get_possible_passwords(self):
        return len(list(permutations(Passwords.__upper_cases, self.__password_lenght)))

    def show_samples(self, number_of_samples):
        for i in range(number_of_samples):
            print(
                ''.join(list(permutations(Passwords.__upper_cases, self.__password_lenght))[i]), ' ', end='')


pass1 = Passwords(3)
print(pass1.get_possible_passwords())
pass1.show_samples(5)
