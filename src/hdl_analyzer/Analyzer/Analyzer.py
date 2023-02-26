
class Analyzer:
  def __init__(self, debug):
    self.debug = debug
  
  def apply_parsed(self, parsed, file_name):
    if self.debug:
      print(type(parsed))
  
  def get_result_text(self):
    return "Dummy analyzer result."

