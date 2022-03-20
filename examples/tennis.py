import numpy as np
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from probable import sumproduct, choose

def main():
    ######################## USER INPUT STARTS HERE ###########################

    # Specify the names of the nodes in the Bayesian network
    nodes=['S1','P1','P2','P3','P4','P5','G1']

    # Defining parents
    parents={}
    parents['P1']=['S1']
    parents['P2']=['S1']
    parents['P3']=['S1']
    parents['P4']=['S1']
    parents['P5']=['S1']
    parents['G1']=['P1','P2','P3','P4','P5']
    
    pWS=0.7
    pWR=0.35

    # Define outcomes
    outcomes={}
    outcomes['S1']=["Player1Serves","Player2Serves"]
    outcomes['P1']=[1,2]
    outcomes['P2']=[1,2]
    outcomes['P3']=[1,2]
    outcomes['P4']=[1,2]
    outcomes['P5']=[1,2]
    outcomes['G1']=[1,2]

    # Set up conditional distribution structure
    dist={}
    dist['S1'] = [0.5,0.5]

    dist['P1']={}
    dist['P2']={}
    dist['P3']={}
    dist['P4']={}
    dist['P5']={}

    dist['P1']["Player1Serves"]=[pWS,1-pWS]
    dist['P2']["Player1Serves"]=[pWS,1-pWS]
    dist['P3']["Player1Serves"]=[pWS,1-pWS]
    dist['P4']["Player1Serves"]=[pWS,1-pWS]
    dist['P5']["Player1Serves"]=[pWS,1-pWS]
    dist['P1']["Player2Serves"]=[pWR,1-pWR]
    dist['P2']["Player2Serves"]=[pWR,1-pWR]
    dist['P3']["Player2Serves"]=[pWR,1-pWR]
    dist['P4']["Player2Serves"]=[pWR,1-pWR]
    dist['P5']["Player2Serves"]=[pWR,1-pWR]

    dist['G1']={}
    dist['G1'][1,1,1,1,1]=[1,0] #you could also use: choose(outcomes['G1'],1)
    dist['G1'][1,1,1,1,2]=[1,0]
    dist['G1'][1,1,1,2,1]=[1,0]
    dist['G1'][1,1,1,2,2]=[1,0]
    dist['G1'][1,1,2,1,1]=[1,0]
    dist['G1'][1,1,2,1,2]=[1,0]
    dist['G1'][1,1,2,2,1]=[1,0]
    dist['G1'][1,1,2,2,2]=[0,1]    
    dist['G1'][1,2,1,1,1]=[1,0]
    dist['G1'][1,2,1,1,2]=[1,0]
    dist['G1'][1,2,1,2,1]=[1,0]
    dist['G1'][1,2,1,2,2]=[0,1]
    dist['G1'][1,2,2,1,1]=[1,0]
    dist['G1'][1,2,2,1,2]=[0,1]
    dist['G1'][1,2,2,2,1]=[0,1]
    dist['G1'][1,2,2,2,2]=[0,1]
    dist['G1'][2,1,1,1,1]=[1,0]
    dist['G1'][2,1,1,1,2]=[1,0]
    dist['G1'][2,1,1,2,1]=[1,0]
    dist['G1'][2,1,1,2,2]=[0,1]
    dist['G1'][2,1,2,1,1]=[1,0]
    dist['G1'][2,1,2,1,2]=[0,1]
    dist['G1'][2,1,2,2,1]=[0,1]
    dist['G1'][2,1,2,2,2]=[0,1]    
    dist['G1'][2,2,1,1,1]=[1,0]
    dist['G1'][2,2,1,1,2]=[0,1]
    dist['G1'][2,2,1,2,1]=[0,1]
    dist['G1'][2,2,1,2,2]=[0,1]
    dist['G1'][2,2,2,1,1]=[0,1]
    dist['G1'][2,2,2,1,2]=[0,1]
    dist['G1'][2,2,2,2,1]=[0,1]
    dist['G1'][2,2,2,2,2]=[0,1]    
   
    # Specify any given information for each event The choose functions takes two arguments: an ordered list of outcomes, and the specified outcome name.
    # If you do not wish to specify the outcome, just use any name/number not in the list of outcomes as your choice.
    info={}
    choose(info,outcomes,'S1',"Player2Serves")
    choose(info,outcomes,'P1',1)
    choose(info,outcomes,'P2',0)
    choose(info,outcomes,'P3',0)
    choose(info,outcomes,'P4',0)
    choose(info,outcomes,'P5',0)
    choose(info,outcomes,'G1',0)
    
    sumproduct(nodes,dist,parents,outcomes,info,100,0.0001)

######################### USER INPUT ENDS HERE ############################



if __name__ == "__main__":
    main()
