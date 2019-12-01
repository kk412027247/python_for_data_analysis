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
    return
    count, bins, ignored = plt.hist(score, 70, density=True)
    std = np.std(score)
    mean = np.mean(score)
    plt.plot(bins, 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (bins - mean) ** 2 / (2 * std ** 2)), linewidth=2,
             color='r')
    plt.show()


def find_position(score, score_list):
    ranking_list = np.unique(score_list)
    for (index, value) in enumerate(np.sort(ranking_list)):
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

total_score_median = np.median(total_score)
# 中位数
print('total_score_median', total_score_median)
# 百分位数
print('percentile', np.percentile(total_score, 50))
# 方差
# 在概率论和统计学中，一个随机变量的方差描述的是它的离散程度，也就是该变量离其期望值的距离。
print('variance', np.var(total_score))
# 标注差
# 标准差（又称标准偏差、均方差，英语：Standard Deviation，缩写SD），数学符号σ（sigma），在概率统计中最常使用作为测量一组数值的离散程度之用。标准差定义：为方差开算术平方根，反映组内个体间的离散程度；标准差与期望值之比为标准离差率。
print('standard deviation', np.std(total_score))

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

# print(tom_chinese_score_position)
# print(tom_math_score_position)
# print(tom_english_score_position)
# print(tom_comprehensive_score_position)
# print(tom_tom_total_score)


# 标准分
# 标准分，是一种由原始分推导出来的相对地位量数，它是用来说明原始分在所属的那批分数中 的相对位置的。考生在接受测验后，按照评分标准对其作答反应直接评出来的分数，叫原始分。
