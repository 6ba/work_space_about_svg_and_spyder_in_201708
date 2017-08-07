""""""
## 所有的信息使用 pandas 的数据框进行存储;

"""
 - 如果存在列中适合用 int 存储就用int，如果存在适合用 float 就用float(m, n)；
否则 都用 varchar 类型 存储。如果是datetime 格式, 进行妥善判断后用datatime 存储。

"""

"""
str(av), str(av), cid, title, tminfo, time, click, danmu, coins, favourites, duration,
                                 mid, name, article, fans, tag1, tag2, tag3, str(common), honor_click, honor_coins,
                                 honor_favourites
"""


"""
drop table if exists `bilibili_tv_info`;
CREATE TABLE `bilibili_tv_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `av` varchar(11) DEFAULT NULL,
  `cid` int(11) unsigned NOT NULL,
  `title` varchar(11) DEFAULT NULL,
  `tminfo` varchar(200) DEFAULT NULL,
  `coins` int(11) DEFAULT NULL,
  `regtime` varchar(45) DEFAULT NULL,
  `spacesta` int(11) DEFAULT NULL,
  `birthday` varchar(45) DEFAULT NULL,
  `place` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `article` int(11) DEFAULT NULL,
  `fans` int(11) DEFAULT NULL,
  `friend` int(11) DEFAULT NULL,
  `attention` int(11) DEFAULT NULL,
  `sign` varchar(300) DEFAULT NULL,
  `attentions` text,
  `level` int(11) DEFAULT NULL,
  `exp` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;




"""