# 파이썬_DAY4

### 1. 함수

= 어떤 일을 수행하는 코드의 코드블록

- 자주 사용되는 명령(코드)들을 담고 있는 블럭주머니 : 프로그램의 재사용성

- 함수에 의해 처리되는 기능에 따라 데이터를 받을 수도 있고 수행 결과값을 리턴할 수 있다.

- 수행 결과값이 없는 경우에는 None(없음)이라는 리터럴이 리턴된다.

- 호출문으로 실행

  : **함수(아규먼트들)**

  - 매개변수 : 함수가 호출될 때, 데이터를 받아서 저장하는 변수

  - 아규먼트 : 함수가 호출될 때, 전달되는 데이터

    아큐먼트(r-value)-매개변수(l-value역할)는 한팀! (둘 다 인수)

    

#### 1.1 함수의 장점

- 필요할 때마다 호출 가능
- 논리적인 단위로 분할 가능
- 코드의 캡슐화



### 2. 함수 만드는 방법

def 함수명(매개변수):

​	수행문1

​	수행문2

​	return <반환값>

> ** 매개변수는 없어도 가능



### 3. 함수사용하는 방법

함수명()

함수값(값, 값)



### 인수

: 함수가 호출될 때 함수로 전달되는 데이터

- 함수의 동작에 변화를 주어 활용성을 높임

- 매개변수를 통해서 전달받음

  - **매개변수** : 함수 정의문의 인수 (ex. begin, end)

  - **아규먼트** : 함수 호출문에서 전달하는 인수 (ex. 3, 7)

``` python
def calrc(begin, end):
	sum = 0
	for num in range(begin, end+1):
        sum += num
    return sum

print('3 ~ 7 =', calrc(3,7))

>>> 3 ~ 7 = 25
```

![image-20210107134804026](C:\Users\MINHEE\AppData\Roaming\Typora\typora-user-images\image-20210107134804026.png)