# 숫자로 변환되는 것들만 리스트에 넣기

# 변수를 선언합니다.
list_input_a = ["52", "273", "32", "스파이", "103"]

# 반복을 적용합니다.
list_number = []
for item in list_input_a:
    # 숫자로 변환해서 리스트에 추가합니다.
    try:
        float(item) # 예외가 발생함녀 알아서 다음으로 진행은 안 되겠지?
        list_number.append(item)
    except:
        pass

# 출력합니다.
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))