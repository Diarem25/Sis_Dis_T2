class BaseStorage:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.base_stock = max_capacity

    def consume_base(self):
        if self.base_stock > 0:
            self.base_stock -= 1
            return True
        return False

    def get_traffic_light(self):
        if self.base_stock >= 480:
            return "Green"
        elif self.base_stock >= 240:
            return "Yellow"
        return "Red"

    def display_status(self):
        print(f"Base Stock: {self.base_stock} ({self.get_traffic_light()})")

    def can_produce(self):
        return self.base_stock > 0

    def replenish_base(self, amount):
        self.base_stock = min(self.base_stock + amount, self.max_capacity)
