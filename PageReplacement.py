class PageReplacement:
    def __init__(self, reference_string, frames):
        self.reference_string = reference_string
        self.frames = frames
        self.page_table = []
        self.page_faults = 0

    def print_step(self, step, page):
        print(f"Step {step}: Page fault ({page}) - Page Table: {self.page_table}, Frames: {self.page_table}, Faults: {self.page_faults}")

    def lru(self): # LRU
        for step, page in enumerate(self.reference_string):
            if page not in self.page_table:
                if len(self.page_table) == self.frames:
                    self.page_table.pop(0)
                self.page_table.append(page)
                self.page_faults += 1
                self.print_step(step + 1, page)
            else:
                self.page_table.remove(page)
                self.page_table.append(page)
                
        print(f"Total Page Faults: {self.page_faults}")

    def optimal(self): # Optimal
        for step, page in enumerate(self.reference_string):
            if page not in self.page_table:
                if len(self.page_table) == self.frames:
                    # Find the page that will not be used for the longest time
                    future_occurrences = {p: float('inf') for p in self.page_table}
                    for i in range(step + 1, len(self.reference_string)):
                        if self.reference_string[i] in future_occurrences:
                            future_occurrences[self.reference_string[i]] = i
                    page_to_replace = min(future_occurrences, key=future_occurrences.get)
                    self.page_table.remove(page_to_replace)
                self.page_table.append(page)
                self.page_faults += 1
                self.print_step(step + 1, page)

        print(f"Total Page Faults: {self.page_faults}")

    def fifo(self): # FIFO
        for step, page in enumerate(self.reference_string):
            if page not in self.page_table:
                if len(self.page_table) == self.frames:
                    self.page_table.pop(0)
                self.page_table.append(page)
                self.page_faults += 1
                self.print_step(step + 1, page)

        print(f"Total Page Faults: {self.page_faults}")