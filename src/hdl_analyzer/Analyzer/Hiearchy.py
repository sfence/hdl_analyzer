
from hdl_analyzer.Analyzer import Analyzer

#from hdlConvertorAst.hdlAst import HdlModuleDef, HdlCompInst, HdlStmFor
from hdlConvertorAst.hdlAst import *

class Instance:
  def __init__(self, inst_name, module_name):
    self.name = inst_name
    self.module_name = module_name
    self.parents = []
    self.children = []

class Hiearchy(Analyzer.Analyzer):
  def __init__(self, debug, down):
    super().__init__(debug)
    
    self.down = down
    self.modules = dict()
  
  def _apply_in_moduledef(self, hdl_object, module_name):
    if self.debug:
      print("Module: {} object type: {}".format(module_name, type(hdl_object)))
    if isinstance(hdl_object, HdlCompInst):
      self.modules[module_name].append(Instance(str(hdl_object.name), str(hdl_object.module_name)))
      if self.debug:
        print("Module {} add instanace {}".format(module_name, hdl_object.module_name))
    elif isinstance(hdl_object, HdlStmFor):
      self._apply_in_moduledef(hdl_object.body, module_name)
    elif isinstance(hdl_object, HdlStmBlock):
      for subobj in hdl_object.body:
        self._apply_in_moduledef(subobj, module_name)
    elif isinstance(hdl_object, HdlStmAssign):
      pass
    elif isinstance(hdl_object, HdlStmProcess):
      pass
    elif isinstance(hdl_object, HdlIdDef):
      pass
    else:
      if self.debug:
        print(hdl_object)
  
  def _add_parents(self, update_instance, parent_module):
    for instances in self.modules.values():
      for instance in instances:
        if instance.module_name == parent_module:
          update_instance.parents.append(instance)
          if self.debug:
            print("{} new parent {}".format(update_instance.module_name, instance.module_name))
  
  def _add_children(self, update_instance):
    if update_instance.module_name in self.modules:
      instances = self.modules[update_instance.module_name]
      for instance in instances:
        update_instance.children.append(instance)
        if self.debug:
          print("{} new child {}".format(update_instance.module_name, instance.module_name))
  
  def _get_down(self, instance, hier, max_levels):
    if max_levels<0:
      raise Exception("Analyzer _get_down method reached maximum number of allowed levels.")
    results = []
    if len(instance.parents)>0:
      for parent in instance.parents:
        result = hier.copy()
        result.insert(0,parent)
        sub_results = self._get_down(parent,result, max_levels - 1)
        for sub_result in sub_results:
          results.append(sub_result)
    else:
      results.append(hier)
    return results
  
  def _results_text_up(self, text, instance, prefix, use_inst_name):
    for child in instance.children:
      name = child.module_name
      if use_inst_name:
        name = "{}({})".format(child.name, child.module_name)
      text = "{}\n{}{}".format(text, prefix, name)
      if name in self.modules:
        text = "{}{}".format(text, self._results_text_up("", child, "{}  ".format(prefix), use_inst_name))
    return text
    
  def apply_parsed(self, parsed, file_name):
    #if self.debug:
    #  print("{}:\n{}".format(file_name,parsed))
    for obj in parsed.objs:
      if isinstance(obj, HdlModuleDef):
        module_name = str(obj.module_name)
        self.modules[module_name] = []
        for subobj in obj.objs:
          self._apply_in_moduledef(subobj, module_name)
  
  def calculate_hiearchy(self):
    for module in self.modules:
      instances = self.modules[module]
      for instance in instances:
        self._add_parents(instance, module)
        self._add_children(instance)
    
  def get_result_for_instance(self, inst_name, max_levels):
    results = []
    for module in self.modules:
      instances = self.modules[module]
      for instance in instances:
        if instance.name == inst_name:
          if self.down:
            sub_results = self._get_down(instance, [], max_levels)
            for sub_result in sub_results:
              results.append(sub_result)
          else:
            results.append(instance)
    return results

  def get_result_for_module(self, module_name, max_levels):
    results = []
    if self.down:
      for module in self.modules:
        instances = self.modules[module]
        for instance in instances:
          if instance.module_name == module_name:
            results = self._get_down(instance, [], max_levels)
            sub_results = self._get_down(instance, [], max_levels)
            for sub_result in sub_results:
              results.append(sub_result)
    else:
      if module_name in self.modules:
        top_instance = Instance("", module_name) 
        results.append(top_instance)
        instances = self.modules[module_name]
        for instance in instances:
          top_instance.children.append(instance)
    return results

  def get_result_for_vivado(self):
    results = []
    for instances in self.modules:
      for instance in instances:
        if len(instance.parents)==0:
          sub_results = self._get_down(instance, [], max_levels)
          for sub_result in sub_results:
            results.append(sub_result)
    return results

  def results_text(self, results, use_inst_name):
    text = ""
    if self.down:
      for hier in results:
        prefix = ""
        for instance in hier:
          name = instance.module_name
          if use_inst_name:
            name = "{}({})".format(instance.name, instance.module_name)
          text = "{}{}{}".format(text, prefix, name)
          prefix = "."
        text = "{}\n".format(text)
    elif len(results)==1:
      instance = results[0]
      name = instance.module_name
      if use_inst_name:
        name = "{}({})".format(instance.name, instance.module_name)
      text = "{}".format(name)
      text = self._results_text_up(text, instance, "  ", use_inst_name)
    else:
      text = "No valid results found."
    return text

