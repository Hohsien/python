def main():
    i=0
    L = input()
    while i < len(L): 
        if int(L[i]) % 2 == 0:
            L = L[i] + L[:i] + L[i+1:]
        i += 1
    if i == len(L):
        print(L)

if __name__ == "__main__":
    main()