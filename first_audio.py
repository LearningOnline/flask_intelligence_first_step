from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '11793737'
API_KEY = 'Mx8wLzbFk2VNVcjybf8lDzFH'
SECRET_KEY = 'DEc7I5q18z7aazW22LKDgwGocZ8h9VdR'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

result = client.synthesis("第一次把下列文字转成MP3语音","zh",1,{
        "spd":4,
        "vol":7,
        "pit":8,
        "per":4
})

if not isinstance(result,dict):
    # 创建一个auido.mp3文件
    with open("auido.mp3","wb") as f:
        f.write(result)

print(result)   # 打印bytes字节
