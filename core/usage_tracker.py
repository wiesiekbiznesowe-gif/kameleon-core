class UsageTracker:

    def __init__(self):
        self.counter = {}

    def track(self, engine):

        if engine not in self.counter:
            self.counter[engine] = 0

        self.counter[engine] += 1

        print(f"[USAGE] {engine}: {self.counter[engine]}")
