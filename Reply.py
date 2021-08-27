class Reply:
  def __init__(self,data,to):
    self.data=data
    self.to=to

  def reply(self):
    addressed=self.to
    out=""
    for address in addressed:
      out+=address+', '
    starter=f"My Dear {out}"
    data=f'{starter}\n{self.data}'
    return data

