|시간 제한|메모리 제한|제출|정답|맞힌 사람|정답 비율|
|---|---|---|---|---|---|
|2 초 (추가 시간 없음)|128 MB|138861|72229|56152|50.933%|


### 문제
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

### 입력
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

### 출력
첫째 줄에 남게 되는 카드의 번호를 출력한다.

### 예제 입력 1 
```
6
```
### 예제 출력 1 
```
4
```

---
### 풀이 생각
패턴을 분석   
N이 짝수일 경우 홀수 자리 수를 제거하는 과정을 반복
N이 홀수일 경우 홀수 자리 수를 한 번 제거한 뒤 맨 앞의 수를 뒤로 이동시킨 다음, 짝수일 경우와 동일하게 홀수 자리 수를 제거하는 과정을 반복

#### 잘못생각한 부분
재귀로 풀고자 했는데 재귀 방식을 이용하게 되면 매 함수 호출마다 deque을 생성하게 되어 N의 수가 커질 경우 공간복잡도 측면에서 좋지 못함, 
또한 로직의 허점이 있지만 아직 밝혀내진 못하였고 로직의 시간복잡도 측면에서도 O(NlogN)으로 deque만 이용했을 때 보다 떨어지는 성능을 보임    

---
### 다른풀이
deque을 이용하는 방법   
단순히 deque 자료형을 이용하여 맨앞의 수를 한번 popleft하고 그 다음수는 popleft한 뒤 append로 붙이는 방식이다.  
시간복잡도는 O(N)이다.
이유는 deque자료형에서 popleft와 append의 시간 복잡도는 O(1)이기 때문이다.

---
### 또다른풀이
2의 거듭제곱의 패턴     
문제의 패턴을 살펴보면 N이 2의 거듭제곱일때 남는 카드는 항상 N이 되는 패턴이 있다.  
만약 N이 2의 거듭제곱이 아닐 경우엔 가장 가까운 거듭제곱을 N에서 뺀 값에 2를 곱한 값이 남은 카드의 숫자가 되는 패턴이 있다.     
이 풀이의 시간 복잡도는 O(logN)이다.    
이유는 N의 거듭제곱을 찾는 과정이 logN이고  
남은 계산은 1이기 때문이다.