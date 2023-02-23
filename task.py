import requests, operator
from nltk import word_tokenize, pos_tag

api_key = 'acc_3b937c6b7d1137c'
api_secret = '92bb273f7c80c1e316f9275424dc2b5b'
for j in range (1,71):
	s = open("/Users/danakoshen/darknet/data/test/"+str(j)+"/input","r").readline()
	nouns = [word for word, pos in pos_tag(word_tokenize(s)) if pos.startswith('NN') or pos.startswith("VBG")]
	d={1:0,2:0,3:0,4:0,5:0,6:0}
	for i in range (1,7):
		image_path = '/Users/danakoshen/darknet/data/test/'+str(j)+'/'+str(i)+'.jpg'
		response = requests.post('https://api.imagga.com/v2/tags',
		auth = (api_key, api_secret),
		files = {'image': open(image_path, 'rb')})
		for item in response.json()['result']['tags']:
			for t in nouns:
				if str(t) in str(item['tag']['en']):
					d[i]=d[i]+item['confidence']
	sorted_by_value = sorted(d.items(), key=lambda kv: kv[1])
	f=open("/Users/danakoshen/darknet/data/test/"+str(j)+"/output","w+")
	f.write(str(sorted_by_value[5][0]))
	f=open("/Users/danakoshen/darknet/data/test/output","a+")
	f.write(str(sorted_by_value[5][0])+"\n")
