
import hdl_analyzer.ProjectLanguage.Language as Language

from hdlConvertor import HdlConvertor
from hdlConvertorAst.language import Language as AstLanguage

class SystemVerilog(Language.ProjectLanguage):
  def __init__(self, json_data, directory, language):
    super().__init__(json_data, directory, language)
    self.file_extensions = [".sv"]
  
  def analyze(self, analyzer, progress):
    convertor = HdlConvertor()
    index = 1
    for file_name in self.files:
      if progress:
        print("File {}/{}: {} ...".format(index, len(self.files), file_name))
        index = index + 1
      parsed = convertor.parse(file_name, AstLanguage.SYSTEM_VERILOG, self.includes)
      analyzer.apply_parsed(parsed, file_name)

