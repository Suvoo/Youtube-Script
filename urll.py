import json
import urllib.request
import string
import random

count = 5
API_KEY = 'AIzaSyDdj9lRzF38phWaJSe5jCKeg-xTD_1mjnA'
random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,random)
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
results = json.loads(data.decode(encoding))

for data in results['items']:
    videoId = (data['id']['videoId'])
    ans = 'https://www.youtube.com/watch?v=' + videoId
    print(ans)
    #store your ids
