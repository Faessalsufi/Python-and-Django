from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")

# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime))

# open("__init__.py","r")
# with open ("__init__.py","r") as file:

# path.read_bytes()
print(path.read_text()) # without open and close

# path.write_text(".....")
# path.write_bytes()


source = Path("ecommerce/__init__.py")

target = Path()/ "__init__.py"


#* copt the file 
# target.write_text(source.read_text())


shutil.copy(source,target)