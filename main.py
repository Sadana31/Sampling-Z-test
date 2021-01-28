import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

# reading the file
df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

# getting the mean of the population
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

# getting the smaples and its mean
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("")
print("Standard deviation of sampling distribution:- ", std_deviation)
print("")

# calculating the 1st, 2nd and 3rd standard deviation
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

# calculating the sample mean
df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()
sample1_mean = statistics.mean(data)
print("Mean of sample1:- ",sample1_mean)
print("")

# plotting the graphs
fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist=False, show_rug=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sample1_mean, sample1_mean], y=[0, 0.17], mode="lines", name="MEAN OF PEOPLE WHO READ BOOKS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

# calculating the z-score
z_score = (mean - sample1_mean)/std_deviation
print("The z score is = ",z_score)
print("")

