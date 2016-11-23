import angr, logging
import pdb
import simuvex
import resource
import sys
import claripy

proj = angr.Project(sys.argv[1], load_options={'auto_load_libs': False})

start = 0x400576            # start of foobar
avoid = [0x4005d5]
end = 0x4005bc              # point that I want to reach

state = proj.factory.blank_state(addr=start, remove_options={simuvex.o.LAZY_SOLVES,})

a = state.regs.edi
b = state.regs.esi

pg = proj.factory.path_group(state, veritesting=False)

while len(pg.active) > 0:

    print pg

    # step 1 basic block for each active path 
    # if veritesting is on: this will step more than one 1 BB!
    pg.explore(avoid=avoid, find=end, n=1)

    # Bazinga!
    if len(pg.found) > 0:
        print "Reached the target"
        print pg
        state = pg.found[0].state
        print state.se.any_int(a)
        print state.se.any_int(b)
        break

print str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024) + " MB"
