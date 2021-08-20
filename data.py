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

  def data(self):
    if self.r=="inspire":
      return self.inspire()
    if self.r=="advice":
      return self.advice
    else:
      return "wrong Data input"
    
