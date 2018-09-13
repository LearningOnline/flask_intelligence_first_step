import os
from aip import AipSpeech
from aip import AipNlp
import test

""" 你的 APPID AK SK """
APP_ID = '11793737'
API_KEY = 'Mx8wLzbFk2VNVcjybf8lDzFH'
SECRET_KEY = 'DEc7I5q18z7aazW22LKDgwGocZ8h9VdR'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


# 用于将任何形式的语音文件格式转化成pcm格式
# 这里使用的是py3.6的模板语法，其他语言可以使用字符串的格式化语法
def get_file_content(filePath):
	os.system(f"ffmpeg -y -i {filePath} -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
	with open(f"{filePath}.pcm",'rb') as fp:
		return fp.read()

def text2audio(text):
	result = client.synthesis(text, 'zh', 1, {
		"spd": 4,
		'vol': 7,
		"pit": 8,
		"per": 4
	})

	if not isinstance(result, dict):
		# 创建一个audio.mp3文件
		with open('audio.mp3', 'wb') as f:
			f.write(result)

	return 'audio.mp3'


# 识别本地文件,转义成文本信息
def audio2text(file_path):
	a = client.asr(get_file_content(file_path), 'pcm', 16000, {
		'dev_pid': 1536,
	})

	if a.get("result") :
		return a.get("result")[0]


def my_nlp(q,uid):
	a = test.to_tuling(q,uid)
	return a

