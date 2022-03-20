import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from probable import sumproduct, choose

def main():
    ######################## USER INPUT STARTS HERE ###########################

    # Specify the names of the nodes in the Bayesian network
    nodes=['B','E','A','J','M']

    # Defining parents
    parents={}
    parents['A']=['B','E']
    parents['J']=['A']
    parents['M']=['A']
    
    # Define outcomes
    outcomes={}
    outcomes['B']=['T','F']
    outcomes['E']=['T','F']
    outcomes['A']=['T','F']
    outcomes['J']=['T','F']
    outcomes['M']=['T','F']

    # Set up conditional distribution structure
    dist={}
    dist['B'] = [0.001,0.999]
    dist['E'] = [0.002,0.998]
    dist['A']={}
    dist['A']['T','T']=[0.95,0.05]
    dist['A']['T','F']=[0.94,0.06]
    dist['A']['F','T']=[0.29,0.71]
    dist['A']['F','F']=[0.001,0.999]
    dist['J']={}
    dist['J']['T']=[0.9,0.1]
    dist['J']['F']=[0.05,0.95]
    dist['M']={}
    dist['M']['T']=[0.7,0.3]
    dist['M']['F']=[0.01,0.99]

    # Specify any given information for each event The choose functions takes two arguments: an ordered list of outcomes, and the specified outcome name.
    # If you do not wish to specify the outcome, just use any name/number not in the list of outcomes as your choice.
    info={}
    choose(info,outcomes,'B','')
    choose(info,outcomes,'E','')
    choose(info,outcomes,'A','')
    choose(info,outcomes,'J','')
    choose(info,outcomes,'M','')
    
    sumproduct(nodes,dist,parents,outcomes,info,100,0.0001)

######################### USER INPUT ENDS HERE ############################



if __name__ == "__main__":
    main()
