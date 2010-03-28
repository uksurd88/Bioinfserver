# Homology modeling by the automodel class
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in
env.io.hetatm = True # Ligand is made true
env.io.water = True  # Water molecule made true

# directories for input atom files
#env.io.atom_files_directory = ['.', '../atom_files']

a = automodel(env,
              alnfile  = 'alignment.ali',     # alignment filename
              knowns   = 'template',          # codes of the templates	
              sequence = 'model')             # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 5                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual homology modeling

