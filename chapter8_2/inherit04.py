# 자식 클래스로써 부모의 함수 재정의(오버라이드)하기
class CustomException(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message = message
        self.value = value 
    
    def __str__(self):
        return self.message

    def print(self):
        print("##### 오류 정보 #####")
        print("메시지:", self.message)
        print("값:", self.value)

# 예외를 발생시켜봅시다.
try:
    raise CustomException("딱히 이유없음", 273)
except CustomException as e:
    e.print()