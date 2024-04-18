from PageReplacement import *

def main():
    # Sample Input
    reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    frames = 4
    
    # LRU
    print("For LRU Algorithm:")
    lru = PageReplacement(reference_string, frames)
    lru.lru()

    # Optimal
    print("\nFor Optimal Algorithm:")
    optimal = PageReplacement(reference_string, frames)
    optimal.optimal()

    # FIFO
    print("\nFor FIFO Algorithm:")
    fifo = PageReplacement(reference_string, frames)
    fifo.fifo()


if __name__ == "__main__":
    main()