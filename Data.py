import requests,json
class Data:
  def __init__(self,requirements):
    self.r=requirements


  def inspire(self):
    r = requests.get('https://zenquotes.io/api/random')
    result = json.loads(r.text)
    data = result[0]['q']
    author = result[0]['a']
    self.data= f'```{data}```\n- {author}'
    return self.data

  def advice(self):
    data = requests.get(
                'https://api.adviceslip.com/advice').json()['slip']['advice']
    self.data = f'```{data}```'
    return self.data

 
  def image(query=''):
    import random,os
    
    words=['cats','birds','shibes']
    word=random.choices(words,[20,10,20],k=1)[0]
    
    r=requests.get('https://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(word))
    
    js=json.loads(r.text)
    url=js[0]

    return url

  def data(self):
    command=self.r
    if command=="inspire":
      return self.inspire()
    if command=="advice":
      return self.advice()
    if command=='image':
      return self.image()
    else:
      return "wrong Data input"
    
