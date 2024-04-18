import PageReplacement

def main():
    # Sample Input
    reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    frames = 4

    # LRU
    print("For LRU Algorithm:")
    lru = PageReplacement(reference_string, frames)
    lru.lru_algorithm()

    # Optimal
    print("\nFor Optimal Algorithm:")
    optimal = PageReplacement(reference_string, frames)
    optimal.optimal_algorithm()

    # FIFO
    print("\nFor FIFO Algorithm:")
    fifo = PageReplacement(reference_string, frames)
    fifo.fifo_algorithm()


if __name__ == "__main__":
    main()