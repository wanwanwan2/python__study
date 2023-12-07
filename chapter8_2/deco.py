# 데코레이터를 사용해 게터와 세터 만들기

# 모듈을 가져옵니다.
import math

# 클래스를 선언합니다.
class Circle:
    # ...생략...
    def __init__(self, radius):
        self.__radius = radius
    # 게터와 세터를 선언합니다.
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

# 원의 둘레와 넓이를 구합니다.
print(" 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름: ", circle.radius)
circle.radius = 2
print("변경된 원의 반지름: ", circle.radius)
print()

# 강제로 예외를 발생시킵니다.
print("# 강제로 예외를 발생시킵니다.")
circle.radius = -10