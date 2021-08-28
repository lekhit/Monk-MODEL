import random
class Decider:
  def __init__(self,message,client):
    self.message=message
    self.msg=message.content
    self.client=client

  def for_me(self):
    if self.message.author == self.client.user:
      return False

    if self.client.user.mentioned_in(self.message) or self.msg.startswith(".") or self.msg.startswith("$"):

      return True

    return False
  
  def requirements(self):
    available=['image']
    basic=["inspire","advice"]
    for word in available:
      if word in self.msg or word[0] in self.msg:
        return word
    var=random.choices(basic,[10,10],k=1)
    return var[0]

 
  def to_name(self):
    to=[]
    # if self.message.reference:
    #   self.get_mentions()
    #   author=self.author
    #   to.append(author)

    mentions=self.message.mentions
    for mention in mentions:
      if self.message.author != self.client.user:
        to.append(mention.name)

    if 'r' in self.msg:
      to.append(random.choice(self.message.channel.guild.members).name)

    if not to :
        to.append(self.message.author.name)
    
    #to=list(map(lambda item : item+',',to))
    self.to1= to

  def to(self):
    self.to_name()
    return self.to1
    

     