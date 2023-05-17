
import os
import sys
import subprocess

import hdl_analyzer.Project as Project

import hdl_analyzer.scripts.hdl_analyzer_project as hdl_analyzer_project
import hdl_analyzer.scripts.hdl_analyzer_hiearchy as hdl_analyzer_hiearchy

def test_verilog_params_like_arm_parse():
  testdir = os.path.dirname(os.path.abspath(__file__))
  cmd = ["tests/verilog_params_like_arm.json", "--clear", "--dir", testdir, "--add-directory", os.path.join(testdir, "verilog_params_like_arm")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_params_like_arm.json", "--remove-file", os.path.join(testdir, "verilog_paramns_like_arm/params.v")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_params_like_arm.json", "--lang", "verilog", "--add-include", os.path.join(testdir, "verilog_params_like_arm")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_params_like_arm.json", "--analyze"]
  hdl_analyzer_project.main(cmd)
  #raise(Exception("Fail here"))

def test_verilog_params_like_arm_hiearchy():
  cmd = ["tests/verilog_params_like_arm.json", "--module", "top"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_params_like_arm.json", "--instance", "i_logic_l1"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_params_like_arm.json", "--module", "logic_l5", "--down"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_params_like_arm.json", "--instance", "i_logic_l5_a", "--down"]
  hdl_analyzer_hiearchy.main(cmd)
  #raise(Exception("Fail here"))
