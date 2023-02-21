
import os

class ProjectLanguage():
  def __init__(self, json_data, directory, language):
    self.files = []
    self.includes = []
    self.defines = []
    
    self.file_extensions = []
    
    if language in json_data:
      language_data = json_data[language]
      
      if "files" in language_data:
        for file in language_data["files"]:
          self.files.append(os.path.join(directory,file))
      if "includes" in language_data:
        for include in language_data["includes"]:
          self.includes.append(os.path.join(directory,include))
      if "defines" in language_data:
        self.defines = language_data["defines"]

  def add_file(self, file):
    split_path = os.path.splitext(file)
    if split_path[1] in self.file_extensions:
      self.files.append(file)
  
  def add_include(self, include):
    sel.includes.append(include)
  
  def add_define(self, define):
    sel.defines.append(define)
  
  def to_dict(self, directory):
    out_dict = {
        "files": [],
        "includes": [],
        "defines": self.defines
      }
    
    for file in self.files:
      out_dict["files"].append(os.path.relpath(file, directory))
    for include in self.includes:
      out_dict["includes"].append(os.path.relpath(include, directory))
    return out_dict

  def analyze(self, analyzer):
    pass

