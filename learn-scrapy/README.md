# Skills Learned
Scrapy 
Mongodb (default port:  271017)

Learn Scrapy Tutorial
1. Creating a new Scrapy project.
2. Writing a spider to crawl a site and extract data.
3. Exporting the scraped data using the command line.
4. Changing spider to recursively follow links.
5. Using spider arguments.

Create Scrapy Project: `scrapy startproject tutorial`
Run Scrapy program: `scrapy crawl quotes`
Run and write output to a json: `scrapy crawl quotes -o quotes.json`
Run Scrapy on shell: `scrapy shell 'http://quotes.toscrape.com`
In shell, scraping with selectors:
  Basic example
  CSS
  >>> response.css("title::text").extract_first()
  >>> response.css("title::text").extract()[0]
  >>> response.css("title::text").get()
  XPATH
  >>> response.xpath("//title/text()").extract_first()
  >>> response.xpath("//title/text()").extract()[0]
  >>> response.xpath("//title/text()").get()

  Example with class tags
  CSS 
  >>> response.css("span.text::text").extract_first()
  >>> response.css("span.text::text").extract()[0]
  >>> response.css("span.text::text").get()
  XPATH
  >>> response.xpath("//span[@class='text']/text()").extract_first()
  >>> response.xpath("//span[@class='text']/text()").extract()[0]
  >>> response.xpath("//span[@class='text']/text()").get()

  Example with href attribute
  CSS
  >>> response.css("li.next a::attr(href)").extract_first()
  >>> response.css("li.next a::attr(href)").extract()[0]
  >>> response.css("li.next a::attr(href)").get()
  >>> response.css("li.next a").attrib['href']
  XPATH (and CSS)
  >>> response.css('li.next a').xpath("@href").extract_first()
  >>> response.css('li.next a').xpath("@href").extract()[0]
  >>> response.css('li.next a').xpath("@href").get()

  Example to crawl site to get ALL links
  >>> response.css("a").xpath("@href").extract()

# DATA PIPELINE PROCESS
Scraped data -> Item Containers -> JSON/CSV Files
or Scraped data -> Item Containers -> Pipeline -> SQL/NoSQL Database

[Item file]
0. Create a temporary container called item.
[Spider file]
1. Extract data with spider's parse().
2. Store data into item
3. Store into a JSON, XML, or CSV
   `scrapy crawl quotes -o items.json`

# Questions/Terms?
Whitelisting IPs








# Use 'Sending e-mail' service