from fixed_assembly_line import FixedAssemblyLine
from base_storage import BaseStorage

class Factory1:
    def __init__(self, num_lines, storage_capacity):
        self.storage = BaseStorage(storage_capacity)
        self.lines = [FixedAssemblyLine(self.storage) for _ in range(num_lines)]

    def run_production(self, num_lines_to_run):
        total_produced = 0

        actual_lines_to_run = min(num_lines_to_run, len(self.lines))

        for i in range(actual_lines_to_run):
            total_produced += self.lines[i].produce()

        return total_produced

    def display_status(self):
        self.storage.display_status()

    def get_storage(self):
        return self.storage
