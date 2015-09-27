# The space is a dict of mutually referential tasks using the same calendar.

import task
import networkx

class Space(dict):

 # nothing to do!
 def __init__(self):
  pass

 # create a new task with higher ID and passing on arguments
 def add(self,**kwargs):
  new_id = max ( [0] + list(self.keys()) ) + 1
  self [new_id] = task.Task(new_id,**kwargs)
  return new_id

 # return the subset of tasks that have specified parameters
 # boolean AND in effect here
 def find(self,**kwargs):

  # old code for finding those tasks which have only hashable contents
  #return [t for t in self if set(kwargs.items()).issubset(set(t.items())) ]

  # more general case
  found = set()
  named = set(kwargs.keys())
  for t_id in self.keys():
   match = True
   for name in named:
    if name not in self[t_id] or self[t_id][name] != kwargs[name]:
     match = False
     continue

   if match:
    found.add (t_id)
  return found


 # return the networkx version of self, for graph theoretic operations
 # when the cost of creating it on the fly becomes unbearable, look into persistent stores
 def nx(self):
  G = networkx.Graph()
  for t_id in self.keys():
   G.add_node (t_id)
  for t_id in self.keys():
   for dependency_id in self[t_id]['dependencies']:
    G.add_edge (t_id, dependency_id)
  return G

