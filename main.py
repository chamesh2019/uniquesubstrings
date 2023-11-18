def unique_substrings(string, length):
    substrings = set()
    for i in range(len(string) - length + 1):
        substrings.add(string[i:i + length])
    return substrings

if __name__ == "__main__":
    string = input()
    length = int(input())
    print(len(unique_substrings(string, length)))