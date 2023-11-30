import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy.stats import shapiro
from scipy.stats import ttest_1samp
import subprocess


st.subheader("**Statistical Analysis with R**")
st.markdown("---")

st.text("""

A randomised controlled trial was designed to assess the impact of an educational
programme on patients’ adherence to antihypertensive drugs. A sample of 190
hypertensive patients were randomly allocated to receive either special care
(the educational programme) or their usual care. Each patient’s adherence to
their antihypertensive drugs was recorded for six weeks. An adherence score
was then calculated for each patient. This score ranged from a possible minimum
of 0 (complete non-adherence) to a possible maximum of 100 (complete adherence).
The collected data are stored in the file “adherenceScore.csv”.
        
    Variable Description:
        
    Care Group (1 = Special Care, 2 = Usual Care)
        
    Age (in years)
    
    Gender (1 = Male, 2 = Female)
    
    Family Support (1 = Yes, 2 = No)
    
    Adherence Adherence score from 0 to 100.
        
        """)

adherence_dataset = "datasets/AdherenceScore.csv"
df = pd.read_csv(adherence_dataset)

st.write("Overview of the data")
st.dataframe(df.head(11))

st.text("Boxplot for Adherence Score")

fig, ax = plt.subplots(figsize=(10, 6))  
sns.boxplot(df['Adherence'])  
ax.set_title('Boxplot for Adherence Score')
ax.set_xlabel('Adherence Score')
st.pyplot(fig)

st.text("""
The median adherence score value is 43. By looking at the median line, we can see
the data for adherence score is slightly right skewed because the median line is
closer to the first quartile, or lower end of the box.

Summary statistics for adherence support this claim, As the mean is greater than
the median (43.8 > 43)
""")

adherence_summary = df["Adherence"].describe()

st.text("Summary Statistics for Adherence Score:")
st.table(adherence_summary)

st.text("""
It should also be noted that there is an outlier for adherence score. It is located
outside the whisker at the bottom of the box and has a value of around 10
        """)

st.text("Boxplot for Adherence Score by Family Support")

fig, ax = plt.subplots(figsize=(10, 6))  
sns.boxplot(x= "Family Support", y= "Adherence", data=df)  
ax.set_title('Boxplot for Adherence Score')
ax.set_ylabel("Adherence Score")
ax.set_xlabel("Family Support")
st.pyplot(fig)

st.write("---")

st.text("Looking at fund data")

fund_a = [0.5, 3.9, 6.3, 3.5, 4.2, 4.1, 4.1, 5.8, 3.2, 2.8, 3.3, 3.2]


fund_b = [6.5, 4.9, 4.3, 6.0, 5.6, 4.8, 6.0, 5.9, 6.4, 6.7]

df_fund_a = pd.DataFrame(fund_a)
df_fund_b = pd.DataFrame(fund_b)

fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(df_fund_a, bins=5, color='skyblue', edgecolor='black')
ax.set_title('Histogram of Fund A')
ax.set_xlabel('Annual Percentage Returns on Fund A')
ax.set_ylabel('Count')

# Show the plot in Streamlit
st.pyplot(fig)

st.text("""
Based on the shape of the histogram produced by, I do think the dataset
is drawn from a normal population. The graph has only one peak and is
slightly symmetrical on either side. A bell curve could be fitted to the
data. However, because the sample size is small (n=12), visual tests of
normality (Histogram and QQ-plot) cannot be relied on and a formal
statistical test like the Shapiro-Wilk Test or Kolmogorov-Smirnov Test
should be used to test for normality.
""")

st.subheader("Shapiro-Wilk Test of Normality on Fund B")

statistic, p_value = shapiro(df_fund_b)

st.write("Shapiro-Wilk Test Results for Fund B:")
st.write(f"Test Statistic: {statistic}")
st.write(f"P-value: {p_value}")

alpha = 0.05
if p_value > alpha:
    st.write("The data follows a normal distribution. As the p-value here is 0.4061 > 0.05 (5% level of significance) (fail to reject the null hypothesis)")
else:
    st.write("The data does not follow a normal distribution (reject the null hypothesis)")

st.subheader("1 sample t-test to determine whether the annual percentage return from Fund A exceeds 3%.")

t_statistic, p_value = ttest_1samp(df_fund_a, 3)

st.write("One-Sample t-Test Results:")
st.write(f"T-Statistic: {t_statistic}")
st.write(f"P-value: {p_value}")

# Interpret the results
if p_value < alpha and t_statistic > 0:
    st.write("The annual percentage return from Fund A is significantly different from 3% (reject the null hypothesis)")
else:
    st.write("There is not enough evidence to suggest that the annual percentage return from Fund A does not exceed 3% (fail to reject the null hypothesis)")

daytime_hours = {"Daytime Hours": [6.3, 4.2, 10.3, 7.1, 8.4, 9.5, 5.0, 3.5, 6.4]}
nighttime_hours = {"Night Time Hours": [9.4, 8.6, 6.3, 10.9, 5.5, 8.7, 9.8, 11.6, 7.7]}

df_daytime = pd.DataFrame(daytime_hours)
df_nighttime = pd.DataFrame(nighttime_hours)

fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(df_daytime['Daytime Hours'], df_nighttime['Night Time Hours'])
coefficients = np.polyfit(df_daytime['Daytime Hours'], df_nighttime['Night Time Hours'], 1)
trend_line = np.poly1d(coefficients)
trend_line_x = np.linspace(df_daytime['Daytime Hours'].min(), df_daytime['Daytime Hours'].max(), 100)
trend_line_y = trend_line(trend_line_x)
ax.plot(trend_line_x, trend_line_y, color='red', linestyle='-', label='Trend Line')

st.subheader("Activity of Dolphins in the the Daytime Compared to the Nightime")
ax.set_title('Scatterplot of Nighttime Hours vs. Daytime Hours')
ax.set_xlabel('Daytime Hours')
ax.set_ylabel('Night Time Hours')

st.pyplot(fig)

st.text("""
There is a negative trend in the data. We can infer from this trend that
as the number of hours spent sleeping in the day by dolphins increases,
the number of hours spent sleeping during the night-time decreases.
""")

st.subheader("Correlation Coefficient")
import numpy as np
y = [9.4, 8.6, 6.3, 10.9, 5.5, 8.7, 9.8, 11.6, 7.7]
x = [6.3, 4.2, 10.3, 7.1, 8.4, 9.5, 5.0, 3.5, 6.4]
r = np.corrcoef(x, y)
r
st.write("The Correlation Coefficient is -0.64")
st.text("""
-0.6464 indicates that there is a strong negative linear correlation between daytime hours
and night-time hours. Because the relationship is negative we can conclude there is an
inverse relationship meaning night-time hours spent sleeping tend to decrease as day-time
hours spent sleeping increases.
""")

st.subheader("Interpret the slope and intercept of the line")

daytime_hours = [6.3, 4.2, 10.3, 7.1, 8.4, 9.5, 5.0, 3.5, 6.4]
nighttime_hours = [9.4, 8.6, 6.3, 10.9, 5.5, 8.7, 9.8, 11.6, 7.7]

# Perform linear regression
coefficients = np.polyfit(daytime_hours, nighttime_hours, 1)
slope, intercept = coefficients

# Display the equation of the regression line
st.write(f"Equation of the Regression Line: y = {intercept:.2f} + {slope:.2f} * x")     
st.write("Where y = Night Time Hours and x = Daytime Hours")

# Interpret the slope and intercept
st.write(f"Slope (Effect of Daytime Sleep on Nighttime Sleep): {slope:.2f}")
st.write(f"Intercept: {intercept:.2f}")

st.text("""
The slope coefficient sign is negative, meaning that night-time hours spent
sleeping tend to decrease as day-time hours spent sleeping increases. Additionally, the
slope coefficient is -0.5542. This value indicates that if you increase daytime hours
by one hour, night-time hours spent sleeping decreases by an average of 0.5542 hours. 


The intercept in the regression equation indicates that the mean night-time hours spent
sleeping is 12.4603 when daytime hours equal zero. 
""")

st.subheader("Coefficient of Determination")

coefficients = np.polyfit(daytime_hours, nighttime_hours, 1)
slope, intercept = coefficients

# Calculate predicted values using the regression line
predicted_nighttime_hours = np.polyval(coefficients, daytime_hours)

# Calculate the coefficient of determination (R-squared)
r_squared = 1 - np.sum((nighttime_hours - predicted_nighttime_hours) ** 2) / np.sum((nighttime_hours - np.mean(nighttime_hours)) ** 2)

st.write(f"Coefficient of Determination (R-squared): {r_squared:.2f}")

st.text("""
The coefficient of determination is the correlation coefficient squared.
Therefore it is (-0.64)² = 0.4177.

We can also read this value from the above R output. This means that day-time
hours spent sleeping can explain 42% of the variation in night-time hours spent
sleeping. The remaining 58% of the variation is unaccounted for.

There are therefore other variables that affect night-time hours spent sleeping,
these could be factors such as time spent feeding or mating"
""")

st.subheader("We can also make predictions using the model")
predicted_nighttime_sleep = np.polyval(coefficients, 6)
st.write(f"If the dolphin sleeps for 6 hours during the day, it is predicted to sleep for {predicted_nighttime_sleep:.2f} hours during the night.")
st.write("Night-time = 12.4603 – 0.5542(6) = 9.135 = 9.135 night-time hours in a unihemispheric sleep state")

st.subheader("Residual for X=8.4")

predicted_nighttime_hours = np.polyval(coefficients, daytime_hours)

residuals = nighttime_hours - predicted_nighttime_hours

st.write("Residuals:")
st.write(residuals)

st.text("""
A residual is the difference between an observed value and the value
predicted by a regression model

X = 8.4 is the 5th value, therefore the residual for X = 8.4 is -2.3046.
Because the value is negative, this means the actual value is less than
the predicted value. 
""")