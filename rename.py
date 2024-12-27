import os
from datetime import datetime

def rename_files(folder_path):

    # 지정한 폴더 안에 있는 모든 파일의 목록을 가져와서 files라는 변수에 저장
    files = os.listdir(folder_path)

    # 이미지 파일의 확장자들을 모아놓은 목록
    image_extensions = ('jpg', 'jpeg', 'png', 'gif')

    # 현재 날짜를 'YYYYMMDD' 형식 (20241227)
    date_str = datetime.now().strftime('%Y%m%d')


    count = 1

    # 폴더 안의 파일들을 하나씩 확인
    for file in files:

        # 파일이 이미지 파일인지 확인
        # .lower()는 파일 이름을 소문자로 바꿔서 확인
        # .endswith()는 파일 이름이 지정된 확장자로 끝나는지 확인
        if file.lower().endswith(image_extensions):

            # 현재 파일의 확장자 ( jpg )
            ext = os.path.splitext(file)[1]

            # 새로운 파일 이름
            # {count:02d}는 숫자를 두 자리로 (예: 1 → 01)
            new_filename = f"부산사직동맛집_더밀_the_meal_{date_str}_{count:02d}{ext}"

            # old_file: 현재 파일의 전체 경로
            # new_file: 새 파일 이름의 전체 경로
            # os.path.join()는 폴더 경로와 파일 이름을 올바르게 합쳐줌
            old_file = os.path.join(folder_path, file)
            new_file = os.path.join(folder_path, new_filename)

            # 실제로 파일의 이름을 변경
            os.rename(old_file, new_file)
            print(f"변경완료: {file} -> {new_filename}")

            # 다음 파일을 위해 번호를 1 증가
            count += 1


# 실제 사용할 폴더 경로를 지정하고
# rename_files 함수를 실행
folder_path = r"C:\Users\arott\Downloads\themill"
rename_files(folder_path)