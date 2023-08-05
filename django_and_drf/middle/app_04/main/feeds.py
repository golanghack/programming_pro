import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatechars_html
from django.urls import reverse_lazy
from main.models import News

class LatestNewsFeed(Feed):
    title = 'News'
    link = reverse_lazy('main:index')
    description = 'Latest news'

    def items(self):
        return News.objects.filter(is_active=True)[:5]
    
    def item_title(self, item: str):
        return item.title

    def item_description(self, item: str):
        return truncatechars_html(markdown.markdown(item.content), 30)

    def item_pubdate(self, item: str):
        return item.created_at