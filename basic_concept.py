import numpy as np

import matplotlib.pyplot as plt


# def random_score(mu=90, sigma=15):
#     score = np.random.normal(mu, sigma, 1000)
#     count, bins, ignored = plt.hist(score, 100, density=True)
#     plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2,
#              color='r')
#     plt.show()
#
#
# random_score(200, 30)


# score11 = np.around(score1, decimals=1)

# chinese_score = np.random.normal(90, 15, 1000)
# np.savetxt('chinese_score.csv', chinese_score, delimiter=',')
#
# math_score = np.random.normal(80, 20, 1000)
# np.savetxt('math_score.csv', math_score, delimiter=',')
#
# english_score = np.random.normal(85, 17, 1000)
# np.savetxt('english_score.csv', english_score, delimiter=',')

# comprehensive_score = np.random.normal(200, 30, 1000)
# np.savetxt('comprehensive_score.csv', comprehensive_score, delimiter=',')

# sum = score1 + score2 + score3
#
# plt.hist(sum, 100, density=True)
#
# plt.show()
#


def draw_graph(score):
    count, bins, ignored = plt.hist(score, 100, density=True)
    std = np.std(score)
    mean = np.mean(score)
    plt.plot(bins, 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (bins - mean) ** 2 / (2 * std ** 2)), linewidth=2,
             color='r')
    plt.show()


chinese_score = np.loadtxt('./chinese_score.csv', delimiter=',')
chinese_score = np.around(chinese_score, decimals=1)
draw_graph(chinese_score)

math_score = np.loadtxt('./math_score.csv', delimiter=',')
math_score = np.around(math_score, decimals=1)
draw_graph(math_score)

english_score = np.loadtxt('./english_score.csv', delimiter=',')
english_score = np.around(english_score, decimals=1)
draw_graph(english_score)

comprehensive_score = np.loadtxt('./comprehensive_score.csv', delimiter=',')
comprehensive_score = np.around(comprehensive_score, decimals=1)
draw_graph(comprehensive_score)

total_score = chinese_score + math_score + english_score + comprehensive_score
draw_graph(total_score)

tom_chinese_score = 123.5
tom_math_score = 98
tom_english_score = 107

