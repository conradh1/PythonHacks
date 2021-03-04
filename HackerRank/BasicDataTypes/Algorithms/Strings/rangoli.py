def print_rangoli(size):
    # your code goes here
    rangoli = list(map(chr, range(97, 97+size))).reverse()

    for i in range(0, len(rangoli))
        print rangoli[i]


if __name__ == '__main__':
    size = int(raw_input().strip())
    print_rangoli(size)
