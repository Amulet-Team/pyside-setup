import glob
import os
import shutil

import PySide6
import shiboken6


def main() -> None:
    # Delete stubs
    stub_dir = os.path.dirname(__file__)
    for path in glob.glob(os.path.join(glob.escape(stub_dir), "*")):
        if os.path.isdir(path):
            shutil.rmtree(path)

    # Copy stubs
    for module_dir in (PySide6.__path__[0], shiboken6.__path__[0]):
        src_dir = os.path.dirname(module_dir)
        for src_path in glob.glob(os.path.join(glob.escape(module_dir), "**", "*.pyi"), recursive=True):
            rel_path = os.path.relpath(src_path, src_dir)
            dst_path = os.path.join(stub_dir, rel_path)
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copyfile(src_path, dst_path)


if __name__ == "__main__":
    main()
