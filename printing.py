if __name__ == '__main__':
    lyst = []

    # Creating Nested lists using for loop
    n = int(input())
    for i in range(n):
        lyst.append([])

        for j in range(1):

            name = input()
            score = float(input())

            lyst[i].append(name)
            lyst[i].append(score)
    # print(lyst)

    # Getting the scores separately in a list
    scores = []
    for i in range(n):
        scores.append(lyst[i][1])
    # print(scores)

    # To find the second largest marks in the scores
    big = min(scores)
    second_big = 99999999
    for i in range(n):
        if lyst[i][1] != big and lyst[i][1] < second_big:
            second_big = lyst[i][1]

    # print(second_big)

    # To print the names of the students scored second marks
    for i in range(n):
        if second_big == lyst[i][1]:
            print(lyst[i][0])