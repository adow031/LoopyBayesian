import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from probable import sumproduct, choose

def main():
    ######################## USER INPUT STARTS HERE ###########################

    # Specify the names of the nodes in the Bayesian network
    nodes=['Cloudy','Sprinkler','Rain','WetGrass']

    # Defining parents
    parents={}
    parents['Sprinkler']=['Cloudy']
    parents['Rain']=['Cloudy']
    parents['WetGrass']=['Sprinkler','Rain']
    
    # Define outcomes
    outcomes={}
    outcomes['Cloudy']=['T','F']
    outcomes['Sprinkler']=['T','F']
    outcomes['Rain']=['T','F']
    outcomes['WetGrass']=['T','F']

    # Set up conditional distribution structure
    dist={}
    dist['Cloudy'] = [0.5,0.5]
    dist['Sprinkler']={}
    dist['Sprinkler']['T']=[0.1,0.9]
    dist['Sprinkler']['F']=[0.5,0.5]
    dist['Rain']={}
    dist['Rain']['T']=[0.8,0.2]
    dist['Rain']['F']=[0.2,0.8]
    dist['WetGrass']={}
    dist['WetGrass']['T','T']=[0.99,0.01]
    dist['WetGrass']['T','F']=[0.9,0.1]
    dist['WetGrass']['F','T']=[0.9,0.1]
    dist['WetGrass']['F','F']=[0.0,1.0]

    # Specify any given information for each event The choose functions takes two arguments: an ordered list of outcomes, and the specified outcome name.
    # If you do not wish to specify the outcome, just use any name/number not in the list of outcomes as your choice.
    info={}
    choose(info,outcomes,'Cloudy','')
    choose(info,outcomes,'Sprinkler','')
    choose(info,outcomes,'Rain','')
    choose(info,outcomes,'WetGrass','')
    
    sumproduct(nodes,dist,parents,outcomes,info,100,0.0001)

######################### USER INPUT ENDS HERE ############################



if __name__ == "__main__":
    main()
