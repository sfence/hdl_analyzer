
import json
import os

import hdl_analyzer.ProjectLanguage as ProjectLanguage
import hdl_analyzer.ProjectLanguage.Verilog as LangVerilog
import hdl_analyzer.ProjectLanguage.SystemVerilog as LangSystemVerilog
import hdl_analyzer.ProjectLanguage.VHDL as LangVHDL

class Project():
  def __init__(self, project_file, directory, progress, debug):
    self.progress = progress
    self.debug = debug
    json_data = {}
    try:
      with open(project_file, "rb") as f:
        json_data = json.load(f)
    except:
      print("File \"{}\" does not exist.".format(project_file))
    
    if directory==None:
      if "directory" in json_data:
        directory = json_data["directory"]
      else:
        directory = ""
    self.directory = directory
  
    languages_data = {}
    if "languages" in json_data:
      languages_data = json_data["languages"]
    self.langs = {
      "verilog" : ProjectLanguage.Verilog.Verilog(languages_data, directory, "verilog"),
      "systemverilog" : ProjectLanguage.SystemVerilog.SystemVerilog(languages_data, directory, "systemverilog"),
      "vhdl" : ProjectLanguage.VHDL.VHDL(languages_data, directory, "vhdl")
    }
  
  def clear(self):
    json_data = {}
    self.langs = {
      "verilog" : ProjectLanguage.Verilog.Verilog(json_data, self.directory, "verilog"),
      "systemverilog" : ProjectLanguage.SystemVerilog.SystemVerilog(json_data, self.directory, "systemverilog"),
      "vhdl" : ProjectLanguage.VHDL.VHDL(json_data, self.directory, "vhdl")
    }
    
  def add_file(self, file_name):
    for lang in self.langs:
      self.langs[lang].add_file(os.path.join(self.directory, file_name))
  def remove_file(self, file_name):
    for lang in self.langs:
      self.langs[lang].remove_file(os.path.join(self.directory, file_name))

  def add_include(self, include, lang):
    if lang in self.langs:
      self.langs[lang].add_include(include)
      if self.debug:
        print("Add include {} for language {}".format(include, lang))
    else:
      if self.debug:
        print("Unknown include language {}".format(include, lang))
  def remove_include(self, include, lang):
    if lang in self.langs:
      self.langs[lang].remove_include(include)
      if self.debug:
        print("Remove include {} for language {}".format(include, lang))
    else:
      if self.debug:
        print("Unknown include language {}".format(include, lang))

  def add_define(self, define, lang):
    if lang in self.langs:
      self.langs[lang].add_define(define)
      if self.debug:
        print("Add define {} for language {}".format(define, lang))
    else:
      if self.debug:
        print("Unknown define language {}".format(include, lang))
  def remove_define(self, define, lang):
    if lang in self.langs:
      self.langs[lang].remove_define(define)
      if self.debug:
        print("Remove define {} for language {}".format(define, lang))
    else:
      if self.debug:
        print("Unknown define language {}".format(include, lang))
  
  def to_dict(self):
    languages_data = {}
    project_dict = {
        "directory" : self.directory,
        "languages" : languages_data
      }
    for lang in self.langs.keys():
      languages_data[lang] = self.langs[lang].to_dict(self.directory)
    return project_dict

  def analyze(self, analyzer):
    for lang in self.langs:
      if self.progress:
        print("Analyzing language {}".format(lang))
      self.langs[lang].analyze(analyzer, self.progress)

