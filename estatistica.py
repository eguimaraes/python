
from matplotlib import pyplot as plt
from collections import defaultdict
from collections import Counter
import random
import sys

def getfriendsPlot(nrf):
    num_friends = randon_friends(nrf)
    friend_counts = Counter(num_friends)
    print(str(friend_counts))
    xs = range(101)
    ys = [friend_counts[x] for x in xs]
    num_points = len(num_friends)
    largest_value = max(num_friends)
    smallest_value = min(num_friends)
    sorted_values = sorted(num_friends)
    smallest_value = sorted_values[0]
    second_smallest_value = sorted_values[1]
    second_largest_value = sorted_values[-2]
    
    plt.bar(xs, ys)
    plt.axis([0, nrf+1, 0, 5])
    plt.title("Histogram da Contagem de Amigos")
    plt.xlabel("# de Amigos")
    plt.ylabel("# of Pessoas")
    plt.show()


def randon_friends(nrf):
    retorno=[int(random.random()*nrf) for _ in range(nrf)]
    print(retorno)
    
    return retorno

def mean(x):
    return sum(x) / len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
    return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
    if count == max_count]


def data_range(x):
        return max(x) - min(x)

def de_mean(x):
        x_bar = mean(x)
        return [x_i - x_bar for x_i in x]

def variance(x):
        n = len(x)
        deviations = de_mean(x)
        return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
        return math.sqrt(variance(x))   

def interquartile_range(x):
        return quantile(x, 0.75) - quantile(x, 0.25)

def covariance(x, y):
        n = len(x)
        return dot(de_mean(x), de_mean(y)) / (n - 1)

getfriendsPlot(int(sys.argv[1]))


