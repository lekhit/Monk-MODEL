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

 
  def image(self,query=''):
    import random,os
    
    words=['cats','birds','shibes']
    word=random.choices(words,[20,10,20],k=1)[0]
    
    r=requests.get('https://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(word))
    
    js=json.loads(r.text)
    url=js[0]

    return url

  def anime(self):
    words=['waifu', 'neko', 'shinobu',     'megumin', 'bully', 'cuddle', 'cry',  'hug', 'awoo', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave',     'highfive', 'handhold', 'nom',         'bite', 'glomp', 'slap', 'kill',    'kick', 'happy', 'wink', 'poke',       'dance', 'cringe']
    reply=''
    for word in words:
      r=requests.get('https://api.waifu.pics/sfw/{}'.format(word))
      js=json.loads(r.text)
      print(json.dumps(js,indent=3))
      reply+=f"{word} \n{js['url']}\n"
    return reply

  def data(self):
    command=self.r
    if command=="inspire":
      return self.inspire()
    if command=="advice":
      return self.advice()
    if command=='image':
      return self.image()
    if command=="anime":
      return self.anime()
    else:
      return "wrong Data input"
    
