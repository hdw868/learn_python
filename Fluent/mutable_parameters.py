class MagicBus(object):
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=None):
        if not passengers:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class Bus(object):
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=None):
        if not passengers:
            self.passengers = []
        else:
            self.passengers = list(passengers)  # Make a copy here

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = Bus(basketball_team)
    magic_bus = MagicBus(basketball_team)
    bus.drop('Maya')
    print(basketball_team)
    magic_bus.drop('Tina')
    print(basketball_team)
