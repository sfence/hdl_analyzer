
import hdl_analyzer.Project as Project
import hdl_analyzer.Analyzer.Analyzer as Analyzer

import argparse
import json
import os

def main(argv):
  parser = argparse.ArgumentParser(
      prog = "hdl_analyzer_project.py",
      description = "manupulate hdl_analyzer json project file."
    )
  
  parser.add_argument("project_file", help="hdl_analyzer JSON project file.")
  parser.add_argument("--dir", dest = "dir", default = None, help = "Redefinition of base directory.")
  
  parser.add_argument("--clear", dest = "clear", default = False, action = "store_true")
   
  parser.add_argument("--add-file", dest = "add_file", help = "One file to be added to project.")
  parser.add_argument("--remove-file", dest = "remove_file", help = "One file to be removed from project.")
  
  parser.add_argument("--lang", dest = "lang", choices = ["verilog","systemverilog","vhdl"], help = "hdl_analyzer project language to be modified.")
  parser.add_argument("--add-include", dest = "add_include", help = "One include to be added to project. --lang is required to be used with this.")
  parser.add_argument("--remove-include", dest = "remove_include", help = "One include to be removed from project. --lang is required to be used with this.")
  parser.add_argument("--add-define", dest = "add_define", help = "One define to be added to project. --lang is required to be used with this.")
  parser.add_argument("--remove-define", dest = "remove_define", help = "One define to be removed from project. --lang is required to be used with this.")
  
  parser.add_argument("--add-directory", dest = "add_directory", help = "Add all files from direcotry to hdl_analyzer project.")
  
  parser.add_argument("--set_project_dir", dest = "set_project_dir", default = None, help = "Set hdl_analyzer project directory before saving to json file.")
  
  parser.add_argument("--analyze", dest = "analyze", default = False, action = "store_true", help = "Test analyze with dummy analyzer.")
  parser.add_argument("--debug", dest = "debug", default = False, action = "store_true")

  args = parser.parse_args(args=argv)
  
  hdl_project = Project.Project(args.project_file, args.dir, False, args.debug)
  
  if args.clear:
    hdl_project.clear()
  
  if args.add_file != None:
    hdl_project.add_file(args.add_file)
  if args.add_include != None:
    hdl_project.add_include(args.add_include, args.lang)
  if args.add_define != None:
    hdl_project.add_define(args.add_define, args.lang)
  
  if args.remove_file != None:
    hdl_project.remove_file(args.remove_file)
  if args.remove_include != None:
    hdl_project.remove_include(args.remove_include, args.lang)
  if args.remove_define != None:
    hdl_project.remove_define(args.remove_define, args.lang)

  if args.add_directory != None:
    add_dir = os.path.abspath(args.add_directory)
    files = os.listdir(add_dir)
    for file_name in files:
      hdl_project.add_file(os.path.join(add_dir, file_name))
  
  if args.analyze:
    print("Dummy analyzer output:")
    analyzer = Analyzer.Analyzer(args.debug)
    hdl_project.analyze(analyzer)
    print(analyzer.get_result_text())
  
  dict_project = hdl_project.to_dict()
  if args.set_project_dir != None:
    dict_project["directory"] = args.set_project_dir
  with open(args.project_file, "w") as fp:
    json.dump(dict_project, fp, indent=2)

