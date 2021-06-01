import subprocess
import os
import shutil

def clustalw_getMultipleSequenceAlignementFrom(mfastaFolder, mfastaFileName,
                                                outFolder,
                                                outMsaName,
                                                outFormat):
    """
    Purpose: Command line for run clustalw

    Parameters:
    -INFILE=archivo_de_entrada (este no puede tener espacios) 
    -OUTFILE=archivo_de_salida 
    -OUTPUT=fasta (-OUTPUT te da la opcion de elegir el formato de salida. Puede ser fasta, phylip, etc)
    """
    try:
        os.makedirs(outFolder)
    except FileExistsError:
        print("Out folder already exist")
    shellcmd = "clustalw -INFILE=%s/%s -OUTFILE=%s/%s -OUTPUT=%s" % (mfastaFolder, mfastaFileName,
                                                                outFolder, 
                                                                outMsaName,
                                                                outFormat)
    os.system(shellcmd)
    #shutil.move(mfastaFolder + "/%s.dnd" % mfastaFileName.replace(".fasta", ""), outFolder)
    #
    # subprocess.call(["clustalw",
    #                 "-INFILE=", mfasta,
    #                 "-OUTFILE=", "%s/%s" % (outFolder, outMsaName),
    #                 "-OUTPUT=", outFormat
    #                 ], shell=False)
    return
    

# from Bio.Align.Applications import ClustalwCommandline
# cline = ClustalwCommandline(cmd="clustalw", infile="opuntia.fasta", outfile=)