
import hdl_analyzer.ProjectLanguage.Language as Language

import hdlConvertorAst.to.json as AstToJson

class VHDL(Language.ProjectLanguage):
  def __init__(self, json_data, directory, language):
    super().__init__(json_data, directory, language)
    self.file_extensions = [".vhd",".vhdl"]
  
  def load(self, project):
    for file in self.files:
      project.load_modules(hdl_structure)
