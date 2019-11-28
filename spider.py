import scrapy


class QuotesSpider(scrapy.Spider):
    name = "reviews"
    start_urls = [
        'https://domicilios.com/restaurantes/bogota/ppc-suba-menu?t=comentarios',
    ]

    def parse(self, response):
        for review in response.css("#reviewList > li"):
            yield {
                'text': review.css("[itemprop='description']::text").get(),
                'author': review.css("div.small").css('[itemprop="author"]::text').get(),
                'date': review.css("[itemprop='datePublished']::text").get(),
                'previous_orders': review.css("div.small::text")[1].get(),
                'previous_reviews': review.css("div.small::text")[2].get(),
                'worstRating': review.css("[itemprop='worstRating']::attr(content)").get(),
                'ratingValue': review.css("[itemprop='ratingValue']::attr(content)").get(),
                'bestRating': review.css("[itemprop='bestRating']::attr(content)").get()
            }

        # No es posible buscar un link para la siguiente página porque domicilios
        # está escrito en JavaScript, por lo que hay que interactuar con un navegador automatizado