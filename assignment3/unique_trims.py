import MapReduce
import sys

"""
Unique DNA Trims
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: record id
    # value: string
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value[:-10], None)

def reducer(key, list_of_values):
    # key: trimmed string
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
