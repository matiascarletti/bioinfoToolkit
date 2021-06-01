import os
from Bio import SeqIO


def getRvIdWithPdbIdInfoListIteratorFrom(rvMfasta):
    """
    Purpose: get the Revenant Ids with pdb structural information \
        from the mfasta get from Revenant Database.
    
    Parameters:
    - rvMfasta       a str path to revenant multifasta
    """
    rvMfastaIterator    = SeqIO.parse(rvMfasta, format="fasta")
    rvSeqRecordList     = list(SeqIO.parse(rvMfasta, format="fasta"))
    
    rvIdsWithPdbInfoListIterator = list()
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
                # print(rvFastaHeader)
                # guardo cada SeqRecord en un fasta individual nombrado con el Rv Id
                rvIdInfoHeader = rvFastaHeader.split("|")[0]
                rvIdsWithPdbInfoListIterator.append(rvIdInfoHeader)

    rvIdsWithPdbInfoNumber  = len(rvIdsWithPdbInfoListIterator)
    rvSeqRecordNumber = len(rvSeqRecordList)
    print("There are ", 
            rvIdsWithPdbInfoNumber, 
            " Rv Ids with Pdb Info of a total of", 
            rvSeqRecordNumber, "Rv fastas")
    return rvIdsWithPdbInfoListIterator