# adapted from https://www.biostars.org/p/380566/
import Bio
from Bio import PDB


def splitPdbModelIfNmrAndChainsFrom(pdb_id, work_dir):
    """
    
    """
    biopdb_name = '{0}/pdb{1}.ent'.format(work_dir, pdb_id.lower())
    ## Read the PDB file and extract the chain from structure[0]
    structure = PDB.PDBParser(PERMISSIVE=1,QUIET=1).get_structure(pdb_id, biopdb_name)
    for model in structure:
        # si tiene un solo modelo significa que != NMR
        if len(structure) == 1:
            for chain_id in model:
                # print(chain_id)
                io = PDB.PDBIO()
                # key error porque chain_id == <Chain id=A> y key debe ser "A"
                # io.set_structure(model[chain_id]) 
                io.set_structure(chain_id)
                chainIdName = str(chain_id).replace(">", "").split("=")[-1]
                io.save('{0}/{1}_{2}.pdb'.format(work_dir, pdb_id, chainIdName))
        # si no tiene un solo modelo significa que tiene más de uno == NMR
        else:
            for chain_id in model:
                io = PDB.PDBIO()
                # key error porque chain_id == <Chain id=A> y key debe ser "A"
                # io.set_structure(model[chain_id]) 
                io.set_structure(chain_id)
                chainIdName = str(chain_id).replace(">", "").split("=")[-1]
                modelName = str(model).replace(">", "").split("=")[-1]
                io.save('{0}/{1}_{2}-{3}.pdb'.format(work_dir, pdb_id, modelName, chainIdName))
    return