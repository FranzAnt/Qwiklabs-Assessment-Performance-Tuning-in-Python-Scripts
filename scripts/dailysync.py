#!/usr/bin/env python
import subprocess
import os

src = "./data/prod/"
dest = "./data/prod_backup/"

from multiprocessing import Pool
def run(task):
  print(task)
  # Do sonething with task here
  subprocess.call(task)
if __name__ == "__main__":
  tasks=[]

  for root , dirs , files  in os.walk("./data/prod/", topdown=False):
    for name in dirs:
      print(os.path.join(root, name))
      if(root is "./data/prod/"):
        task = ['rsync','-arq',src+name+"/",dest+name+"/"]
        tasks.append(task)
  
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)

