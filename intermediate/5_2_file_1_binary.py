# 바이너리 파일 쓰기
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03')

# 바이너리 파일 읽기
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)