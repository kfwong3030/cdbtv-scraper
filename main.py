import requests
from bs4 import BeautifulSoup

def scrape_cdbtv():
    url = "https://cdbtv.com/32383607"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # 查找 iframe 中的直播源
    iframe_links = [iframe.get("src") for iframe in soup.find_all("iframe") if iframe.get("src")]
    print("找到的 iframe 链接：")
    for link in iframe_links:
        print(link)

    # 可扩展：查找 .m3u8 或其他直播源
    for script in soup.find_all("script"):
        if script.string and ".m3u8" in script.string:
            print("可能的直播源：", script.string)

if __name__ == "__main__":
    scrape_cdbtv()
