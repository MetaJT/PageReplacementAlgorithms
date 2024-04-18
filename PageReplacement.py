class PageReplacement:
    def __init__(self, reference_string, frames):
        self.reference_string = reference_string
        self.frames = frames
        self.pages = []
        self.faults = 0

    def print_step(self, step, page):
        print(f"Step {step}: Page fault ({page}) - Page Table: {self.pages}, Frames: {self.pages}, Faults: {self.faults}")

    def lru(self): # LRU
        for step, page in enumerate(self.reference_string):
            if page not in self.pages:
                # If the size of pages matches the number of frames then pop the first page
                if len(self.pages) == self.frames:
                    self.pages.pop(0)
                # If page not in pages then append to back
                self.pages.append(page)
                self.faults += 1
                self.print_step(step + 1, page)
            else:
                # If the page exists remove it and append it to the back
                self.pages.remove(page) 
                self.pages.append(page)

        print(f"Total Page Faults: {self.faults}")

    def optimal(self): # Optimal
        for step, page in enumerate(self.reference_string):
            if page not in self.pages:
                if len(self.pages) == self.frames:
                    # Find the page that will not be used for a while
                    future_occurrences = {p: float('inf') for p in self.pages}
                    for i in range(step + 1, len(self.reference_string)):
                        if self.reference_string[i] in future_occurrences:
                            future_occurrences[self.reference_string[i]] = i
                    # Find the min of the future page occurences and remove it
                    page_to_replace = min(future_occurrences, key=future_occurrences.get)
                    self.pages.remove(page_to_replace)
                # Add the current page to the back
                self.pages.append(page)
                self.faults += 1
                self.print_step(step + 1, page)

        print(f"Total Page Faults: {self.faults}")

    def fifo(self): # FIFO
        for step, page in enumerate(self.reference_string):
            if page not in self.pages:
                # If the size of pages matches the number of frames we'll just pop from the front
                if len(self.pages) == self.frames:
                    self.pages.pop(0)
                # Append the current page to the back
                self.pages.append(page)
                self.faults += 1
                self.print_step(step + 1, page)

        print(f"Total Page Faults: {self.faults}")