
import hdl_analyzer.ProjectLanguage.Language as Language

from hdlConvertor import HdlConvertor
from hdlConvertorAst.language import Language as AstLanguage

class Verilog(Language.ProjectLanguage):
  def __init__(self, json_data, directory, language):
    super().__init__(json_data, directory, language)
    self.file_extensions = [".v"]
  
  def analyze(self, analyzer):
    convertor = HdlConvertor()
    for file_name in self.files:
      parsed = convertor.parse(file_name, AstLanguage.VERILOG, self.includes)
      analyzer.apply_parsed(parsed, file_name)

