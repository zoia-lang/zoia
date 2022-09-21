#!/bin/python3
import re
from pathlib import Path

_ANTLR4_REGEX = re.compile(r'(?<!vendor\.)\bantlr4\b')

_SZ_ORIG_CODE = """    from . import sa_zoia_cpp_parser
except ImportError:"""
_SZ_PATCH_CODE = """    from . import sa_zoia_cpp_parser
    # Need to create entries in sys.modules for the C++ code to use
    vendor_strip = len('_vendor.')
    for module_name, module in list(sys.modules.items()):
        if module_name.startswith('_vendor.antlr4'):
            sys.modules[module_name[vendor_strip:]] = module
except ImportError:"""

_CPP_REPLACEMENTS = {
    # Add any future C++ replacements here
}

def main():
    curr_path = Path.cwd()
    src_path = curr_path.parent / 'src'
    if not src_path.is_dir():
        src_path = curr_path / 'src'
        if not src_path.is_dir():
            raise RuntimeError('Failed to find src path, run this script from '
                               'top level or from scripts folder')
    # Patch generated imports to use vendored dependencies
    print('Patching generated ANTLR code to use vendored ANTLR runtime')
    files_to_patch = list(src_path.glob('grammar/**/*.py'))
    for ftp in files_to_patch:
        with ftp.open('r', encoding='utf-8') as ins:
            ftp_contents = ins.read()
        if _ANTLR4_REGEX.search(ftp_contents):
            ftp_contents = _ANTLR4_REGEX.sub('_vendor.antlr4', ftp_contents)
        with ftp.open('w', encoding='utf-8') as out:
            out.write(ftp_contents)
    # Patch sa_zoia.py to hack sys.modules for the C++ code to use the vendored
    # copy of ANTLR
    print('Patching sa_zoia.py to add workaround for C++ code to use vendored '
          'ANTLR runtimem')
    sa_zoia = src_path / 'grammar' / 'sa_zoia.py'
    with sa_zoia.open('r', encoding='utf-8') as ins:
        sz_contents = ins.read()
    sz_contents = sz_contents.replace(_SZ_ORIG_CODE, _SZ_PATCH_CODE)
    with sa_zoia.open('w', encoding='utf-8') as out:
        out.write(sz_contents)
    # Patch C++ code (currently unused)
    def _cpp_patch(cpp_path):
        with cpp_path.open('r', encoding='utf-8') as ins:
            cpp_contents = ins.read()
        for target, sub in _CPP_REPLACEMENTS.items():
            cpp_contents = cpp_contents.replace(target, sub)
        with cpp_path.open('w', encoding='utf-8') as out:
            out.write(cpp_contents)
    # print('Patching C++ files to do X')
    # _cpp_patch(src_path / 'grammar' / 'cpp' / 'speedy_antlr.cpp')

if __name__ == '__main__':
    main()
