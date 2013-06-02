import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
   # key: document identifier
   # value: document contents
   
   mat,i,j,value = record
   if mat == "a":
      for k in xrange(5):
         mr.emit_intermediate((i,k),(mat,j,value))
   else:
      for k in xrange(5):
         mr.emit_intermediate((k,j),(mat,i,value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for u in list_of_values:
      for v in list_of_values:
         if u[0] == "a" and v[0] == "b" and u[1]==v[1]:
            total += u[2]*v[2]
    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
