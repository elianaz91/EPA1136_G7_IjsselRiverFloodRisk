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
| Timon Otter               |                |



## Introduction

The repository contains a simulation of exploratory modelling and analysis of the Ijssel River exposed to flood risk. The model called Dike Model (dike_model) that implemented using the NetworkX framework. 

## Getting Started

To run the simulation, you will need to have Python 3.6 or higher installed, as well as the EMA Workbench and NetworkX as the main libraries. You can install these dependencies using pip, the Python package manager:
```
    pip install -r requirements.txt
```
Once you have installed the necessary dependencies, you can launch the open exploration by running the script:
```
    $ python MORDM_environmentalist_group_analyst.ipynb
```
To set up the open exploration, users must change [line 2]() for the problem formulation initialisation in `MORDM_environmentalist_group_analyst.ipynb`. `problem_formulation.py` provides more detail on the problem formulation options. The experiments and optimization will run for a default of 3 planning steps, with each tick representing planning steps. You can adjust the simulation parameters, such as the run scenarios, reference scenarios, and the number of function evaluations, by modifying the variables in the `MORDM_environmentalist_group_analyst.ipynb` script.

### Output
After the notebook run has been completed, the output is printed within the notebook. Additionally, complete CSV and tar.gz files can be found in the archive folder, while any figures can be found in the figure folder.

## Folder Structure

This folder contains the following folders and files.
The report in the report folder explains all of our analysis.
Before running the model, please look at the "README_model.md" in the model folder.

```
├── archive                                               <- Output files of the exploratory modelling and analysis.  
│                         
├── data                                                  <- The data for running the dike_model.                   
│
├── figure                                                <- Output pictures of the exploratory modelling and analysis.                   
│            
├── report                                                <- Our technical and political reflection report     
│
├── MORDM_environmentalist_group_analyst.ipynb            <- The open explorations script.
│
├── README.md                                             <- This file.
│
├── dike_model_function.py                                <- The primary model for the DikeNetwork, further defined as dike_model
│
├── dike_model_optimization.py                            <- Provide the directed search script.
│
├── dike_model_simulation.py                              <- Perform experiments based on the `problem_formulation.py`.
│
├── funs_dikes.py                                         <- Contains functions related to dike management and analysis.
|
├── funs_economy.py                                       <- Contains functions related to economic calculations for the measured investment.
│
├── funs_generate_network.py                              <- Contains functions to generate a network of dikes and related elements of the flood system.
|
├── funs_hydrostat.py                                     <- Contains functions to calculate hydrostatic calculations.
|
├── problem_formulation.py                                <- Setup specific problem formulation for open exploration using DikeNetwork class.
|
├── requirements.txt                                      <- The requirements file for reproducing the analysis environment.
│
            
```

### Acknowledgments
This simulation was created as part of a group assignment for the final project of EPA1361 Model-Based Decision Making.
