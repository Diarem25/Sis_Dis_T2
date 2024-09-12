from Dynamic_plant.Dynamic_lines.variable_assembly_line import VariableAssemblyLine
from variable_storage import VariableStorage

class Factory2:
    def __init__(self, num_lines, storage_capacity, num_parts=6):
        self.storage = VariableStorage(storage_capacity, num_parts)
        default_product_type = 0
        self.lines = [VariableAssemblyLine(self.storage, default_product_type) for _ in range(num_lines)]

    def set_product_type_for_all_lines(self, product_type):
        product_types = [product_type] * len(self.lines)
        self.set_product_types_for_lines(product_types)

    def set_product_types_for_lines(self, product_types):
        num_types = len(product_types)
        for i in range(len(self.lines)):
            self.lines[i].set_product_type(product_types[i % num_types])

    def run_production(self, product_types):
        total_produced = 0
        var_produced = 0
        actual_lines = min(len(self.lines), len(product_types))

        for i in range(actual_lines):
            product_to_produce = product_types[i]
            for _ in range(product_to_produce):
                if i == 0:
                    total_produced += self.lines[i].produce(i)
                else:
                    var_produced += self.lines[i].produce(i)

                if not self.storage.can_produce(i):
                    break

            if i > 0:
                print(f"Number of variable pieces created: {var_produced}")

        return total_produced

    def display_status(self):
        self.storage.display_status()

    def get_storage(self):
        return self.storage
