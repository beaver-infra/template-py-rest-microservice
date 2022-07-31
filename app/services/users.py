class ProfileModel():
  def __init__(self, *args, **kwargs):
    pass

  def helloWorld(self):
    response = {}
    try:
      response["status"] = "SUCCESS"
      response["data"] = str({
        "text": "Hello World!"
      })
      return response
    except Exception as e:
      print(e)
