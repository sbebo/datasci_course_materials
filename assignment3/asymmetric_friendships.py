import MapReduce
import sys

"""
Asymmetric Friendships Count
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    a = record[0]
    b = record[1]
    mr.emit_intermediate(a, record)
    mr.emit_intermediate(b, record)


def reducer(key, list_of_values):
    for (a,b) in list_of_values:
       if [b,a] not in list_of_values:
          if b == key:
             mr.emit((b,a))
          else:
             mr.emit((a,b))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
