import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            first = Runner('Alex', -5)
            for i in range(10):
                first.walk()
            self.assertEqual(first.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as ex:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            second = Runner(324, 5)
            for i in range(10):
                second.run()
            self.assertEqual(second.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except TypeError as ex:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        third = Runner('Ben', 10)
        forth = Runner('Scarlet', 10)
        for i in range(10):
            third.walk()
            forth.run()
        self.assertNotEqual(third.distance, forth.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()
