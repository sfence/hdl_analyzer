
import hdl_analyzer.Project as Project

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
   
  parser.add_argument("--file", dest = "file", help = "One file to be added to project.")
  
  parser.add_argument("--lang", dest = "lang", choices = ["verilog","systmeverilog","vhdl"], help = "hdl_analyzer project language to be modified.")
  parser.add_argument("--include", dest = "include", help = "One include to be added to project. --lang is required to be used with this.")
  parser.add_argument("--define", dest = "define", help = "One define to be added to project. --lang is required to be used with this.")
  
  parser.add_argument("--add-directory", dest = "add_directory", help = "Add all files from direcotry to hdl_analyzer project.")
  
  parser.add_argument("--set_project_dir", dest = "set_project_dir", default = None, help = "Set hdl_analyzer project directory before saving to json file.")

  args = parser.parse_args(args=argv)
  
  hdl_project = Project.Project(args.project_file, args.dir)
  
  if args.clear:
    hdl_project.clear()
  
  if args.file != None:
    hdl_project.add_file(args.file)
  if args.include != None:
    hdl_project.add_include(args.include, args.lang)
  if args.define != None:
    hdl_project.add_define(args.define, args.lang)

  if args.add_directory != None:
    files = os.listdir(args.add_directory)
    for file in files:
      hdl_project.add_file(file)
  
  dict_project = hdl_project.to_dict()
  if args.set_project_dir != None:
    dict_project["directory"] = args.set_project_dir
  with open(args.project_file, "w") as fp:
    json.dump(dict_project, fp, indent=2)

