# From : https://thecleverprogrammer.com/2020/11/28/youtube-trending-videos-analysis-with-python/
import time

import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

import warnings
from collections import Counter
import datetime
import wordcloud
import json

df = pd.read_csv("youtube_trending_videos_analysis/data/USvideos.csv")
PLOT_COLORS = ["#268bd2", "#0052CC", "#FF5722", "#b58900", "#003f5c"]
# pd.options.display.float_format = '{:.2f}'.format
# sns.set(style="ticks")
plt.rc('figure', figsize=(8, 5), dpi=100)
# plt.rc('axes', labelpad=20, facecolor="#ffffff", linewidth=0.4, grid=True, labelsize=14)
# plt.rc('patch', linewidth=0)
# plt.rc('xtick.major', width=0.2)
# plt.rc('ytick.major', width=0.2)
# plt.rc('grid', color='#9E9E9E', linewidth=0.4)
plt.rc('font', family='Arial', weight='400', size=10)
plt.rc('text', color='#282828')
plt.rc('savefig', pad_inches=0.3, dpi=300)
df["description"] = df["description"].fillna(value="")
print(df.describe())
print(df[["likes", "views"]])
# plt.plot(df=df[["likes","views"]])
# df["view_to_like_%"] = df[["likes", "views"]].apply(lambda x, y: x/y,axis=1)
df["view_to_like"] = (df["likes"] / df["views"]) * 100
df['view_to_like'] = df['view_to_like'].map('{:.2f}%'.format)
df["view_to_dislike"] = (df["dislikes"] / df["views"]) * 100
df['view_to_dislike'] = df['view_to_dislike'].map('{:.2f}%'.format)
df["description_length"] = df['description'].apply(lambda x: len(x))
df = df[df["comments_disabled"] == True]
print(df[["likes", "dislikes", "views", "view_to_like", "view_to_dislike", "comments_disabled"]])
print(df[["likes", "description_length"]].describe())
# plt.show()


# def contains_capitalized_word(s):
#     for w in s.split():
#         if w.isupper():
#             return True
#     return False


# df["contains_capitalized"] = df["title"].apply(contains_capitalized_word)
#
# value_counts = df["contains_capitalized"].value_counts().to_dict()
# print(value_counts)
# fig, ax = plt.subplots()
# _ = ax.pie([value_counts[False], value_counts[True]], labels=['No', 'Yes'],
#            colors=['#003f5c', '#ffa600'], textprops={'color': '#040204'}, startangle=45)
# _ = ax.axis('equal')
# _ = ax.set_title('Title Contains Capitalized Word?')
#
# df["title_length"] = df["title"].apply(lambda x: len(x))

# fig, ax = plt.subplots()
# _ = sns.distplot(df["title_length"], kde=False, rug=False,
#                  color=PLOT_COLORS[4], hist_kws={'alpha': 1}, ax=ax)
# _ = ax.set(xlabel="Title Length", ylabel="No. of videos", xticks=range(0, 110, 10))
#
# fig, ax = plt.subplots()
# _ = ax.scatter(x=df['views'], y=df['title_length'], color=PLOT_COLORS[2], edgecolors="#000000", linewidths=0.5)
# _ = ax.set(xlabel="Views", ylabel="Title Length")
#
# title_words = list(df["title"].apply(lambda x: x.split()))
# title_words = [x for y in title_words for x in y]
# wc = wordcloud.WordCloud(width=1200, height=500,
#                          collocations=False, background_color="white",
#                          colormap="tab20b").generate(" ".join(title_words))
# plt.figure(figsize=(15,10))
# plt.imshow(wc, interpolation='bilinear')
# _ = plt.axis("off")

# h_labels = [x.replace('_', ' ').title() for x in
#             df.select_dtypes(include=['number', 'bool']).columns.to_list()]
#
# fig, ax = plt.subplots(figsize=(10,7))
# _ = sns.heatmap(df[df.select_dtypes(include=['number', 'bool']).columns.to_list()].corr(), annot=True, xticklabels=h_labels, yticklabels=h_labels, cmap=sns.cubehelix_palette(as_cmap=True), ax=ax)
#
# # plt.show()
# fn = "heat_map_"+time.strftime("%Y_%m_%d_%H_%M_%S")+".png"
# print(fn)
# plt.savefig(fn)
