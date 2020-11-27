# coding: utf-8
import webbrowser

url_list = ['https://webmasters.googleblog.com/','https://ai.googleblog.com/','http://www.unofficialgoogledatascience.com/','https://ai.google/research/pubs','https://www.blog.google/products/search/','https://www.thinkwithgoogle.com/advertising-channels/search/','https://www.reddit.com/user/johnmu','https://twitter.com/searchliaison','https://twitter.com/googlewmc','https://moz.com/blog','https://www.seroundtable.com/','https://www.gsqi.com/marketing-blog/','https://searchengineland.com/','https://searchenginewatch.com/tag/google-algorithm-updates/','http://www.seobythesea.com/','https://www.elephate.com/blog/','https://www.hobo-web.co.uk/seo-blog/','https://sparktoro.com/trending']

chrome_path = 'open -a /Applications/Google\\ Chrome.app %s'

for url in url_list:
	webbrowser.get(chrome_path).open_new(url)