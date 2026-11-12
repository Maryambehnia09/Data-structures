def Duplicate(s):

    start = 0
    n = len(s)

    while start < n:

        length = n - start

        if length == 1:
            return False

        if length % 2 == 0:

            mid = length // 2
            equal = True

            for i in range(mid):
                if s[start + i] != s[start + mid + i]:
                    equal = False
                    break

            if equal:
                return True

        start += 1

    return True


s = input("Enter a string: ")

if Duplicate(s):
    print("Duplicate")
else:
    print("Not Duplicate")