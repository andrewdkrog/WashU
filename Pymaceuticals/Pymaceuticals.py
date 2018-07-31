
# Dependencies and Setup
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "./Resources/mouse_drug_data.csv"
clinical_trial_data_to_load = "./Resources/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_clinicals = pd.read_csv(mouse_drug_data_to_load)
drug_clinicals = pd.read_csv(clinical_trial_data_to_load)

# Combine the data into a single dataset
mouse_drug_clinicals = pd.merge(mouse_clinicals, drug_clinicals, on="Mouse ID", how="left")

# Display the data table for preview
mouse_drug_clinicals.head()

## Tumor Response to Treatment

# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
mean_tumor_vol = mouse_drug_clinicals.groupby(["Drug", "Timepoint"]).mean()["Tumor Volume (mm3)"]

# Convert to DataFrame
mean_tumor_vol = pd.DataFrame(mean_tumor_vol)
# Preview DataFrame
mean_tumor_vol.head()

# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
sem_tumor_vol = mouse_drug_clinicals.groupby(["Drug", "Timepoint"]).sem()["Tumor Volume (mm3)"]

# Convert to DataFrame
sem_tumor_vol = pd.DataFrame(sem_tumor_vol)

# Preview DataFrame
sem_tumor_vol.head()

# Minor Data Munging to Re-Format the Data Frames
mean_tumor_vol = mean_tumor_vol.reset_index()
sem_tumor_vol = sem_tumor_vol.reset_index()

# Preview that Reformatting worked
sem_tumor_vol.head()

# Change mean tumor volume dataframe from long to wide format
mean_tumor_wide = mean_tumor_vol.pivot(index = "Timepoint", columns = "Drug", values = "Tumor Volume (mm3)")
sem_tumor_wide = sem_tumor_vol.pivot(index = "Timepoint", columns = "Drug", values = "Tumor Volume (mm3)")

mean_tumor_wide.head()

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

for column in mean_tumor_wide:
    ax.errorbar(x = mean_tumor_wide.index, y = mean_tumor_wide[column], yerr = sem_tumor_wide[column], fmt = 'o-')
    
plt.title("Tumor Size over Time by Treatment", size = 22)
plt.ylabel("Tumor Size (mm3)", size = 15)
plt.xlabel("Timepoint", size = 15)
plt.legend(loc = 'upper left', fontsize = 15)
plt.grid()
plt.rcParams.update({'font.size': 20})

# Save picture
plt.savefig('Tumor Size over Time')

# Show the Figure
plt.show()

## Metastatic Response to Treatment

# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
mean_metastatic = mouse_drug_clinicals.groupby(["Drug", "Timepoint"]).mean()["Metastatic Sites"]

# Convert to DataFrame
mean_metastatic = pd.DataFrame(mean_metastatic)

# Preview DataFrame
mean_metastatic.head()



# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
sem_metastatic = mouse_drug_clinicals.groupby(["Drug", "Timepoint"]).sem()["Metastatic Sites"]

# Convert to DataFrame
sem_metastatic = pd.DataFrame(sem_metastatic)

# Preview DataFrame
sem_metastatic.head()




# Minor Data Munging to Re-Format the Data Frames
mean_metastatic_wide = mean_metastatic.reset_index().pivot(index = "Timepoint", columns = "Drug", values = "Metastatic Sites")
sem_metastatic_wide = sem_metastatic.reset_index().pivot(index = "Timepoint", columns = "Drug", values = "Metastatic Sites")

# Preview wide format
mean_metastatic_wide.head()

# Generate plot
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

for column in mean_metastatic_wide:
    ax.errorbar(x = mean_metastatic_wide.index, y = mean_metastatic_wide[column], yerr = sem_metastatic_wide[column], fmt = 'o-')
    
plt.title("Metastatic Sites over Time by Treatment", size = 22)
plt.ylabel("Metastatic Sites", size = 15)
plt.xlabel("Treatment Duration (Days)", size = 15)
plt.legend(loc = 'upper left', fontsize = 15)
plt.grid()
plt.rcParams.update({'font.size': 20})

# Save picture
plt.savefig('Metastatic Sites')

plt.show()

## Survival Rates

# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mouse_count = mouse_drug_clinicals.groupby(["Drug", "Timepoint"]).count()["Mouse ID"]

# Convert to DataFrame
mouse_count = pd.DataFrame(mouse_count)
# Preview DataFrame
mouse_count.head()

# Minor Data Munging to Re-Format the Data Frames
mouse_count_wide = mouse_count.reset_index().pivot(index = "Timepoint", columns = "Drug", values = "Mouse ID")

# Preview wide format
mouse_count_wide.head()

# Create new pandas dataframe of the survival rate of mice using the starting number of mice per drug
mouse_survival = mouse_count_wide.div(mouse_count_wide.iloc[0])*100

# Generate plot
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)

for column in mouse_count_wide:
    ax.errorbar(x = mouse_survival.index, y = mouse_survival[column], fmt = 'o-')
 
plt.title("Survival During Treatment", size = 22)
plt.ylabel("Survival Rate (%)", size = 15)
plt.xlabel("Time (Days)", size = 15)
plt.legend(loc = 'lower left', fontsize = 15)
plt.grid()
plt.rcParams.update({'font.size': 20})

# Save picture
plt.savefig('Survival Rate')

plt.show()

## Summary Bar Graph

# Calculate the percent changes for each drug
tumor_growth_rates = (mean_tumor_wide.iloc[-1]/mean_tumor_wide.iloc[0] - 1)*100

# Display the data to confirm
print(tumor_growth_rates)

# Store all Relevant Percent Changes into a Tuple
tumor_growth = pd.DataFrame(tumor_growth_rates)
tumor_growth.columns = ['Growth Rate']
growth_rates = tuple(tumor_growth['Growth Rate'])

# Splice the data between passing and failing drugs
bins = [-100, 0, 100]
group_names = ['Pass', 'Fail']

tumor_growth["Pass"] = pd.cut(tumor_growth['Growth Rate'], bins, labels = group_names)

# Create a list of colors: green = drugs that pass, red = failures
my_color = []
for rate in tumor_growth['Growth Rate']:
    if rate < 0:
        color = 'g'
        my_color.append(color)
    else:
        color = 'r'
        my_color.append(color)

# Orient widths. Add labels, tick marks, etc.
fig = plt.figure()
ax = tumor_growth['Growth Rate'].plot(kind = 'bar', figsize = (15, 10),
                                     color = my_color)

# Label chart and y-axis
ax.set_title('Tumor Growth Rate by Drug')
plt.ylabel('Tumor Growth Rate (%)')

# Rotate drug labels so you can read them
plt.xticks(rotation=90)

# Create thick black line for x-axis
ax.axhline(linewidth=4, color='black')

# Create auto_label function to put label on each bar halfway up/down
def auto_label(ax):
    for i in ax.patches:
            ax.text(i.get_x()-.03, i.get_height()/2, \
                str(round(i.get_height(),0)))

# Use auto_label function to label each bar            
auto_label(ax)            
            
# Create grid with gray dashed lines and make grid appear behind bars
plt.grid()
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# Autoscale the view
ax.autoscale_view()

# Plot
fig.show()

# Save the Figure
fig.savefig('Tumor Growth Rate')


