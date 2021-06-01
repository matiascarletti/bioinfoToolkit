import os
from Bio import SeqIO


def getRvFastasWithPdbInfoFrom(rvMfasta, outFastaFolder):
    """
    Purpose: get the Revenant fastas with pdb structural information \
        from the mfasta get from Revenant Database. \
        The fastas will be named with the respective Rv Id
    
    Parameters:
    - rvMfasta       a str path to revenant multifasta
    - outFastaFolder a str path to outFolder to save te Revenant Fastas
    """
    try:
        os.makedirs(outFastaFolder)
    except FileExistsError:
        print("Folder already exist")
    rvMfastaIterator    = SeqIO.parse(rvMfasta, format="fasta")
    for rvSeqRecord in rvMfastaIterator:
        rvFastaHeader       = rvSeqRecord.description
        
        rvPdbInfoHeader     = rvFastaHeader.split("|")[1]
        
        rvPdbIdsHeader      = rvPdbInfoHeader.split(";")
        # Si hay un string vacio dentro de la lista significa que no hay Pdb Info
        # if "" not in rvPdbIdsHeader:
        # Si el campo de Pdb Info es un string vacío
        if rvPdbInfoHeader != "":
            rvPdbIdsNumber  = len(rvPdbIdsHeader)
            if rvPdbIdsNumber >= 1:
                # imprimo el fasta header para checkear los filtros
                print(rvFastaHeader)
                # guardo cada SeqRecord en un fasta individual nombrado con el Rv Id
                rvIdInfoHeader = rvFastaHeader.split("|")[0]
                SeqIO.write(sequences=rvSeqRecord, 
                            handle="%s/%s.fasta" % (outFastaFolder, rvIdInfoHeader), 
                            format="fasta")
    return