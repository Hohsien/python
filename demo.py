def main():
    #print('hello world!')
    #ToLowerCase('Hello World!')
    str = ToLowerCase(input())
    print(str)
    
def ToLowerCase(str):
    i = 0
    while i < len(str):
        if (str[i] >= 'A' and str[i] <= 'Z'):
            str = str[:i] + chr(ord(str[i]) + 32) + str[(i+1):]
        i += 1
    return(str)

if __name__ == "__main__":
    main()