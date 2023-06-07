
import hdl_analyzer.Project as Project

import hdl_analyzer.Analyzer.Hiearchy as Analyzer

import argparse
import json
import os

def main(argv):
  parser = argparse.ArgumentParser(
      prog = "hdl_analyzer_hiearchy.py",
      description = "Open hdl_analyzer json project file and analyze hiearchy for wanted instance/module."
    )
  
  parser.add_argument("project_file", help="hdl_analyzer JSON project file.")
  parser.add_argument("--dir", dest = "dir", default = None, help = "Redefinition of base directory.")
  
  parser.add_argument("--down", dest = "down", default = False, action = "store_true", help = "Change hiearchy finding direction.")
  parser.add_argument("--print_inst_names", dest = "use_inst_name", default = False, action = "store_true", help = "Print instance names instead of module names.")
  parser.add_argument("--instance", dest = "instance", default = None, help = "Hiearchy for instance.")
  parser.add_argument("--module", dest = "module", default = None, help = "Hiearchy for module.")
  parser.add_argument("--vivado", dest = "vivado", default = None, help = "Hiearchy for vivado (Tcl).")
  
  parser.add_argument("--max_levels", dest = "max_levels", type = int, default = 999, help = "Hiearchy max levels to check.")
  
  parser.add_argument("--progress", dest = "progress", default = False, action = "store_true", help = "Print some progress info.")
  parser.add_argument("--debug", dest = "debug", default = False, action = "store_true")
  
  args = parser.parse_args(args=argv)
  
  hdl_project = Project.Project(args.project_file, args.dir, args.progress, args.debug)
    
  analyzer = Analyzer.Hiearchy(args.debug, args.down)
  hdl_project.analyze(analyzer)
  analyzer.calculate_hiearchy()
  
  if args.instance != None:
    results = analyzer.get_result_for_instance(args.instance, args.max_levels)
    print("Output for instance {}:".format(args.instance))
    print(analyzer.results_text(results, args.use_inst_name))
    print("")
  if args.module != None:
    results = analyzer.get_result_for_module(args.module, args.max_levels)
    print("Output for module {}:".format(args.module))
    print(analyzer.results_text(results, args.use_inst_name))
    print("")
  if args.vivado != None:
    results = analyzer.get_result_for_vivado()
   
