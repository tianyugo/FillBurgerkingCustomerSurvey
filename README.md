
## 自动填写汉堡王问卷调查by Python+Selenium

作为一个薅羊毛爱好者，发现了填写汉堡王小票的问卷调查可以换小薯之后，开始了+小薯的愉快生活。作为一个自动化专业的银，填写调查怎么能不自动化。

### Python3

略

### Selenium

- 浏览器自动化测试框架：Selenium /səˈliːniəm/

可以用来实现：

- 控制浏览器（浏览器打开网址、控制窗口大小、关闭等）

- 定位符进行定位操作（根据网页源代码中HTML的各类标签进行定位）

	`find_elements_by_XXXXX('需要被找查找的元素')` XXX可以选择多种不同方法：id、name、xpath等

- 鼠标键盘的操作（点击、键盘输入等多种操作）

更多内容可以参考：

- 一文详解：[以后再有人问你selenium是什么，你就把这篇文章给他
](https://blog.csdn.net/TestingGDR/article/details/81950593)


安装方式：在线pip


由于 安装好的 Python 默认有 pip Python 包管理工具，可以通过 pip 非常方便的安装 Selenium。

- 启动命令行工具：Win+R + cmd 

- 输入命令：pip install selenium



### Chromedriver

本项目使用的是Chrome浏览器,下载地址如下：


-  [Chromedriver](http://chromedriver.storage.googleapis.com/index.html)

根据浏览器版本下载对应的驱动，可以通过设置—关于Chrome查看自己浏览器的版本。但在实际选择驱动版本的时候，会发现没有完全对应的版本。例如我的浏览器：Google Chrome 已是最新版本
版本 77.0.3865.90（正式版本），而我选择driver版本：77.0.3865.40  能够成功实现。

-  其他可供选择的驱动：
 


 Firefox:[https://github.com/mozilla/geckodriver/releases/](https://github.com/mozilla/geckodriver/releases/)



IEdriver:[http://www.nuget.org/packages/Selenium.WebDriver.IEDriver/](http://www.nuget.org/packages/Selenium.WebDriver.IEDriver/)


### 程序
根据前人的工作["Python 3 + Selenium 3 实现汉堡王客户调查提交"](https://www.cnblogs.com/herbert/p/10852841.ht )进行了进一步的改进，进一步实现了自动提取验证码。

程序基于unittest单元测试框架。暂有改进思路：
	
- 实现多调查码同意完成



