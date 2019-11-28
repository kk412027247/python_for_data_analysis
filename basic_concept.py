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


# score11 = np.around(score1, decimals=0)
#
# chinese_score = np.random.normal(90, 15, 1000)
# chinese_score = np.around(chinese_score, decimals=0)
# np.savetxt('chinese_score.csv', chinese_score, delimiter=',')
#
# math_score = np.random.normal(80, 20, 1000)
# math_score = np.around(math_score, decimals=0)
# np.savetxt('math_score.csv', math_score, delimiter=',')
#
# english_score = np.random.normal(85, 17, 1000)
# english_score = np.around(english_score, decimals=0)
# np.savetxt('english_score.csv', english_score, delimiter=',')
#
# comprehensive_score = np.random.normal(200, 30, 1000)
# comprehensive_score = np.around(comprehensive_score, decimals=0)
# np.savetxt('comprehensive_score.csv', comprehensive_score, delimiter=',')

# sum = score1 + score2 + score3
#
# plt.hist(sum, 100, density=True)
#
# plt.show()
#
#

def draw_graph(score):
    count, bins, ignored = plt.hist(score, 70, density=True)
    std = np.std(score)
    mean = np.mean(score)
    plt.plot(bins, 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (bins - mean) ** 2 / (2 * std ** 2)), linewidth=2,
             color='r')
    plt.show()


def find_position(score, score_list):
    for (index, value) in enumerate(np.sort(score_list)):
        if value > score:
            return index - 1


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

tom_chinese_score = 123
tom_math_score = 98
tom_english_score = 107
tom_comprehensive_score = 224
tom_total_score = tom_chinese_score + tom_math_score + tom_english_score + tom_comprehensive_score

tom_chinese_score_position = find_position(tom_chinese_score, chinese_score)
tom_math_score_position = find_position(tom_math_score, math_score)
tom_english_score_position = find_position(tom_english_score, english_score)
tom_comprehensive_score_position = find_position(tom_comprehensive_score, comprehensive_score)
tom_tom_total_score = find_position(tom_total_score, total_score)

print(tom_chinese_score_position)
print(tom_math_score_position)
print(tom_english_score_position)
print(tom_comprehensive_score_position)
print(tom_tom_total_score)

