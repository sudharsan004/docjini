from django.contrib import sitemaps
from django.urls import reverse
from django.contrib.sites.models import Site


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'how-to', 'contact','terms',
        'privacy']

    def location(self, item):
        return reverse(item)
    
    def get_urls(self, site=None, **kwargs):
        site = Site(domain='docjini.com', name='docjini.com')
        return super(StaticViewSitemap, self).get_urls(site=site, **kwargs)
