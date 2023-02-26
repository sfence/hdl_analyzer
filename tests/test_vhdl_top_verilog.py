
import os
import sys
import subprocess

import hdl_analyzer.Project as Project

import hdl_analyzer.scripts.hdl_analyzer_project as hdl_analyzer_project
import hdl_analyzer.scripts.hdl_analyzer_hiearchy as hdl_analyzer_hiearchy

def test_vhdl_top_verilog_parse():
  testdir = os.path.dirname(os.path.abspath(__file__))
  cmd = ["tests/vhdl_top_verilog.json", "--clear", "--dir", testdir, "--add-directory", os.path.join(testdir,"vhdl_top_verilog")]
  hdl_analyzer_project.main(cmd)
  cmd = ["tests/vhdl_top_verilog.json", "--analyze"]
  hdl_analyzer_project.main(cmd)
  #raise(Exception("Fail here"))

def test_vhdl_top_verilog_hiearchy():
  cmd = ["tests/vhdl_top_verilog.json", "--module", "top"]
  hdl_analyzer_hiearchy.main(cmd)
  #raise(Exception("Fail here"))
