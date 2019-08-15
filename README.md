# book_spider
book spider

### Usage

```bash
scrapy crawl douban_book
```

#### 豆瓣图书搜索页爬取依赖服务
1. 安装splash服务
```bash
docker pull scrapinghub/splash #拉取镜像
docker run -p 8050:8050 scrapinghub/splash #启动实例
```

2. 安装scrapy-splash
```bash
pip install scrapy-splash
````
