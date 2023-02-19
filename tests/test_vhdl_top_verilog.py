
import sys
import subprocess

import hdl_analyzer.Project as Project

import hdl_analyzer.scripts.hdl_analyzer_project as hdl_analyzer_project

def test_vhdl_top_verilog():
  cmd = ["tests/vhdl_top_verilog.json", "--clear", "--add-directory", "tests/vhdl_top_verilog"]
  hdl_analyzer_project.main(cmd)
  raise Exception("Fail here")
