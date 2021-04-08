from django.db import models

# Create your models here.

import numpy as np
import itertools

g_girls = [
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

g_scores = np.array([
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

def score_mtx(idx):
    return np.array([[g_scores[y][x] for y in idx] for x in idx])

def avg_score(idx):
    return score_mtx(idx).sum() / len(idx) / len(idx)

# TODO 再帰
def to_girl_indices(names):
    return [g_girls.index(i) for i in names]

# TODO 再帰
def to_girl_names(idx):
    return [g_girls[i] for i in idx]

def _contains_list(a, b):
    return len(_not_in_list(a, b)) == 0

def _all_combinations(size):
    return itertools.combinations(range(len(g_scores)), size)

def _not_in_list(a, b):
    return [i for i in a if i not in b]

def combinations(idx = [], size = 4, score = 1.0):
    return [_not_in_list(c, idx) for c in _all_combinations(size) if _contains_list(idx, c) and avg_score(c) >= score]
