# Brute force algorith to test results
for x in range(1,1000):
    if ((x % 17) == 9) and ((x % 12) == 9) and ((x % 19) == 13):
        print(x)