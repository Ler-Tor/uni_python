import requests
res = requests.get('http://apple.com')
print(res.status_code)
print(res.headers['Content-Type'])
print(res.content)
with open ('site.png','w') as f:
	f.write(res.conten))
