# rxnsmiles2rinchi

A Python wrapper for the IUPAC RInChI library, using ctypes.

## Install

```bash
pip install .
```

## Usage

```python
from rxnsmiles2rinchi import RInChI

rinchi_tool = RInChI()
rinchi, webrinchikey = rinchi_tool.rxn_smiles_to_rinchi_rinchikey("CC(=O)O.OCC>>CC(=O)OCC")
print(rinchi)
print(webrinchikey)
```