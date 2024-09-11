class VariableStorage:
    def __init__(self, max_capacity, num_parts=6):
        self.max_capacity = max_capacity
        self.part_stock = [max_capacity] * num_parts

    def get_stock(self, part_index):
        return self.part_stock[part_index]

    def set_stock(self, part_index, value):
        if value > self.max_capacity:
            value = self.max_capacity
        self.part_stock[part_index] = value

    def consume_part(self, part_index):
        if self.part_stock[part_index] > 0:
            self.part_stock[part_index] -= 1
            return True
        return False

    def get_traffic_light(self, part_index):
        if self.part_stock[part_index] >= self.max_capacity // 2:
            return "Green"
        elif self.part_stock[part_index] >= self.max_capacity // 4:
            return "Yellow"
        return "Red"

    def display_status(self):
        for i, stock in enumerate(self.part_stock):
            print(f"Part {i} Stock: {stock} ({self.get_traffic_light(i)})")

    def replenish_part(self, part_index, amount):
        self.part_stock[part_index] = min(self.part_stock[part_index] + amount, self.max_capacity)

    def can_produce(self, part_index):
        return self.part_stock[part_index] > 0
