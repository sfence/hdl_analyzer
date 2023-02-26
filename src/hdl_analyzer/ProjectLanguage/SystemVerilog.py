
import hdl_analyzer.ProjectLanguage.Language as Language

from hdlConvertor import HdlConvertor
from hdlConvertorAst.language import Language as AstLanguage

class SystemVerilog(Language.ProjectLanguage):
  def __init__(self, json_data, directory, language):
    super().__init__(json_data, directory, language)
    self.file_extensions = [".sv"]
  
  def analyze(self, analyzer):
    convertor = HdlConvertor()
    for file_name in self.files:
      parsed = convertor.parse(file_name, AstLanguage.SYSTEMVERILOG, self.includes)
      analyzer.apply_parsed(parsed, file_name)

