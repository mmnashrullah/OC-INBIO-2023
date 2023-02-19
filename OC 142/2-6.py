# ME

import os
from dendropy.interop.paup import PaupService
from Bio import Phylo
import matplotlib
from matplotlib import pyplot

PAUP_bin = "D:\\BIOTOOLS\\PAUP4\\paup4c.exe"

curr_dir = os.getcwd()
NEXUS_file = curr_dir + "\\Trimmed najas31.nexus"
NEXUS_BootstrapTrees_file = curr_dir + "\\BTSTRP ME najas31.nexus"
NEWICK_Tree_file = curr_dir + "\\ME najas31.nwk"

PAUP_block = """\
    begin paup;
      cd '%s';
      execute '%s';
      outgroup 'MZ827035 Bungarus caeruleus isolate ZSI SRC R-631';
      set criterion=distance;
      lset nst=6 rclass=(abacdc) rmatrix=(12.294613 174.65795 12.294613 1 77.174033) basefreq=(0.25577179 0.2905658 0.15351004) pinv=0.69474281;
      dset distance=P objective=ME; 
      bootstrap search=heuristic nreps=100 conlevel=50 treefile='%s' format=Nexus /start=stepwise swap=NNI;
    end
""" % (curr_dir, NEXUS_file, NEXUS_BootstrapTrees_file)

if not os.path.isfile(NEXUS_BootstrapTrees_file):
    print("File Bootstrap Tree" , NEXUS_BootstrapTrees_file, "Belum ada!")
    print("Membuat:" , NEXUS_BootstrapTrees_file)
    returncode, stdout, stderr = PaupService.call(
                paup_commands=PAUP_block,
                paup_path=PAUP_bin,
                cwd = os.getcwd(),
                )
    print(returncode, stdout, stderr)
    print(NEXUS_BootstrapTrees_file, "selesai dibuat!")
else:
    print("Tidak bisa membuat file Bootstrap Tree!")
    print("Karena file" , NEXUS_BootstrapTrees_file, "ada!")

#Cari pohon konsensus
PAUP_block = """\
    begin paup;
      cd '%s';
      execute '%s';
      outgroup 'MZ827035 Bungarus caeruleus isolate ZSI SRC R-631';
      set root=outgroup;
      contree all/strict=no majrule=yes treefile='%s' usetreewts=yes saveasrooted=yes format=Newick;
    end
""" % (curr_dir, NEXUS_BootstrapTrees_file, NEWICK_Tree_file)

if not os.path.isfile(NEWICK_Tree_file):
    print("File Consensus Tree" , NEWICK_Tree_file, "Belum ada!")
    print("Membuat:" , NEWICK_Tree_file)
    returncode, stdout, stderr = PaupService.call(
                paup_commands=PAUP_block,
                paup_path=PAUP_bin,
                cwd = os.getcwd(),
                )
    print(returncode, stdout, stderr)
    print(NEWICK_Tree_file, "selesai dibuat!")
else:
    print("Tidak bisa membuat file Consensus Tree!")
    print("Karena file" , NEWICK_Tree_file, "ada!")
    
#baca dan plot filogeni
Filogeni = Phylo.read(NEWICK_Tree_file, "newick")
matplotlib.rc("font", size = 40)
matplotlib.rc("axes", titlesize = 40)
matplotlib.rc("axes", labelsize = 40)
matplotlib.rc("xtick", labelsize = 40)
matplotlib.rc("ytick", labelsize = 40)
fig = pyplot.figure(figsize = (50, 20), dpi = 300)
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(Filogeni, show_confidence = True, axes = axes)