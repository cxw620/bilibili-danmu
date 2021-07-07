# 新手上路！
# 20210707 一边写一边学ing
import json
import sys
import time
import urllib3


def getdanmu():
    global jsonsaved, danmu_name, danmu_text, danmu
    if input("默认打开作者的直播间，确定吗？确认输入y，否则输入n") == "n":
        cid = input("请输入房间号：")
    else:
        cid = "21721322"
    print("调试信息：哟西，准备获取房间号为", cid, "的最近弹幕！")
    # 开始获取弹幕
    http = urllib3.PoolManager()
    r = http.request('GET', "https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid=" + cid, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"})
    if r.status != 200:
        print("获取弹幕失败，重试ing……")
        if http.request('GET', "https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid=" + cid, headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"}).status != 200:
            print("两次尝试ERROR!有可能api接口已经失效！程序终止！请联系作者！")
            sys.exit(1)
        else:
            time.sleep(1)
            r = http.request('GET', "https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid=" + cid,
                             headers={
                                 "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"})
    jsonsaved = json.loads(r.data.decode("utf-8"))
    savedanmu()
    # print(danmu)


# 由于后续的开发目标（弄个GUI）需要多次用到保存，就单独拎出来了
def savedanmu():
    # 不同def间公用变量？啊不懂
    global jsonsaved, danmu_name, danmu_text, danmu
    c = 1
    # 数组不太会用，只能用字典了
    danmu_name = []
    danmu_text = []
    # 目前设计为每次都会重置”弹幕库“，若做了GUI也考虑能否保存到文件
    danmu = {}
    while c <= len(jsonsaved["data"]["room"]):
        # python不支持dict的key为list或dict类型
        # 这里还是不满意，数组还是不太会
        danmu[len(danmu) + 1] = [jsonsaved["data"]["room"][c - 1]["check_info"]["ts"],
                                 jsonsaved["data"]["room"][c - 1]["nickname"], jsonsaved["data"]["room"][c - 1]["text"]]
        c = c + 1
    # 还是搞不太懂为什么加个return，但反正跑得起来就行了
    return


# delete selected danmu
# 受限学习进度，以下模块暂没有能力编写
def deletedanmu():
    pass


# 本来是想调用窗口程序显示出来，这个先挖坑吧
def showdanmu():
    pass


getdanmu()
