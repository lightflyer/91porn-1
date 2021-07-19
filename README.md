# 91porn
91pron爬虫


爬虫部分代码主要来自https://github.com/jakehu/91porn 感谢jakehu
m3u8下载软件主要代码来自https://github.com/magicdmer/M3U8-Downloader 感谢magicdmer

由于我也是新手，在使用jakehu大神的成品时发现可以获取网页链接但是没法获取视频的下载地址，不知道是我不会用还是获取视频下载地址的方式已经失效了，于是就基于他的代码进行了修改，去除了redis的依赖，直接把链接写入到文件里了，这样虽然效率低了，但是用起来简单了很多也没什么问题。M3U8下载器部分则是对magicdmer大神的代码进行了修改，把原本的手动输入下载链接改为从文件里获取，并且支持标题。真正完全由本人写的部分只有downloadm3u8.py

使用方式：
1.下载所有的py文件和运行.bat文件放到同一个文件夹内,下载M3U8Dwonloader.7z解压到任意位置（建议和前面那些py文件放一起）
2.运行 运行.bat，根据提示输入想要抓取的页数（确保自己能访问91的网址，网址在common.py的第16行）
3.等到cmd窗口出现      所有视频下载地址获取完成，接下来可以把存在m3u8url.txt中的结果复制到M3U8Dwonloader中下载了       这个提示的时候就可以关闭cmd打开前面解压出来的M3U8 Downloader.exe选择前面生成的m3u8url.txt文件下载了。


不用爬太多，后面的视频基本都失效了，目前的设置可以下载大约1100个左右。如果想下更多，可以去parse_list里修改第26行，比如改成 /video.php?category=long&page= 就是下载超过10分钟的视频还有其他关键字自己去网站里找了替换就行。
