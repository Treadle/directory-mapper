import os

depth = 0
last_folder_depth = []

def display(path):
  global depth
  
  try:
    files, folders = get_files_and_folders(path)
    depth += 1
    
    for f in range(len(files)):
      b = ((f == len(files)-1) and (len(folders) == 0))
      print(get_padding(b) + files[f])

    for f in range(len(folders)):
      if f == len(folders)-1:
        last_folder_depth.append(depth-1)

      print(get_padding(f == len(folders)-1) + folders[f])
      display(path + "\\" + folders[f])

    depth -= 1

    try:
      tar = last_folder_depth[-1]
      if tar == depth:
        last_folder_depth.pop(-1)
    except:
      pass

  except:
    pass

def get_padding(end):
  BLANK = "   "
  OUTER = "│  "
  INNER = "├──"
  ENDING = "└──"
  accumulator = ""

  last_segment = ENDING if end else INNER

  for i in range(depth-1):
    accumulator += OUTER if i not in last_folder_depth else BLANK
  accumulator += last_segment + " "
    
  return accumulator 

def get_files_and_folders(path):
  try:
    raw_items = os.listdir(path)
    
    files = [file for file in raw_items if os.path.isfile(os.path.join(path, file))]
    folders = [folder for folder in raw_items if os.path.isdir(os.path.join(path, folder))]

    return files, folders

  except Exception as e:
    print("Error getting files and folders:", e)

path = input("Enter absolute path: ")
display(path)