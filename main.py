from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 设置无头浏览器
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

# 打开页面
url = "https://cdbtv.com/32383607"
driver.get(url)

# 等待页面加载（延长时间）
time.sleep(10)

# 打印页面 HTML（调试用）
html = driver.page_source
with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)

# 查找 iframe
iframes = driver.find_elements(By.TAG_NAME, "iframe")
iframe_links = [iframe.get_attribute("src") for iframe in iframes if iframe.get_attribute("src")]

# 输出结果
print(f"✅ 找到 {len(iframe_links)} 个 iframe 链接")
for link in iframe_links:
    print(link)

# 保存到文件
with open("output.txt", "w", encoding="utf-8") as f:
    for link in iframe_links:
        f.write(link + "\n")

driver.quit()
