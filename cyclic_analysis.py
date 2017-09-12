import pyansys
import sys


def main(argv):

  result = pyansys.ResultReader(argv[0])

  # Create an array of results (nnod x dof)
  disp = result.GetNodalResult(0) # uses 0 based indexing

  # which corresponds to the sorted node numbers from
  nnum = result.nnum

  # The same results can be plotted using

 # normalized displacement can be plotted by excluding the direction string
  result.PlotCyclicNodalResult(0, label='Normalized')

  # returns numpy matrix

  






if __name__ == "__main__":

  main(sys.argv[1:])
