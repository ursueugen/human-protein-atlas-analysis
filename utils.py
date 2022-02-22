from pathlib import Path


class Paths:
    HPA_BASE_PATH = Path("/data/Human_Protein_Atlas")
    NORMAL_TISSUE_PATH = HPA_BASE_PATH / "normal_tissue.tsv"
    PROTEINATLAS_PATH = HPA_BASE_PATH / "proteinatlas.tsv"
    RNA_READCOUNTS_PATH = HPA_BASE_PATH / "rna_single_cell_read_count.tsv"
    RNA_TISSUES_PATH = HPA_BASE_PATH / "rna_single_cell_type_tissue.tsv"