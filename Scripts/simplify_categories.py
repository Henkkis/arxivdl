# Physics 1 [ 1 0 0 0 0 0]
# Mathematics 2 [ 0 1 0 0 0 0 ]
# Computer Science 3 [ 0 0 1 0 0 0]
# Quantative biology 4 [ 0 0 0 1 0 0]
# Quantative finance 5 [ 0 0 0 0 1 0]
# Statistic 6 [ 0 0 0 0 0 1]
import sys
simple ={}

simple["acc-phys"] = 1
simple["adap-org"] = 2
simple["alg-geom"] = 2
simple["astro-ph"] = 1
simple["atom-ph"] = 1
simple["chao-dyn"] =2
simple["chem-ph"] = 1
simple["cmp-lg"] = 3
simple["comp-gas"] = 2
simple["cond-mat"] = 1
simple["cs"] = 3
simple["dg-ga"] = 2
simple["econ"] = 5
simple["eess"] = 1
simple["funct-an"] = 2
simple["gr-qc"] = 1
simple["hep-ex"] = 1
simple["hep-lat"] = 1
simple["hep-ph"] = 1
simple["hep-th"] = 1
simple["math"] = 2
simple["math-ph"] = 2
simple["mtrl-th"] = 1
simple["nlin"] = 2
simple["nucl-ex"] = 1
simple["nucl-th"] = 1
simple["patt-sol"] = 2 
simple["physics"] = 1
simple["q-alg"] = 2
simple["q-bio"] = 4
simple["q-fin"] = 5
simple["quant-ph"] = 1 
simple["solv-int"] = 2
simple["stat"] = 6
simple["supr-con"] = 1


data_dir=sys.argv[1]

with open ("{}/categories.temp".format(data_dir), "r") as fh_in, open ("{}/categories.txt".format(data_dir),"w") as outF:
    # Read each line in loop
    for line in fh_in:
        outF.write(str(simple[line.rstrip()])+"\n")




