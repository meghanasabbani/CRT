def even_odd(n):
    if n%2==0:
        if n>=2 and n<=5:
            return "Not weird"
        if n>=6 and n<=20:
            return "weird"
        if n>20:
            return "Not weird"
    else:
        return "weird"
if __name__ == "__main__":
    n = int(input())
    print(even_odd(n))  