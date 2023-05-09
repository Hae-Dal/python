from selenium import webdriver
from bs4 import BeautifulSoup

# 웹 드라이버 설정
driver = webdriver.Chrome('//chromedriver')  # Chrome 웹 드라이버 경로 지정

# 웹 드라이버 실행
with driver:
    # 웹 페이지 로드
    driver.get('https://bbs.pdpop.com/board_re.php?code=F_02')

    count = 0

    'for i in range(1, 4906):'
    # 페이지 소스 가져오기
    page_source = driver.page_source

    # BeautifulSoup을 사용하여 데이터 추출
    soup = BeautifulSoup(page_source, 'html.parser')

    # 필요한 데이터 추출 작업 수행
    div = soup.find('div', class_="shlstcon")
    li = div.find_all('li')

    data_li = li[1:]
    count += len(data_li)

    print(count)
    # 필요한 경우 JavaScript 실행 및 페이지 상호작용 수행
    next_btn = driver.find_element('xpath', '//*[@id="Contents_Next"]/img')
    next_btn.click()

