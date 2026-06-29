import os
import json

# 현재 경로와 폴더 목록을 출력해서 로그에 남김
print(f"현재 실행 위치: {os.getcwd()}")
print(f"파일 목록: {os.listdir('.')}")

assets_dir = './assets'

# assets 폴더가 있는지 체크
if not os.path.exists(assets_dir):
    print(f"에러: {assets_dir} 폴더를 찾을 수 없습니다!")
else:
    data = {}
    print(f"assets 폴더 안의 내용: {os.listdir(assets_dir)}")
    
    # assets 폴더 안의 class101, class102 등의 폴더를 하나씩 확인
    for class_name in os.listdir(assets_dir):
        class_path = os.path.join(assets_dir, class_name)
        
        if os.path.isdir(class_path):
            # 폴더 안에서 .pdf 로 끝나는 파일 이름만 싹 모으기
            files = [f for f in os.listdir(class_path) if f.endswith('.pdf')]
            data[class_name] = files
            print(f"폴더 {class_name}에서 찾은 파일: {files}")

    # 모은 데이터를 file_list.js 라는 파일로 저장
    with open('file_list.js', 'w', encoding='utf-8') as f:
        f.write(f"const classFiles = {json.dumps(data, ensure_ascii=False, indent=2)};")
    print("file_list.js 생성 완료!")