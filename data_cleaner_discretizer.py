# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# from subprocess import check_output
# print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.
input = pd.read_csv("train.csv")
print("SIZE: %d %d" % input.shape)

input.drop(["PassengerId"], axis=1)
input["New Gender"] = input["Gender"].apply()

# titles = {}

# for index,row in input.iterrows():
#     name = row["Name"]
#     last_name, rest_of_name = name.split(", ", 1)
#     title, first_names = rest_of_name.split(' ', 1)
#     if title not in titles:
#         titles[title] = 1
#     else:
#         titles[ title ] += 1

# for title, title_count in titles.items():
#     print("%s: %d" % (title, title_count))

