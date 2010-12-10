import vtk, qt, ctk
import slicer
from slicer.util import *
import slicer.cli

#
# Internal
#

class _Internal():
  import slicer.util

  def __init__(self):
    global _qSlicerCoreApplicationInstance
    app = _qSlicerCoreApplicationInstance
    slicer.util._app = app

    import imp
    moduleManager = app.moduleManager()
    factoryManager = moduleManager.factoryManager()
    factoryManager.connect('allModulesRegistered()', self.setSlicerModuleNames)
    moduleManager.connect('moduleLoaded(qSlicerAbstractCoreModule*)', self.setSlicerModules)

    # Add module slicer.moduleNames
    _moduleNames = imp.new_module('moduleNames')
    setattr(slicer, _moduleNames.__name__, _moduleNames)

    # Add module slicer.modules
    _modules = imp.new_module('modules')
    setattr(slicer, _modules.__name__, _modules)

    # Retrieve current instance of the scene and set 'slicer.mrmlScene'
    setattr(slicer, 'mrmlScene', app.mrmlScene())


  def setSlicerModuleNames(self):
    """Add module names as attributes of module slicer.moduleNames"""
    for name in moduleNames():
      setattr(slicer.moduleNames, name, name)

  def setSlicerModules(self, module):
    """Add modules as attributes of module slicer.modules"""
    setattr(slicer.modules, module.name, module)


_internalInstance = _Internal()
