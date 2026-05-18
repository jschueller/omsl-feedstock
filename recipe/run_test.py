import os
import subprocess
from pathlib import Path


def create_mos_file(mosfn, mofile=None, modelName=None, install_msl=False, load_msl=False):
    with open(mosfn, "w") as mos_file:
        if install_msl:
            # TODO: check if already installed
            mos_file.write('installPackage(Modelica, "3.2.3");')
            mos_file.write('getErrorString();')
        if load_msl:
            mos_file.write('loadModel(Modelica);\n')
            mos_file.write('getErrorString();')
        if mofile is not None:
            mos_file.write('loadFile("' + mofile + '");\n')
            mos_file.write('getErrorString();')
        if modelName is not None:
            mos_file.write('buildModel(' + modelName + ');\n')
            mos_file.write('getErrorString();')


def run_mos_file(mosfn):
    env = os.environ.copy()
    env["OPENMODELICALIBRARY"] = str(Path(env["PREFIX"]) / "lib" / "omlibrary")
    cp = subprocess.run("omc " + mosfn, shell=True, check=True, capture_output=True, env=env)
    return cp.stdout.decode()


def main():
    prefix = os.environ['PREFIX']
    msl_version = os.environ['PKG_VERSION']

    ok = (Path(prefix) / "lib" / "omlibrary" / (f"Modelica {msl_version}")).exists()
    assert ok, "did not find MSL directory - check recipe and build.sh"

    create_mos_file('load_msl.mos', load_msl=True)
    stdout = run_mos_file('load_msl.mos')
    assert len(stdout) > 0, "calling omc did not return anything"
    assert "true" in stdout, "loadModel(Modelica) did not succeed"


if __name__ == '__main__':
    main()
