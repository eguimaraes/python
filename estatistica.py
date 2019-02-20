
from matplotlib import pyplot as plt
from collections import defaultdict
from collections import Counter
import random
import sys

def getfriendsPlot(nrf,nrftf,nrtxr):
    num_friends = randon_friends(nrf,nrftf)
    friend_counts = Counter(num_friends)
    xs = range(nrtxr)
    ys = [friend_counts[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([0, nrf+1, 0, nrftf])
    plt.title("Histogram da Contagem de Amigos")
    plt.xlabel("# de Amigos")
    plt.ylabel("# of Pessoas")
    plt.show()


def randon_friends(nrf,nrtf):
    return [int(random.random()*nrtf)*100 for _ in range(nrf)]

getfriendsPlot(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))

