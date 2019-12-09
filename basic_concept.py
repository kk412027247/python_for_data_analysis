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

def show_basic_value(score_list):
    mean = np.mean(score_list)
    total_score_median = np.median(score_list)
    percentile_25 = np.percentile(score_list, 25)
    percentile_75 = np.percentile(score_list, 75)
    variance = np.var(score_list)
    standard_deviation = np.std(score_list)

    # 平均数
    # 中位数
    # 百分位数
    # 方差
    # 在概率论和统计学中，一个随机变量的方差描述的是它的离散程度，也就是该变量离其期望值的距离。
    # 标注差
    # 标准差（又称标准偏差、均方差，英语：Standard Deviation，缩写SD），数学符号σ（sigma），在概率统计中最常使用作为测量一组数值的离散程度之用。
    # 标准差定义：为方差开算术平方根，反映组内个体间的离散程度；标准差与期望值之比为标准离差率。

    print('平均数:', mean, '中位数: ', total_score_median, ', 25%分位:', percentile_25, ', 75%分位:', percentile_75,
          ', 方差:', variance, ', 标准差:', standard_deviation, '\n')
    return percentile_25, total_score_median, percentile_75


def draw_graph(score_list, name):
    ranking_list = np.unique(score_list)
    ranking_list_length = len(ranking_list)
    count, bins, ignored = plt.hist(score_list, bins=ranking_list_length, density=True)
    x_label = 'range: ' + str(ranking_list[0]) + ' ~ ' + str(ranking_list[-1])
    print(name + '总体成绩范围:', x_label)
    plt.xlabel(x_label)
    plt.ylabel("proportion")
    std = np.std(score_list)
    mean = np.mean(score_list)
    # 25% 50% 75% percentile value
    percentile_25, total_score_median, percentile_75 = show_basic_value(score_list)
    plt.vlines(percentile_25, 0, np.exp(-(percentile_25 - mean) ** 2 / (2 * std ** 2)) / (np.sqrt(2 * np.pi) * std),
               colors="r", )
    plt.vlines(total_score_median, 0,
               np.exp(-(total_score_median - mean) ** 2 / (2 * std ** 2)) / (np.sqrt(2 * np.pi) * std), colors="r", )
    plt.vlines(percentile_75, 0, np.exp(-(percentile_75 - mean) ** 2 / (2 * std ** 2)) / (np.sqrt(2 * np.pi) * std),
               colors="r", )
    plt.plot(bins, 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (bins - mean) ** 2 / (2 * std ** 2)), linewidth=2,
             color='r')
    plt.show()


def show_person_score(score, score_list, name):
    fig_size = plt.gcf().get_size_inches()
    plt.gcf().set_size_inches(5 * fig_size)
    ranking_list = np.unique(np.append(score_list, score))
    position = np.where(ranking_list == score)[0][0]
    length = len(ranking_list)
    color = ['black' for _ in range(length)]
    color[position] = 'red'
    plt.barh(range(length), ranking_list, color=color)
    ticks = [x + 1 for x in np.flip(range(length))]
    ticks[position] = '-->' + str(length - position)
    plt.yticks(range(length), ticks)
    plt.show()
    _score_list = np.sort(np.append(score_list, score))
    percentile_position = np.where(_score_list >= score)[0][0]
    percentile = str(np.around(percentile_position / len(_score_list) * 100, 2))
    # Z = (X - X_bar) / S
    # 式中，X为原始分数，X_bar为原始分的平均数，S为原始分的标准差。
    mean = np.mean(score_list)
    standard_deviation = np.std(score_list)
    standard_score = (score - mean) / standard_deviation * 100 + 100

    print(name, score, '排名:', str(length - position), '超越了: ', percentile + '%', '标准分:', standard_score)


chinese_score = np.loadtxt('./chinese_score.csv', delimiter=',')
chinese_score = np.around(chinese_score, decimals=1)
draw_graph(chinese_score, '语文')

math_score = np.loadtxt('./math_score.csv', delimiter=',')
math_score = np.around(math_score, decimals=1)
draw_graph(math_score, '数学')

english_score = np.loadtxt('./english_score.csv', delimiter=',')
english_score = np.around(english_score, decimals=1)
draw_graph(english_score, '英语')

comprehensive_score = np.loadtxt('./comprehensive_score.csv', delimiter=',')
comprehensive_score = np.around(comprehensive_score, decimals=1)
draw_graph(comprehensive_score, '综合科')

total_score = chinese_score + math_score + english_score + comprehensive_score
draw_graph(total_score, '总分')

tom_chinese_score = 123
tom_math_score = 98
tom_english_score = 107
tom_comprehensive_score = 224
tom_total_score = tom_chinese_score + tom_math_score + tom_english_score + tom_comprehensive_score

show_person_score(tom_chinese_score, chinese_score, '陈小花的语文成绩:')
show_person_score(tom_math_score, math_score, '陈小花的数学成绩:')
show_person_score(tom_english_score, english_score, '陈小花的英语成绩:')
show_person_score(tom_comprehensive_score, comprehensive_score, '陈小花的综合科成绩:')
show_person_score(tom_total_score, total_score, '陈小花的总分成绩:')

# 标准分
# 标准分，是一种由原始分推导出来的相对地位量数，它是用来说明原始分在所属的那批分数中 的相对位置的。
# 考生在接受测验后，按照评分标准对其作答反应直接评出来的分数，叫原始分。


