# 파일이 제대로 닫혔는지 확인하기

# try except 구문을 사용합니다.
try:
    # 파일을 엽니다.
    file = open("info.txt","w")
    # 여러가지 처리를 수행합니다.
    # 파일을 닫습니다.
    file.close()
except:
    print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)