### 注意！！！此教程只是出于学习交流目的，请不要恶意用于消耗某酷服务器资源 （2019/10/20）
---
# 优酷弹幕词云分析
### 注意！！！此教程只是出于学习交流目的，请不要恶意用于消耗某酷服务器资源

&nbsp;

**最近刚好在学习爬虫与数据分析，就想拿优酷的这部《我不能恋爱的女朋友》来分析一下，哈哈哈哈我也有在看，剧情有点搞笑。闲话不多说，进入主题吧！**

&nbsp; 
#### 技术方案
* 分析弹幕加载方式，用requests库进行爬取
* 这里就只爬取8集的弹幕
* 数据清洗（这里由于不是获取指定弹幕内容故没有数据清洗）
* 将弹幕做成词云

&nbsp; 
#### 实现过程
* 找到弹幕接口url 

    1. 打开某酷网站，等待广告加载完播放开始后，按f12调出浏览器调试窗口，复制一条弹幕，然后按ctrl+f 进行搜索。
![1.png](https://i.loli.net/2019/10/21/7YJ61khLg3QwqiH.png) &nbsp; 
    2. 点击搜索到的数据，点击header按钮，记住弹幕接口Url、请求头 Headers 和 Referer、 User-Agent 参数。
 ![2.png](https://i.loli.net/2019/10/21/7cjLYSrWyqVKD1t.png)
 &nbsp; 

* requests库构造请求，返回网页数据
  

&nbsp; 
* 提取弹幕数据
    ![3.png](https://i.loli.net/2019/10/21/zqtylcUAS6ndNEu.png)
 &nbsp; 

* 根据分析，发现弹幕接口 Url 中mat后接的数字是每表示分钟 ，iid后接的是第几集的id号
![43.png](https://i.loli.net/2019/10/21/o9VXaOIuA4qvC5w.png)

 &nbsp; 
* 这部电视剧40分钟左右一集，我们取40分钟，剩下的集数id我们需要再去获取。
    1. 我们将刚才找到的iid查找一下，在Preview里发现我们需要的集数iid就在这里
    ![88.png](https://i.loli.net/2019/10/21/RvBxYS65ioTpuFJ.png)
    ![15.png](https://i.loli.net/2019/10/21/BDbcvPNIqluftOM.png)
     &nbsp; 
    2. 记录下cookies，用requests请求返回网页数据
    ![41230.png](https://i.loli.net/2019/10/21/8dbhCQBL3lfqWIF.png)
     &nbsp; 
    
* 提取集数id数据
![7.png](https://i.loli.net/2019/10/21/pOCm8c57LbyXktS.png)
 &nbsp; 

* 到这里，弹幕数据就可以爬取下来了。我们可以将弹幕数据保存下来（我这里没有），最后是将弹幕数据做成词云
![wordcloud.png](https://i.loli.net/2019/10/21/cCKNvXmdnteEFfM.png)
 &nbsp; 

### 数据清洗虽然我这里没有做，但是从刚才的词云可以看出，哈哈哈这些词没多大意义，可以洗掉的啦。这只是一只粗略，简陋的蜘蛛，还没有很好，还有很多地方可以优化。这里就留给大家自己优化学习喽。

&nbsp; 
