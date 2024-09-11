class FixedAssemblyLine:
    def __init__(self, storage):
        self.daily_production = 48
        self.storage = storage

    def produce(self):
        produced = 0
        for _ in range(self.daily_production):
            if self.storage.consume_base():
                produced += 1
            else:
                break
        return produced
