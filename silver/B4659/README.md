## 비밀번호 발음하기

|시간 제한|메모리 제한|제출|정답|맞힌 사람|정답 비율|
|---|---|---|---|---|---|
|1 초|128 MB|---|---|---|---|

---

### 문제
좋은 패스워드는 다음의 조건을 만족해야 한다.

1. 모음(a, e, i, o, u) 중 하나를 반드시 포함하여야 한다.
2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

입력으로 제시되는 단어가 위의 조건을 모두 만족하는지 아닌지를 판단하는 프로그램을 작성하시오.

---

### 입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 마지막 테스트 케이스는 "end"이다. 각 테스트 케이스는 길이가 20 이하인 알파벳 소문자로만 이루어져 있다.

---

### 출력
각 테스트 케이스에 대해, 테스트 케이스의 단어를 포함하여 다음과 같이 출력한다.

- <test-case> is acceptable. 또는
- <test-case> is not acceptable.

---

### 예제 입력 1
~~~plaintext
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end
~~~

### 예제 출력 1
~~~plaintext
<a> is acceptable.
<tv> is not acceptable.
<ptoui> is not acceptable.
<bontres> is not acceptable.
<zoggax> is not acceptable.
<wiinq> is not acceptable.
<eep> is acceptable.
<houctuh> is acceptable.
~~~

---

### 풀이 생각

---

### 다른 풀이
