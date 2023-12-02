from baseBuilder import baseBuilder
from GPclass import GPclass
import pandas as pd
import os

if __name__ == "__main__":
    base = './../../Dataset'
    tosave = os.path.join(base, 'meaningfulSetsb')
    os.makedirs(tosave)
    
    files = [f for f in os.listdir(base) if f[0] == 'U']
    print(files)
    
    for f in files:
        df = pd.read_csv(os.path.join(base, f))
        bf = GPclass()
        # print(df.head())
        bf.ccrm("betweenness", df.values, VERBOSE=False)
        nodes = list(bf.graph.nodes)
        print(nodes)
        msbs = df.iloc[nodes, :]
        msbs.to_csv(os.path.join(tosave, 'r'+f))


        