# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from scrapy.spiders import Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from .parser import parse_record


# Module API

class Spider(CrawlSpider):

    # Public

    name = 'pfizer'
    allowed_domains = ['pfizer.com']

    def __init__(self, conf=None, conn=None):

        # Save conf/conn
        self.conf = conf
        self.conn = conn

        # Make urls
        self.start_urls = [
            'http://www.pfizer.com/research/clinical_trials/find_a_trial?recr=0',
        ]

        # Make rules
        self.rules = [
            Rule(LinkExtractor(
                allow=r'find_a_trial/NCT\d+',
            ), callback=parse_record),
            Rule(LinkExtractor(
                allow=r'page=\d+',
            )),
        ]

        # Inherit parent
        super(Spider, self).__init__()
