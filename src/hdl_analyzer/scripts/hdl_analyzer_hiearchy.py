
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
  
  args = parser.parse_args(args=argv)
  
  hdl_project = Project.Project(args.project_file, args.dir)

