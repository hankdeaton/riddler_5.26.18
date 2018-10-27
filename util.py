import random
import matplotlib

def selectThree(array):
    three = sorted(random.sample(array, 3))
    return three

def selectTwo(array):
    two = sorted(random.sample(array, 2))
    return two

def singleAttack(three, array, scores):
    trap1 = array[three[0]]
    trap2 = array[three[1]]
    trap3 = array[three[2]]

    if random.random() <= trap1/100.:
        scores[three[0]] = scores[three[0]] + 1
    elif random.random() <= trap2/100.:
        scores[three[1]] = scores[three[1]] + 1
    elif random.random() <= trap3/100.:
        scores[three[2]] = scores[three[2]] + 1

def sim(all_traps, scores, tests_per_trap):
    for i in range(0,100):
        for j in range(0, tests_per_trap):
            two = sorted(selectTwo(all_traps))
            three = [0]*3
            if (i< two[0]) & (i<two[1]):
                three[0] = i
                three[1] = two[0]
                three[2] = two[1]
                index = 0
            elif (i>=two[0]) & (i <two[1]):
                three[0] = two[0]
                three[1] = i
                three[2] = two[1]
                index = 1
            else:
                three[0] = two[0]
                three[1] = two[1]
                three[2] = i
                index = 2

            trap1 = three[0]
            trap2 = three[1]
            trap3 = three[2]

            if random.random() <= trap1/100.:
                caught = 0
            elif random.random() <= trap2/100.:
                caught = 1
            elif random.random() <= trap3/100.:
                caught = 2
            else:
                caught = 3

            if index == caught:
                scores[i] = scores[i] + 1
