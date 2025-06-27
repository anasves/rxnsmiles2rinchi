from rxnsmiles2rinchi import RInChI

def test_basic_conversion():
    rinchi_tool = RInChI()
    rinchi, webrinchikey = rinchi_tool.rxn_smiles_to_rinchi_rinchikey("CC(=O)O.OCC>>CC(=O)OCC")
    assert rinchi is not None
    assert webrinchikey is not None