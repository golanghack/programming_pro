from django.contrib.sitemaps import Sitemap
from main.models import News, Rubric

class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.all()

    

class RubricSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Rubric.objects.all()





    