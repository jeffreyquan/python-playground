import shutil
import os

# copies files that end with .jpg into destination folder

def copy_files(dir, dest):
  subdirs = [x[0] for x in os.walk(dir)]
  for subdir in subdirs:
    files = os.walk(subdir).__next__()[2]
    if (len(files) > 0):
      for file in files:
        if file.endswith("jpg"):
          shutil.copy(subdir + "/" + file, dest)

