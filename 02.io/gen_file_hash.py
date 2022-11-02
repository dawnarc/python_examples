
import os
import glob
import hashlib
import io
import sys

if __name__ == "__main__":
    dire = sys.argv[1]

    text = '<?xml version="1.0" ?>\n'
    text += f'<rcs root_path="{dire:s}">\n'
    files = glob.glob(dire + '/**/*', recursive=True)
    for file in files:
        if os.path.isfile(file):
            with open(file, "rb") as f:
                file_hash = hashlib.md5()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
            file_related = file.replace(dire + '\\', '')
            text += f'    <rc name="{file_related:s}" md5="{file_hash.hexdigest():s}" size="{os.path.getsize(file):d}"/>\n'
    text += '</rcs>'
    with io.open(dire + '/../manifest.xml', 'w', encoding = 'utf8') as f:
        f.write(text)   