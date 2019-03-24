import numpy as np
from scipy import stats

# 仮説Aの母数
a_count = 10000
# 仮説Aの成果
a_conv = 400
# 仮説Bの母数
b_count = 90000
# 仮説Bの成果
b_conv = 3100
# カイ二乗検定を行う
data = np.array([[a_conv,a_count],[b_conv,b_count]])
chi2, p, dof, expected = stats.chi2_contingency(data)
# 結果が偶然である確率を出力
print("結果が偶然である確率 %.2f %%" % (p*100))
