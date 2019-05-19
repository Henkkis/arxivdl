# Physics 0 [ 1 0 0 0 0 0]
# Mathematics 1 [ 0 1 0 0 0 0 ]
# Computer Science 2 [ 0 0 1 0 0 0]
# Quantative biology 3 [ 0 0 0 1 0 0]
# Quantative finance 4 [ 0 0 0 0 1 0]
# Statistic 5 [ 0 0 0 0 0 1]
import sys
simple ={}

simple["acc-phys"] = 0
simple["adap-org"] = 1
simple["alg-geom"] = 1
simple["astro-ph"] = 0
simple["atom-ph"] = 0
simple["chao-dyn"] =1
simple["chem-ph"] = 0
simple["cmp-lg"] = 2
simple["comp-gas"] = 1
simple["cond-mat"] = 0
simple["cs"] = 2
simple["dg-ga"] = 1
simple["econ"] = 4
simple["eess"] = 0
simple["funct-an"] = 1
simple["gr-qc"] = 0
simple["hep-ex"] = 0
simple["hep-lat"] = 0
simple["hep-ph"] = 0
simple["hep-th"] = 0
simple["math"] = 1
simple["math-ph"] = 1
simple["mtrl-th"] = 0
simple["nlin"] = 1
simple["nucl-ex"] = 0
simple["nucl-th"] = 0
simple["patt-sol"] = 1
simple["physics"] = 0
simple["q-alg"] = 1
simple["q-bio"] = 3
simple["q-fin"] = 4
simple["quant-ph"] = 0
simple["solv-int"] = 1
simple["stat"] = 5
simple["supr-con"] = 0


data_dir=sys.argv[1]

with open ("{}/categories.temp".format(data_dir), "r") as fh_in, open ("{}/categories.txt".format(data_dir),"w") as outF:
    # Read each line in loop
    for line in fh_in:
        outF.write(str(simple[line.rstrip()])+"\n")




