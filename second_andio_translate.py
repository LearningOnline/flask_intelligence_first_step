from aip import AipSpeech
import os
""" 你的 APPID AK SK """
APP_ID = '11793737'
API_KEY = 'Mx8wLzbFk2VNVcjybf8lDzFH'
SECRET_KEY = 'DEc7I5q18z7aazW22LKDgwGocZ8h9VdR'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

# 读取文件
filePath = "auido.mp3"
def get_file_content(filePath):
	# 用于将任何形式的语音文件格式转化成pcm格式，这里使用的是py3.6的模板语法，其他语言可以使用字符串的格式化语法
	os.system(f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
	with open(f"{filePath}.pcm",'rb') as fp:
		return fp.read()

# 识别本地文件
liu = get_file_content(filePath)

res = client.asr(liu,'pcm',16000,{
	'dev_pid':1536
})
print(res)  # 查看格式
# {'corpus_no': '6599876657908188502', 'err_msg': 'success.', 'err_no': 0,
# 'result': ['第一次把下列文字转MP3语音'], 'sn': '465883505901536653530'}

if res.get("result"):
	print(res.get('result')[0])

else:
	print(res)


#
#
