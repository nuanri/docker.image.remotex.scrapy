# ooclab/remotex-scrapy

## 目标

方便地运行 remotex scrapy spiders .

## 任务

创建一个 docker image - "ooclab/remotex-scrapy"
实现更新 github repo 可以触发 docker hub 的自动编译生成 ooclab/remotex-scrapy 镜像

## 运行

比如我们本地有个 spiders/ 目录，存放的是需要运行的 spider ，可以这样：

```
docker run -it --rm \
    -v "./spiders:/work/PyBots/spiders/" \
    -e "API_PREFIX=https://remotex.ooclab.org/api" \
    -e "API_KEY=我的秘钥" \
    ooclab/remotex-scrapy \
    scrapy crawl lagou
```
