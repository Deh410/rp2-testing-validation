import csv
from read_csv import Read_csv

class GitRepoSpider(scrapy.Spider):
    name = "Github"
    urls = Read_csv.repo_github()
    start_urls = []
    for url in urls:
        start_urls.append("https://github.com/" + url)

    def parse(self, response):
        f = open("results.txt","a+")
        for paragraph in response.css('div.Box-body p'):
            for a in paragraph.css('a'):
                title = a.css("::attr(href)").extract_first()
                travis = re.findall("travis", title)
                if(len(travis) > 0):
                    f.write(response.url.replace(',','') + " true\n")
                    time.sleep(2)
        f.close()