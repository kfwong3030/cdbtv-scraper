from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 设置无头模式（适用于 GitHub Actions 或服务器环境）
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# 初始化 Chrome 浏览器
driver = webdriver.Chrome(options=options)

# 目标页面
url = "https://cdbtv.com/32383607"
driver.get(url)

# 等待页面加载（可根据页面复杂度调整时间）
time.sleep(3)

# 抓取所有 iframe 元素
iframes = driver.find_elements(By.TAG_NAME, "iframe")
iframe_links = [iframe.get_attribute("src") for iframe in iframes if iframe.get_attribute("src")]

# 输出到终端
print("找到的 iframe 链接：")
for link in iframe_links:
    print(link)

# 保存到 output.txt
with open("output.txt", "w", encoding="utf-8") as f:
    for link in iframe_links:
        f.write(link + "\n")

# 关闭浏览器
driver.quit()
