import os
import json

assets_dir = './assets'
data = {}

# assets 폴더 안의 class101, class102 등의 폴더를 하나씩 확인
for class_name in os.listdir(assets_dir):
    class_path = os.path.join(assets_dir, class_name)
    
    if os.path.isdir(class_path):
        # 폴더 안에서 .pdf 로 끝나는 파일 이름만 싹 모으기
        files = [f for f in os.listdir(class_path) if f.endswith('.pdf')]
        data[class_name] = files

# 모은 데이터를 file_list.js 라는 파일로 저장
with open('file_list.js', 'w', encoding='utf-8') as f:
    f.write(f"const classFiles = {json.dumps(data, ensure_ascii=False, indent=2)};")