import os
import sys
import subprocess

sys.path.insert(0, os.path.dirname(__file__))

from common import *

def test_tes():
    subprocess.call(["rm", "-rf", "tests/test_tes/.snakemake"])
    subprocess.call(["rm", "-rf", "tests/test_tes/output.txt"])
    subprocess.call(["rm", "-rf", "tests/test_tes/output.txt.bz2"])
    workdir = dpath("test_tes")
    run(
        workdir,
        snakefile="Snakefile",
        tes=True,
        tes_url="http://localhost:8000",
        use_conda=True,
        conda_prefix="/tmp/conda",
        conda_frontend="conda",
        envvars=["HTTP_PROXY", "HTTPS_PROXY", "CONDA_PKGS_DIRS", "CONDA_ENVS_PATH"],
        no_tmpdir=True,
        cleanup=False
    )