
import os
import sys
import subprocess

import hdl_analyzer.Project as Project

import hdl_analyzer.scripts.hdl_analyzer_project as hdl_analyzer_project
import hdl_analyzer.scripts.hdl_analyzer_hiearchy as hdl_analyzer_hiearchy

def test_systemverilog_multi_hier_parse():
  testdir = os.path.dirname(os.path.abspath(__file__))
  cmd = ["tests/systemverilog_multi_hier.json", "--clear", "--dir", testdir, "--add-directory", os.path.join(testdir, "systemverilog_multi_hier")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/systemverilog_multi_hier.json", "--remove-file", os.path.join(testdir, "systemverilog_multi_hier/params.v")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/systemverilog_multi_hier.json", "--lang", "verilog", "--add-include", os.path.join(testdir, "systemverilog_multi_hier")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/systemverilog_multi_hier.json", "--analyze"]
  hdl_analyzer_project.main(cmd)
  #raise(Exception("Fail here"))

def test_systemverilog_multi_hier_hiearchy():
  cmd = ["tests/systemverilog_multi_hier.json", "--module", "top"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/systemverilog_multi_hier.json", "--instance", "i_logic_l1"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/systemverilog_multi_hier.json", "--module", "logic_l5", "--down"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/systemverilog_multi_hier.json", "--instance", "i_logic_l5_a", "--down"]
  hdl_analyzer_hiearchy.main(cmd)
  #raise(Exception("Fail here"))
