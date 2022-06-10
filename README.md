# 회귀식 추정
___

## 주제
* 2020년 5월 ~ 2022년 4월까지 코로나가 지속되는 기간에 따른 온라인(PC, 모바일) 음식배달 거래액 변화  

___

### 예상
* 2020~2022까지는 코로나의 대유행으로 자가격리 인구수 증가와 2022년도에 가까워질수록 상승하는 배달팁(배달비용)에 따라서 그래프의 값이 지속적인 상승보다는 하락과 상승을 반복할 것으로 예상  
* 위의 예상에 따라 일반식(수학적 모형: 회귀식)을 구할 때, 식의 형태에 가장 크게 영향을 끼치는 구간은 2021년말~2022년 구간으로 예상  

___

### 데이터셋 확보와 엑셀을 이용한 그래프 생성
* 데이터셋
    - 2020년 5월부터 2022년 4월까지의 온라인 음식배달 거래액  
    - 통계청에서 해당 데이터셋 확보 가능(출처는 readme.md 가장 마지막 부분에 표기)  
* 그래프
    - 엑셀을 활용  
    - 한 가지 문제점은 데이터를 분산형 차트로 변경했을 때, 차트의 x축이 알 수 없는 임의의 값으로 변경되어 분산형과 가장 유사한 꺾은선형으로 제작할 수 밖에 없었음  
___

### 회귀식  
* 엑셀의 차트 기능에 따르면 추세선이라고 하는 임의의 그래프를 확인할 수 있음
* 여러 형태의 추세선을 확인했을 때 선형 추세선이 가장 적합하게 보임
* 지수 형태의 추세선도 적합해 보였으나, 그래프의 끝으로 갈수록 추세선과 실제 그래프의 오차가 미묘하게 커졌음
* 따라서 선형(1차식)으로 선택


![추세선 1차식](https://postfiles.pstatic.net/MjAyMjA2MTBfMjcz/MDAxNjU0ODUwNzg2MDI0._B8trKNL31SCYPCARQ2xJcCzsfgzAJiclEU6diTF5qog.97Wzkd76A5eeUJPXAGfi59O-bVJ205_XQ14AQtsDuY8g.PNG.jinha081131/%EA%B7%B8%EB%9E%98%ED%94%84_new.png?type=w966)

![추세선 지수 형태](https://postfiles.pstatic.net/MjAyMjA2MTBfMjkx/MDAxNjU0ODUwNzg4ODA2.IUikl2EXOmqf56oLaElfiJ8X02Da1dy8C_gfe12FEwwg.tEcBBAXpAqdLTxRmztRTuKSQURrab25QikmNmCUrwGQg.PNG.jinha081131/%EA%B7%B8%EB%9E%98%ED%94%84_%EC%A7%80%EC%88%98%ED%98%95_new.png?type=w966)

![둘의 비교](https://postfiles.pstatic.net/MjAyMjA2MTBfMjgw/MDAxNjU0ODUwNzk2MjQy._ZAKhr7W0hARF-TJtFXLFLatpj21VofXoNATOTs4Vg0g.LPcNQxEumYz726t5l1i0JfvxgzKG4JciVJMaBj26aSYg.PNG.jinha081131/%EA%B7%B8%EB%9E%98%ED%94%84_%EC%A7%80%EC%88%98%ED%98%95_%EC%84%A0%ED%98%95.png?type=w966)

___

### 알고리즘
* 유전 알고리즘을 이용하여 최적화  
* 유전 알고리즘을 사용하기 전, 1차식이라는 가정하에 y(x) = ax + b의 형태로 식을 하나 만듦(x = 개월, y = 음식배달 거래액)  
* 실제 측정된 기간에 따른 거래액의 변화와 추세선(회귀식)을 유전 알고리즘에 따라 그래프와 실제 값들과의 오차를 줄이면서 최종 최적화 그래프, 즉 앞으로의 거래액 변화도 추측할 수 있는 1차식 형태의 정확한 그래프를 구함

___

### 소스코드 설명
* 동작방식
    - 1
    - 2
    - 3  
* 함수 및 매개변수
    - 1
    - 2
    - 3

___

### 모수 값 추정
* 모수 값은 이다
* 추세선과 비교했을 때나 전체적인 그래프의 형태와 비교했을 때 거의 유사한 모습을 보임

___

### 최적화 과정
* 코드를 실행하는 횟수가 많아질수록 오차는 ~하는 형태로 줄어들었음
* 더 많은 실행횟수로 실행했으나 특정 횟수 이후로는 오차가 줄어들지 않았음(따라서 위에서 구한 모수 값이 가장 최적화된 값임)

