import os
import glob

def fpocket(pdbDbFilesFolder=str, pdbDbFile=str):
    """
    Purpose:
                Run fpocket for a list of PdbDb files (cif or pdb formats) \
                or altenatively for an only PdbDb file (cif or pdb formats)
    Parameters:
                - pdbFilesFolder  (str)   a path to the target pdb files folder \
                - pdbFile         (str)   a path to the target pdb or cif file
    Command line example:
            fpocket -F {pdbFilesFolder}
            fpocket -f {pdbFile}
    """
    if pdbDbFilesFolder:
        pdbDbFilesList    = glob.glob(pdbDbFilesFolder + "/*.pdb")
        for pdbDbFile in pdbDbFilesList:
            with open(pdbDbFilesFolder + "/pdbFileList.list", "a") as f:
                f.write(f"{pdbDbFile}\n")
        pdbDbFileList = open(pdbDbFilesFolder + "/pdbFileList.list", "r")
        os.system(f"fpocket -F {pdbDbFileList}")
    else:
        os.system(f"fpocket -f {pdbDbFile}")
    return