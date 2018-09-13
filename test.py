import requests
import json
import third

apiKey = "d76b3e9669404fe7b5a1949466fd6376"
userId = "taylor"  # 机器人名称
data = {
    # 请求的类型 0 文本 1 图片 2 音频
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": "你是谁"
        }
    },
    "userInfo": {
        "apiKey": apiKey,
        "userId": userId
    }
}

tuling_url = "http://openapi.tuling123.com/openapi/api/v2"

def to_tuling(question,user_id):
    # 修改请求参数中的inputText，也就是问题
    data["perception"]["inputText"]["text"] = question
    # # 修改userInfo
    data["userInfo"]["userId"] = user_id

    res = requests.post(tuling_url,json=data)  # 请求url
    # 将返回信息解码
    res_dic = json.loads(res.content.decode("utf-8"))  # type:dict
    # 得到返回信息中的文本信息
    result = res_dic.get("results")[0].get("values").get("text")
    # print(res_type)

    return result