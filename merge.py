import PyPDF2

def interleave_pdfs(file1_path, file2_path, output_path):
    # PDF 파일 열기
    pdf1 = PyPDF2.PdfReader(file1_path)
    pdf2 = PyPDF2.PdfReader(file2_path)
    
    writer = PyPDF2.PdfWriter()
    
    # 두 파일 중 더 많은 페이지 수를 기준으로 반복
    max_pages = max(len(pdf1.pages), len(pdf2.pages))
    
    for i in range(max_pages):
        # 첫 번째 파일(본문)에서 한 페이지 추가 -> 홀수 쪽
        if i < len(pdf1.pages):
            writer.add_page(pdf1.pages[i])
        
        # 두 번째 파일(해설)에서 한 페이지 추가 -> 짝수 쪽
        if i < len(pdf2.pages):
            writer.add_page(pdf2.pages[i])
            
    # 결과 저장
    with open(output_path, "wb") as output_file:
        writer.write(output_file)
        
    print(f"성공적으로 교차 병합되어 '{output_path}'로 저장되었습니다.")

# 파일 경로 설정 (실제 파일명이 다를 경우 수정해서 사용하세요)
input_body = "유찬 본문.pdf"
input_commentary = "유찬 해설.pdf"
output_result = "유찬_교차_편집_완료.pdf"

# 함수 실행
interleave_pdfs(input_body, input_commentary, output_result)
