import numpy as np
import matplotlib.pyplot as plt
# 배열 처리와 데이터 구조 및 수치 계산을 위한 numpy와 그래프를 나타내기 위한 matplotlib


# 배열 x, 코로나 지속 기간 / 배열 y, 월별 모바일과 PC에서의 온라인 음식배달 거래액
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
y = np.array([1320798, 1253440, 1378600, 1676687, 1603614, 1546338, 1642625, 2197375, 2030620, 1824078, 1965974, 1975909, 2140672, 1971954, 2377984, 2418806, 2187844, 2263884, 2071141, 2449469, 2388571, 2244240, 2380695, 2089205])

# 정식명칭은 scikit-learn, python의 머신러닝 라이브러리 / 이번 회귀 분석을 통한 모수 값 추정에 가장 중요한 사항
from sklearn import linear_model
regr = linear_model.LinearRegression()
# 선형 회귀

regr.fit(x.reshape(24,1),y)
# regr, 선형 회귀분석 수행 객체 / fit을 통해 회귀분석 / reshape, 회귀분석에서 x는 하나 이상의 변수 가정하기 때문에 배열의 모양을 세로로 바꿔주는 역할(reshape을 하지 않으면 오류 발생)

plt.ylim(0,3000000)
plt.xlim(0,25)
# 각각 x축과 y축을 어느 값까지 표현할지 결정(x축은 25까지, y축은 3000000까지)

plt.plot(x,y,'o')
# 점으로 데이터 표현

plt.plot(x, x * regr.coef_ + regr.intercept_)
# intercept는 상수항, 즉 회귀식 ax + b에서 b의 값을 출력 / coef는 계수를 뜻함

print(regr.coef_)
# 상관계수 출력


plt.show()
