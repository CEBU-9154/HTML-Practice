def ways(s):
    if s < 0:
        return 0
    if s == 0:
        return 1
    twoSteps=0
    oneStep=0

    if (s>=2):
        twoSteps=ways(s-2)
        oneStep=ways(s-1)
    return twoSteps+oneStep

stairs=int(input("Enter number of steps: "))
print("Number of ways to climb: ", ways(stairs))