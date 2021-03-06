# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:50:48 2019

@author: Raneem
"""
from optimizer_run import run

# Select optimizers
# "SSA","PSO","GA","BAT","FFA","GWO","WOA","MVO","MFO","CS"
optimizer=["SSA"]

# Select objective function
# "SSE","TWCV","SC","DB","DI"
objectivefunc=["SSE"] 

# Select data sets
#"aggregation","aniso","appendicitis","balance","banknote","blobs","Blood","circles","diagnosis_II","ecoli","flame","glass","heart","ionosphere","iris","iris2D","jain","liver","moons","mouse","pathbased","seeds","smiley","sonar","varied","vary-density","vertebral2","vertebral3","wdbc","wine"
dataset_List = ["iris"]

# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs are executed for each algorithm.
NumOfRuns=3

# Select general parameters for all optimizers (population size, number of iterations) ....
params = {'PopulationSize' : 20, 'Iterations' : 20}

#Export results?
export_flags = {'Export_avg':True, 'Export_details':True, 'Export_details_labels':True, 
'Export_convergence':True, 'Export_boxplot':True}

run(optimizer, objectivefunc, dataset_List, NumOfRuns, params, export_flags)