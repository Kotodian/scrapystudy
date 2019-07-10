##安装Scrapy框架
```python
scrapy start project [projectname]
```


##创建爬虫
```python
scrapy genspider example example.com
```
##获取数据
```python
#response是一个'scrapy.http.response.html.HtmlResponse'对象,可执行'xpath'和'css'方法获取数据。
response.xpath()#返回selectorList
response.xpath().xpath()#返回selector
#getall获取全部文本返回一个列表

```
##运行命令行
```python
from scrapy import cmdline
cmdline.execute(""scrapy crawl qsbk_spider".split()")
```
##数据解析
```python
#yleid 返回数据提交到pipline处理
#pipline获得数据将其转换成json数据格式。

```

###JsonItemExporter和JsonLinesItemExporter:
- 保存json数据的时候,可以使用这两个类,让操作变更简单。
