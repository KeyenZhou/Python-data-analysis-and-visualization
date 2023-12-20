import os
import pandas as pd

file = os.getcwd() + r'/File/tips.csv'

tips = pd.read_csv(file)

# tips['total_bill'] = tips['total_bill'].apply(lambda x: float(f'{x:.2f}'))
# tips['tip'] = tips['tip'].apply(lambda x: float(f'{x:.2f}'))

s = input()

if s == 'gender':
    ans = tips['tip'].groupby(by=tips['gender']).agg(['mean'])
    # print(ans)
    print(f'男性顾客平均小费为：{ans.loc["Male", "mean"]:.2f}')
    print(f'女性顾客平均小费为：{ans.loc["Female", "mean"]:.2f}')
elif s == 'day':
    ans = tips['tip'].groupby(by=tips['day']).agg(['mean'])
    # print(ans)
    ans.sort_values(by='mean', inplace=True)
    for index in ans.index:
        print(f'{index}：{ans.loc[index, "mean"]:.2f}')
elif s == 'time':
    mapping = {
        'total_bill': ['sum', 'mean'],
        'tip': 'mean'
    }
    ans_grouped = tips.groupby(by='time')
    ans = ans_grouped.agg(mapping)
    # print(ans.columns)
    ans_dict = ans_grouped.groups
    print(
        f'午餐时间共{len(ans_dict["Lunch"])}条记录，共消费{ans.loc["Lunch", ("total_bill", "sum")]:.2f}，平均每单消费{ans.loc["Lunch", ("total_bill", "mean")]:.2f}，平均小费{ans.loc["Lunch", ("tip", "mean")]:.2f}')
    print(
        f'晚餐时间共{len(ans_dict["Dinner"])}条记录，共消费{ans.loc["Dinner", ("total_bill", "sum")]:.2f}，平均每单消费{ans.loc["Dinner", ("total_bill", "mean")]:.2f}，平均小费{ans.loc["Dinner", ("tip", "mean")]:.2f}')
elif s == 'smoker':
    gender = input()
    ans = tips.loc[
        (tips.loc[:, 'gender'] == gender) & (tips.loc[:, 'total_bill'] > 30) & (tips.loc[:, 'smoker'] == 'Yes')]
    for line in ans.values.tolist():
        line[0] = f'{line[0]:.2f}'
        line[1] = f'{line[1]:.2f}'
        print(line)
elif s == 'average':
    n = int(input())
    average = tips.loc[:, 'total_bill'] / tips.loc[:, 'size']
    tips.loc[:, 'average'] = average
    ans = tips.sort_values(by='average', ascending=False)
    for line in ans.head(n).values.tolist():
        line[0] = f'{line[0]:.2f}'
        line[1] = f'{line[1]:.2f}'
        print(line[:-1])
else:
    print('无数据')
