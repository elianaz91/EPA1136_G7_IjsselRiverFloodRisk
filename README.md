# README: Ijssel Flood Risk Model
# The Analyst of Environmentalist Group 
## EPA 11136 - Group 7

|           Name            | Student Number |
|:-------------------------:|:---------------|
|        Misa Aikawa        | 5750830        | 
| Almira Dilis Eliana Zelin | 5382866        |
|  Anna Dwita Paulus Sudin  | 5601215        |
|       Robin Müller        | 5633958        |
| Haekal Akbar Kartasasmita | 5450098        |


## Introduction

The repository contains a simulation of exploratory modelling and analysis of the Ijssel River that exposed with flood risk. The model called Dike Model (dike_model) that implemented using NetworkX framework. 

## Getting Started

To run the simulation, you will need to have Python 3.6 or higher installed, as well as the EMA Workbench and NetworkX as the main libraries. You can install these dependencies using pip, the Python package manager:
```
    pip install -r requirements.txt
```
Once you have installed the necessary dependencies, you can launch the model and run the simulation by executing the model_run.py script:
```
    $ python MORDM_environmentalist_group_analyst.ipynb
```
To set up the scenario, users must change [line 2]() for the problem formulation initialisation in `MORDM_environmentalist_group_analyst.ipynb`. `problem_formulation.py` provides more detail on the problem formulation options. The experiments and optimization will run for a default of 3 planning steps, with each tick representing planning steps. You can adjust the simulation parameters, such as the run scenarios, reference scenarios, and nfe by modifying the variables in the `1_Group 7_Environmentalist analyst.ipynb` script.

### Output
After the notebook run has completed, the output is printed within the notebook. Additionally, a complete csv and tar.gz files can be found in the archive folder while any figures can be found in the figure folder.

## Folder Structure

This folder contains following folders and files.
The report in Report folder explains all of our analysis.
Before trying to run the model, please have a look at the "README_model.md" in the model folder.

```
├── README.md         <- This file.
│
├── archive           <- Output files of the exploratory modelling and analysis.  
│                         
├── data              <- The data for running the dike_model.                   
│
├── figure            <- Output pictures of the exploratory modelling and analysis.                   
│            
├── report            <- Our report `EPA1352-G015-A3-Report.pdf`     
│
├── requirements.txt  <- The requirements file for reproducing the analysis environment.
│            
```

### Acknowledgments
This simulation was created as part of a group assignment of the final project of EPA1361 Model-Based Decision Making.
