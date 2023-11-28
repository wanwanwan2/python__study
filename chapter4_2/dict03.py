# 딕셔너리에 요소 제거하기

# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

# 요소 추가 전에 내용을 출력해 봅니다.
print("요소 추가 이전:", dictionary)

# 딕셔너리에 요소를 제거합니다.
del dictionary["name"]
del dictionary["type"]

# 출력합니다.
print("요소 제거 이후:", dictionary)
