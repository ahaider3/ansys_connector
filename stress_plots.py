import pyansys
import sys
import argparse

FLAGS=None

def main():
  input_path = FLAGS.input
  dim = FLAGS.dimension
  print(input_path)
  result = pyansys.ResultReader(input_path)

  # Create an array of results (nnod x dof)
  disp = result.GetNodalResult(0) # uses 0 based indexing

  nnum = result.nnum

  stress = result.NodalStress(0)

  print(result.GetTimeValues())


  






if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--input", type=str)
  parser.add_argument("--dimension", type=str)
  FLAGS = parser.parse_args()
  main()
