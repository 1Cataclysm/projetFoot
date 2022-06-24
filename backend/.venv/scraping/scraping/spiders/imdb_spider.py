import scrapy
import os


class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    allowed_domains = ['footmercato.net']
    #allowed_domains = ['imdb.com']
    start_urls = ["https://www.footmercato.net/joueur/kylian-mbappe/statistique-but?season=2021&club=psg&competitionType=championship&competition=8879186764835452557&position="]

    def parse(self, response):
        print ("ouioui")
        scores = response.xpath("//div[@class='stats']//tbody//tr")
        #movies = response.xpath("//div[@class='lister-item-content']")
        print (scores)
        print ("ouioui")
        for score in scores:
            equipe_name = score.xpath(".//td[@class='stats__title']//a//text()").get()
            player_time_score = score.xpath(".//td[@class='stats__time']//text()").get()
            #movie_name = movie.xpath(".//h3//a//text()").get()
            #movie_link = "https://www.imdb.com" + movie.xpath(".//h3//a//@href").get()
            #movie_rating = movie.xpath(".//div[@class='ratings-bar']//strong//text()").get()

            yield{
                    'match':equipe_name,
                    'time_score':player_time_score
                    #'movie link':movie_link,
                    #'movie_rating':movie_rating
                  }

        #os.system('scrapy crawl imdb_spider -o imdb_mbappe2.csv')

        #https://www.footmercato.net/joueur/kylian-mbappe/statistique-but?season=2021&club=psg&competitionType=championship&competition=8879186764835452557&position=