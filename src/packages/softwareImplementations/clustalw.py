import subprocess
import os

def clustalw_getMultipleSequenceAlignementFrom(mfasta,
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
    subprocess.call(["clustalw",
                    "-INFILE=", mfasta,
                    "-OUTFILE=", "%s/%s" % (outFolder, outMsaName),
                    "-OUTPUT=", outFormat
                    ], shell=False)
    return
    