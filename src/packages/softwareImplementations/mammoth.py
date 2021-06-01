import subprocess
import os


def mammoth_getStructureSuperimpositionFrom(pdbChainModel1, pdbChainModel2,
                                            outLogFolder=str, outLogName=str,
                                            structureAlignFile=0):
    """
    MAMMOTH: The valid command parameters are:
    REQUIRED args
    -p <predicted conformation file>
    -e <experimental conformation file>
    OPTIONAL args
    -nvec # CA in local alignment (default 9, suggested 7-14)
    -gapi gap insertion (default 0.21, suggested 0.2-1.4)
    -gape gap extension (default 0.008, suggested 0.01-0.1)
    -sigma sigma (default 5.00, suggested 3-10)
    -sim  simthr (default 0.48, suggested 3-10)
    -w1d  weight of 1D profile (default 0.240)
    -o <output information>
    -t <threshold z-score> for output of pdbs and SS alignment
    -r <1 or 0>  make pdb file  (default = 0  i.e. false)
    -v <1 or 0>  verbose output (default = 1)  (false also sets -t =100)
    -l <1 or 0>   calculate score in respect to the longest structure (default = 0)
    OPTIONAL BULK LIST PROCESSING MODE:
    if the first 12 characters of -e or -p file are 'MAMMOTH_List'
    then the file is interpreted as a list of files to process
    """
    # shellcmd = "mammoth -p %s -e %s -o %s/%s -r %s/%s" % (pdbChainModel1,
    #                                                     pdbChainModel2,
    #                                                     outLogFolder,
    #                                                     outLogName,
    #                                                     outPdbAlignFolder,
    #                                                     outPdbAlignName
    #                                                     )
    # os.system(shellcmd)
    subprocess.call(["mammoth",
                    "-p", pdbChainModel1,
                    "-e", pdbChainModel2,
                    "-o", "%s/%s" % (outLogFolder, outLogName),
                    "-r", str(structureAlignFile)
                    ], shell=False)
    return

# mammoth_getStructureSuperimpositionFrom("/home/matias/Projects/2020/RvDb_codnasHomologues/processed_data/2020-06-23/pdbFiles/RV6/Cluster_20103/5l7e_A.pdb", 
# "/home/matias/Projects/2020/RvDb_codnasHomologues/processed_data/2020-06-23/pdbFiles/RV6/Cluster_20103/5l7e_B.pdb",
# "/home/matias/Projects/2020/RvDb_codnasHomologues/processed_data/2020-06-23/pdbFiles/RV6/Cluster_20103",
# "/mammot.log")