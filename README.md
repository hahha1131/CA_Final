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

* 선형 추세선

![추세선 지수 형태](https://postfiles.pstatic.net/MjAyMjA2MTBfMjkx/MDAxNjU0ODUwNzg4ODA2.IUikl2EXOmqf56oLaElfiJ8X02Da1dy8C_gfe12FEwwg.tEcBBAXpAqdLTxRmztRTuKSQURrab25QikmNmCUrwGQg.PNG.jinha081131/%EA%B7%B8%EB%9E%98%ED%94%84_%EC%A7%80%EC%88%98%ED%98%95_new.png?type=w966)

* 지수형 추세선

![둘의 비교](https://postfiles.pstatic.net/MjAyMjA2MTBfMjgw/MDAxNjU0ODUwNzk2MjQy._ZAKhr7W0hARF-TJtFXLFLatpj21VofXoNATOTs4Vg0g.LPcNQxEumYz726t5l1i0JfvxgzKG4JciVJMaBj26aSYg.PNG.jinha081131/%EA%B7%B8%EB%9E%98%ED%94%84_%EC%A7%80%EC%88%98%ED%98%95_%EC%84%A0%ED%98%95.png?type=w966)

* 그 둘의 비교


___

### 알고리즘
* 유전 알고리즘을 이용하여 최적화  
* 분산형 차트(꺾은 선 그래프, 말하자면 데이터값이 점으로 퍼져 있는 형태의 그래프)에서 회귀식은 추세선이라고도 볼 수 있음  
* 유전 알고리즘을 사용하기 전, 1차식이라는 가정하에 y(x) = ax + b의 형태로 식을 만듦(x = 개월, y = 음식배달 거래액)  
* 실제 측정된 기간에 따른 거래액의 변화와 추세선(회귀식)을 유전 알고리즘에 따라 그래프와 실제 값들과의 오차를 줄이면서 최종 최적화 그래프, 즉 앞으로의 거래액 변화도 추측할 수 있는 1차식 형태의 정확한 그래프를 구함  
* 따라서 선형 회귀 분석을 실시함

___

### 소스코드(linear regression code) 설명
* 동작방식
    - 임의의 (x, y) 2쌍(ex> x = 5 / y = 1,603,614 | x = 17 / y = 2,187,844)을 입력받아 그 둘을 기준으로 1차식 그래프의 a, b를 구함
    - 임의의 (x, y)를 입력받으면서 오차가 가장 작은 그래프를 도출
    - 오차가 가장 작은 그래프를 최종 그래프로 결정  
    - 돌연변이 확률 = 0.05~0.1% (실제 코드로 구현은 하지 못함)
        - 돌연변이: x와 y의 배열에서 값을 순차적으로 조사하다가 랜덤한 x 또는 y의 값을 배열에서 참고하는 것을 의미


* 함수 및 매개변수
    - 함수
        - y = ax + b  
        - 단순 선형 회귀식  

    - 매개변수
        - a, 모수 값(완벽에 가까운 추세선)의 기울기, b는 모수 값의 y절편  
        - x, 코로나 지속기간(단위: 개월)  
        - y, x(코로나 지속기간)에 따른 모바일과 PC를 포함한 온라인 음식배달 주문 거래액  


* 돌연변이 확률 높을 때 (20 ~ 30%로 발생) **{예상}**
    - 갑작스럽게 랜덤한 값으로 그래프를 그리면서 다양한 형태의 그래프가 나타남(a와 b의 값의 범위가 커짐)
    - 입력 값의 범위가 커져서 모수 값을 구하는 데에 시간이 조금 걸림
    - 예상대로 정확도가 조금 떨어짐  


* 돌연변이 확률 낮을 때 (0.005 ~ 0.01%로 발생) **{예상}**
    - 랜덤한 값으로 그래프가 나타나지 않아서 a, b 값의 범위가 작아졌음
    - 다양한 모습의 그래프가 나타나지 않음
    - 생각보다 정확도가 낮음

___

### 모수 값 추정
* 모수 값(최적화가 끝난 식)은 **f(x) = 44270x + 77086957(a = 44270 / b = 77086957)**
* 파이썬을 이용하여 분산형 차트와 차트를 가로지르는 모수 값(1차식) 시각화


     그래프 형태
![shape of graph](https://postfiles.pstatic.net/MjAyMjA2MTVfNjMg/MDAxNjU1MzAxMjMyMTEy.g8nzhOgJJUNlEg3_5nGh8gnB_4kwUYCFS8wqL3aU5sgg.THmGxN_wSBJ6AKyiQsbukxMz7GGboxliZPt60AwrYLAg.PNG.jinha081131/%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EC%BD%94%EB%93%9C%EB%A1%9C_%EC%8B%A4%ED%96%89%ED%95%9C_%EC%8B%A4%EC%A0%9C_%EB%AA%A8%EC%88%98_%EA%B0%92_%EA%B7%B8%EB%9E%98%ED%94%84.png?type=w966)


* 추세선과 비교했을 때나 전체적인 그래프의 형태와 비교했을 때 거의 유사한 모습을 보임
* 엑셀에서 나타난 그래프에서 추세선에 가장 가까운 두 지점을 기준으로 식을 구했을 때, 위의 식과 유사한 식이 구해짐

___

### 최적화 과정
* 이 부분은 다른 코드로 선형 회귀를 수행하면서 기울기가 정확한 값으로 맞춰지는 과정을 설명
* 코드를 실행하는 횟수가 많아질수록 실제 데이터와 모수 값(1차 회귀식) 사이의 오차는 분산형 데이터셋에서 가장 평균에 가까운 두 쌍에 근접하는 형태와 유사하게 줄어들었음
* 더 많은 실행횟수로 실행했으나 특정 횟수 이후로는 오차가 더 줄어들지 않았음(따라서 위에서 구한 모수 값이 가장 최적화된 값임)  

___

### 참고 사이트
* 국가 통계 포털  


<https://kosis.kr/index/index.do>  
  
  
* 온라인 음식배달 거래액  


<https://kosis.kr/statHtml/statHtml.do?orgId=164&tblId=DT_002&vw_cd=MT_ZTITLE&list_id=N1_13&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE>  
  
  
* 회귀 분석 관련 사이트  


<https://nevertrustbrutus.tistory.com/426>  
  
  
<https://creatorjo.tistory.com/135>  

  
  
<https://velog.io/@amobmocmo/Python-%EB%8B%A8%EC%88%9C-%EC%84%A0%ED%98%95-%ED%9A%8C%EA%B7%80-Linear-Regression-%EA%B5%AC%ED%98%84-9ik2uej68q>  

  
