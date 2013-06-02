import MapReduce
import sys

"""
Join tables on order_id (position 1 in record)
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    table = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: order_id 
    # value: list of records with that order_id
    tuples = []
    for u in list_of_values:
       for v in list_of_values:
          if (u[0] == "order") and (v[0] == "line_item"):
             mr.emit(u+v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
