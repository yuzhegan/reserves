import feapder
from curl_cffi import requests


class AirSpiderTest(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://www.baidu.com")

    def download_midware(self, request):
        response = requests.get(request.url, impersonate="chrome110")
        return request, response

    def parse(self, request, response):
        print(response.text)


if __name__ == "__main__":
    AirSpiderTest().start()
