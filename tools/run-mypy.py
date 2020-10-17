#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from typing import List

from zulint import lister

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(TOOLS_DIR))

sys.path.append(os.path.dirname(TOOLS_DIR))
from lib.test_script import assert_provisioning_status_ok

exclude = """
stubs/
""".split()

parser = argparse.ArgumentParser(description="Run mypy on files tracked by git.")
parser.add_argument('targets', nargs='*',
                    help="files and directories to check (default: .)")
parser.add_argument('--version', action='store_true',
                    help="show mypy version information and exit")
parser.add_argument('-m', '--modified', action='store_true',
                    help="check only modified files")
parser.add_argument('--scripts-only', action='store_true',
                    help="only check extensionless python scripts")
parser.add_argument('-a', '--all', action='store_true',
                    help="check all files, bypassing the default exclude list")
parser.add_argument('--force', action="store_true",
                    help="run tests despite possible provisioning problems")
parser.add_argument("--quiet", action="store_true",
                    help="suppress mypy summary output")
args = parser.parse_args()

assert_provisioning_status_ok(args.force)

command_name = "mypy"

# Use zulip-py3-venv's mypy if it's available.
VENV_DIR = "/srv/zulip-py3-venv"
MYPY_VENV_PATH = os.path.join(VENV_DIR, "bin", command_name)
if os.path.exists(MYPY_VENV_PATH):
    mypy_command = MYPY_VENV_PATH
else:
    mypy_command = command_name

if args.version:
    print("mypy command:", mypy_command)
    sys.exit(subprocess.call([mypy_command, "--version"]))

if args.all:
    exclude = []

# find all non-excluded files in current directory
files_dict = lister.list_files(
    targets=args.targets, ftypes=['py', 'pyi'],
    use_shebang=True, modified_only=args.modified,
    exclude=exclude, group_by_ftype=True,
    extless_only=args.scripts_only,
)
pyi_files = list(files_dict['pyi'])
python_files = [fpath for fpath in files_dict['py']
                if not fpath.endswith('.py') or fpath + 'i' not in pyi_files]
if not python_files and not pyi_files:
    print("There are no files to run mypy on.")
    sys.exit(0)

mypy_args: List[str] = []
if args.quiet:
    mypy_args += ["--no-error-summary"]
mypy_args += ["--", *python_files, *pyi_files]
rc = subprocess.call([mypy_command, *mypy_args])

if rc != 0:
    print("")
    print("See https://zulip.readthedocs.io/en/latest/testing/mypy.html for debugging tips.")

sys.exit(rc)

