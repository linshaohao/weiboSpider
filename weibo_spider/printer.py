# -*- coding: UTF-8 -*-


def print_one_weibo(weibo):
    """打印一条微博"""
    print(weibo["content"])
    print(u"微博发布位置：%s" % weibo["publish_place"])
    print(u"发布发布时间：%s" % weibo["publish_time"])
    print(u"发布发布工具：%s" % weibo["publish_tool"])
    print(u"点赞数：%d" % weibo["up_num"])
    print(u"转发数：%d" % weibo["retweet_num"])
    print(u"评论数：%d" % weibo["comment_num"])
    print(u"url：https://weibo.cn/comment/%s" % weibo["id"])
    print("-" * 100)


def print_user_info(user):
    """打印微博用户信息"""
    print(u"用户昵称: %s" % user["nickname"])
    print(u"用户id: %s" % user["id"])
    print(u"微博数: %d" % user["weibo_num"])
    print(u"关注数: %d" % user["following"])
    print(u"粉丝数: %d" % user["followers"])

