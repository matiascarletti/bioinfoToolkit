import os
import shutil

def iqtree_getPhyloTreeFrom(alignFolder, alignFileName, outFolder, bootstraps=1000 ):
    """
    Example shellCmd:
    iqtree -s alineamiento -bb 1000 
    """
    try:
        os.makedirs(outFolder)
    except FileExistsError:
        print("outfolder already exist")
    shellCmd = "iqtree -s %s/%s -bb %s" % (alignFolder, alignFileName, str(bootstraps))
    os.system(shellCmd)
    # TODO fix shutil not found files in the first 
    shutil.move(alignFolder + "/%s.treefile" % alignFileName, outFolder)
    shutil.move(alignFolder + "/%s.iqtree" % alignFileName, outFolder)
    shutil.move(alignFolder + "/%s.log" % alignFileName, outFolder)
    shutil.move(alignFolder + "/%s.ckp.gz" % alignFileName, outFolder)
    shutil.move(alignFolder + "/%s.model.gz" % alignFileName, outFolder)
    shutil.move(alignFolder + "/%s.bionj" % alignFileName, outFolder)
    shutil.move(alignFolder + "/%s.contree" % alignFileName, outFolder)
    shutil.move(alignFolder + "/%s.mldist" % alignFileName, outFolder)
    shutil.move(alignFolder + "/%s.splits.nex" % alignFileName, outFolder)
    return