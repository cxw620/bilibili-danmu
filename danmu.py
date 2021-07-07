# 新手上路！
# 20210707 一边写一边学ing
import json
import sys
import time
import urllib3


def getdanmu():
    global jsonsaved, danmu_name, danmu_text, danmu_no
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
    # print(danmu_name)


# 由于后续的开发目标（弄个gui）需要多次用到保存，就单独拎出来了
def savedanmu():
    global jsonsaved, danmu_name, danmu_text, danmu_no
    c = 1
    # 数组不太会用，只能用字典了
    danmu_name = {}
    danmu_text = {}
    danmu_no = {}
    while c <= 10:
        ts = jsonsaved["data"]["room"][c - 1]["check_info"]["ts"]
        danmu_name[ts] = jsonsaved["data"]["room"][c - 1]["nickname"]
        danmu_text[ts] = jsonsaved["data"]["room"][c - 1]["text"]
        danmu_no[str(len(danmu_name) + 1)] = ts
        c = c + 1
    return


# delete selected danmu
# 受限学习进度，以下模块暂没有能力编写
def deletedanmu():
    pass


# 本来是想调用窗口程序显示出来，这个先挖坑吧
def showdanmu():
    pass


getdanmu()
