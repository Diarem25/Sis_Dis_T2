import random
import numpy as np
from Static_plant.factory1 import Factory1
from Dynamic_plant.factory2 import Factory2

class Controller:
    def __init__(self):
        self.factory1 = Factory1(5, 960)
        self.factory2 = Factory2(8, 160)
        self.daily_demand = 0
        self.total_produced = 0

    def run_day(self):
        self.daily_demand = random.randint(230, 270)  # Random demand between 230 and 270
        print(f"Market demand for the day: {self.daily_demand} products")

        # Generate random binomial demand for different products
        a = self.generate_random_binomial()
        b = self.generate_random_binomial()
        c = self.generate_random_binomial()
        d = self.generate_random_binomial()
        e = self.daily_demand - a - b - c - d

        print(f"The demand of the different products are\n1: {a}\n2: {b}\n3: {c}\n4: {d}\n5: {e}")

        active_lines = self.daily_demand // 48
        print(f"Number of active lines: {active_lines}")

        self.total_produced = self.factory1.run_production(active_lines)

        if self.total_produced < self.daily_demand:
            remaining_demand = self.daily_demand - self.total_produced

            # Set product types and run production in Factory 2
            product_types = [remaining_demand, a, b, c, d, e]
            produced_by_factory2 = self.factory2.run_production(product_types)
            self.total_produced += produced_by_factory2

        print(f"Total products produced: {self.total_produced}")

        # Display status of storage after replenishing
        self.factory1.display_status()
        self.factory2.display_status()

        # Show performance review
        points = self.performance_review()
        print(f"Performance Points for the Day: {points}")

        # Replenish stock after production
        self.replenish_stock()

    def replenish_stock(self):
        # Replenish stock for Factory 1 (Base storage)
        base_storage = self.factory1.get_storage()
        if base_storage.get_traffic_light() in ["Yellow", "Red"]:
            stock_f1 = 960 - base_storage.base_stock
            base_storage.replenish_base(stock_f1)
            print("Replenished base stock in Factory 1.")

        # Replenish stock for Factory 2 (Variable storage)
        var_storage = self.factory2.get_storage()
        for i in range(6):
            if var_storage.get_traffic_light(i) in ["Yellow", "Red"]:
                stock_f2 = 160 - var_storage.get_stock(i)
                var_storage.replenish_part(i, stock_f2)
                print(f"Replenished part {i} stock in Factory 2.")

    def generate_random_binomial(self):
        # Binomial distribution parameters: n=52 trials, p=44/52 probability of success
        result = np.random.binomial(52, 44.0 / 52.0)
        return int(result)  # Ensure the result is an integer

    def performance_review(self):
        points = 0

        # Check traffic light performance for Factory 1
        base_traffic = self.factory1.get_storage().get_traffic_light()
        if base_traffic == "Green":
            points += 1
        elif base_traffic == "Yellow":
            points += 0.5

        # Check traffic light performance for Factory 2
        for i in range(6):
            part_traffic = self.factory2.get_storage().get_traffic_light(i)
            if part_traffic == "Green":
                points += 1
            elif part_traffic == "Yellow":
                points += 0.5

        # Add 3 points if the demand quota is met
        if self.total_produced >= self.daily_demand:
            points += 3

        # Subtract 0.1 points for each leftover product if overproduction occurs
        if self.total_produced > self.daily_demand:
            leftover = self.total_produced - self.daily_demand
            points -= leftover * 0.1

        return points
