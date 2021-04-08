import numpy as np
import itertools

g_names = [
    'アグネスタキオン',
    'ウイニングチケット',
    'ウォッカ',
    'エアグルーブ',
    'エルコンドルパサー',
    'オグリキャップ',
    'キングヘイロー',
    'グラスワンダー',
    'ゴールドシップ',
    'サイレンススズカ',
    'サクラバクシンオー',
    'シンボリルドルフ',
    'スーパークリーク',
    'スペシャルウィーク',
    'タイキシャトル',
    'ダイワスカーレット',
    'トウカイテイオー',
    'ナイスネイチャ',
    'ハルウララ',
    'マチカネフクキタル',
    'マヤノトップガン',
    'マルゼンスキー',
    'メジロマックイーン',
    'メジロライアン',
    'ライスシャワー',
]

g_likes = np.array([
    [1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,1,1,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,1,1,0,1,1,0],
    [1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0],
    [1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,0,0,1,0,0,1,0,1],
    [0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,1],
    [1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1],
    [1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1],
    [0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,1],
    [1,1,1,1,1,0,0,0,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1],
    [1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1],
    [1,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,1],
    [1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,1,0,0,0,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0],
    [1,1,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0],
    [1,0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1],
])

def like_mtx(idx):
    return np.array([[g_likes[y][x] for y in idx] for x in idx])

def like_sum(idx):
    return like_mtx(idx).sum() / len(idx) / len(idx)

def to_indices(names):
    return [g_names.index(i) for i in names]

def to_names(idx):
    return [g_names[i] for i in idx]

def contains(idx, c):
    return len([i for i in idx if i not in c]) == 0

def combinations(n):
    return itertools.combinations(range(len(g_likes)), n)

def listup(names = [], num = 4, score = 1.0):
    idx = to_indices(names)
    return np.array([to_names([i for i in c if i not in idx]) for c in combinations(num) if contains(idx, c) and like_sum(c) >= score])

print(listup(['メジロマックイーン', 'シンボリルドルフ', 'トウカイテイオー'], 4, 1.0))
print(listup().shape)

# import scipy as sp
# import matplotlib.pyplot as plt
# import math
# from sklearn.decomposition import PCA
# from sklearn.cluster import KMeans

# def deep_likes(i, n):
#     return [(np.array(deep_likes(data[k], n-1))*i*v).sum() for k,v in enumerate(i)] if n > 0 else i

# data = np.array([deep_likes(i,2) for i in data])
# data = data/data.max()
# data = {i: {names[k]: v for k,v in enumerate(data[names.index(i)])} for i in names}

# data = PCA(n_components=1).fit_transform(data)
# km = KMeans(4)
# km.fit_transform(data)
# data = {i: [] for i in km.labels_}
# for k,v in enumerate(km.labels_):
#     data[v] += [names[k]]

# tier表
# 脚質、距離、場適
# 相性ループ同士の近似性
