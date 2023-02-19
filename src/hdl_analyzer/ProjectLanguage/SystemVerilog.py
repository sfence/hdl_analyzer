
import hdl_analyzer.ProjectLanguage.Language as Language

import hdlConvertorAst.to.json as AstToJson

class SystemVerilog(Language.ProjectLanguage):
  def __init__(self, json_data, directory, language):
    super().__init__(json_data, directory, language)
    self.file_extensions = [".sv"]

