
import os
import sys
import subprocess

import hdl_analyzer.Project as Project

import hdl_analyzer.scripts.hdl_analyzer_project as hdl_analyzer_project
import hdl_analyzer.scripts.hdl_analyzer_hiearchy as hdl_analyzer_hiearchy

def test_verilog_generate_parse():
  testdir = os.path.dirname(os.path.abspath(__file__))
  cmd = ["tests/verilog_generate.json", "--clear", "--dir", testdir, "--add-directory", os.path.join(testdir, "verilog_generate")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_generate.json", "--remove-file", os.path.join(testdir, "verilog_generate/params.v")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_generate.json", "--lang", "verilog", "--add-include", os.path.join(testdir, "verilog_generate")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/verilog_generate.json", "--analyze"]
  hdl_analyzer_project.main(cmd)
  #raise(Exception("Fail here"))

def test_verilog_generate_hiearchy():
  cmd = ["tests/verilog_generate.json", "--module", "top"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_generate.json", "--module", "top", "--print_inst_names"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_generate.json", "--instance", "i_logic_A"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_generate.json", "--instance", "i_logic_A", "--print_inst_names"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_generate.json", "--module", "xor_logic", "--down"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_generate.json", "--module", "xor_logic", "--down", "--print_inst_names"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_generate.json", "--instance", "i_logic_B", "--down"]
  hdl_analyzer_hiearchy.main(cmd)
  cmd = ["tests/verilog_generate.json", "--instance", "i_logic_B", "--down", "--print_inst_names"]
  hdl_analyzer_hiearchy.main(cmd)
  #raise(Exception("Fail here"))
