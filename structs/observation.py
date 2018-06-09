from structs.condition import Condition


class Observation:
    def __init__(self, condition: Condition, begin_time: int):
        self.condition = condition
        self.begin_time = begin_time