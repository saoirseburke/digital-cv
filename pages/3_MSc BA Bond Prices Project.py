import streamlit as st  
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm, preprocessing

st.subheader("**Data Preprocessing and Training a Machine Learning Model: Predicting Bond Prices**")
st.markdown("---")

bonds_dataset = "/Users/saoirse/Desktop/datasets/trade_combined.csv"
df = pd.read_csv(bonds_dataset)

st.write("The first 10 rows of the dataset to give an idea of it")
st.dataframe(df.head(11))
st.dataframe(df.shape)
st.write("This is a large dataset with 20000 rows and 27 columns (or features). As seen below there is also a mixture of numeric and non-numeric (object) datatypes.")
st.dataframe(df.dtypes)
st.write("Supervised-Regression is the ML model that will be used on the dataset. This is the most appropriate model to use because the data is already labelled and regression is used because the target we are predicting is continuous values of bond price.")

st.subheader("Analysis of Current Bond Prices")
print(df['Price'].describe())

fig, ax = plt.subplots()
sns.kdeplot(df['Price'], ax=ax)
st.pyplot(fig)

st.write("The Price data is mostly concentrated around the 85 to 125 euro range")

st.subheader("Data Cleaning - Step 1 - Remove features with unique values for each row")

unique_values = df.nunique()
st.dataframe(unique_values)
st.write("As we can see no features have unique values for each row")

st.subheader("Step 2 - Remove features with one unique value for the entire dataset")

st.write("As we can see from the table of values above, there are 11 features with just one unique value")

st.subheader("Removing the unique values")

for column in df.columns:
    unique_values = df[column].unique()
    if len(unique_values) == 1:
        df.drop(column, axis=1, inplace=True)
        st.write(f"Column '{column}' has been removed from the dataset.")

st.subheader("Updated DataFrame")
st.dataframe(df.head(11))

st.subheader("Step 3 - Removing Null (NAN) values")

null_values = df.isnull().values.sum()
st.write("Total Null Values:", null_values)

null_value_list = df.isnull().sum()
st.write("List of Null Values by Feature:", null_value_list)

df = df[df['SecurityID'].notna()]
null_count = df['SecurityID'].isnull().sum()
st.write("Null values in 'SecurityID' column after removal:", null_count)

df = df[df['Price'].notna()]
null_count = df['Price'].isnull().sum()
st.write("Null values in 'Price' column after removal:", null_count)

df = df[df['Yield'].notna()]
null_count = df['Yield'].isnull().sum()
st.write("Null values in 'Yield' column after removal:", null_count)

df = df[df['DealerTraderID'].notna()]
null_count = df['DealerTraderID'].isnull().sum()
st.write("Null values in 'DealerTraderID' column after removal:", null_count)

null_value_list = df.isnull().sum()
st.write("Updated List with Null Values Removed:", null_value_list)

st.subheader("Data Transformation - Converting non-numeric features to numeric")

st.write("There are 7 non-numeric features")
non_numeric = df.select_dtypes(exclude = ['number']) 
st.dataframe(non_numeric)

df['MaturityDate'] = pd.to_datetime(df['MaturityDate']).dt.strftime("%Y%m%d").astype(int)
df['IssueDate'] = pd.to_datetime(df['IssueDate']).dt.strftime("%Y%m%d").astype(int)
df['SettlDate'] = pd.to_datetime(df['SettlDate']).dt.strftime("%Y%m%d").astype(int)
df['TransactTime'] = pd.to_datetime(df['TransactTime']).dt.strftime("%Y%m%d").astype(int)

class_mapper = {'BUY':1, 'SELL':2}
df['Side'] = df['Side'].replace(class_mapper)

security_type_values = df['SecurityType'].unique()
print(security_type_values)

class_mapper = {}
num = 0
for element in security_type_values:
    num += 1
    class_mapper[element] = num

df['SecurityType'] = df['SecurityType'].replace(class_mapper)

symbol_values = df['Symbol'].unique()
print(symbol_values)

class_mapper = {}
num = 0
for element in symbol_values:
    num += 1
    class_mapper[element] = num

df['Symbol'] = df['Symbol'].replace(class_mapper)

st.write("After converting to numeric:")
st.dataframe(df.head(11))

st.subheader("Step 4 - Model Training and Testing")

st.write("Because I pick the Supervised Regression ML algorithm, I will use sklearn.ensemble package and import RandomForestRegressor")

from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

st.subheader("Training the Model")
st.subheader("X - Dataset (Excluding Price)")

X = df.drop(axis=1, labels='Price')

st.dataframe(X)

st.subheader("Y - Price feature only")

Y = df["Price"]

st.dataframe(Y)

st.subheader("Slicing the Dataset")

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=0)

X_train

Y_train

from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Combine X_train and X_test for label encoding
combined_data = pd.concat([X_train, X_test], axis=0)

# Identify categorical columns
categorical_cols = combined_data.select_dtypes(include=['object']).columns

# Use LabelEncoder to convert categorical columns to numeric values
label_encoder = LabelEncoder()
for col in categorical_cols:
    combined_data[col] = label_encoder.fit_transform(combined_data[col])

# Split the combined data back into X_train and X_test
X_train = combined_data.iloc[:len(X_train), :]
X_test = combined_data.iloc[len(X_train):, :]

# Now apply MinMaxScaler
scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X_train)
X_train = scaling.transform(X_train)
X_test = scaling.transform(X_test)

st.write( """ # Code used in train, test, split
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

st.subheader("Training the Model")
st.subheader("X - Dataset (Excluding Price)")

X = df.drop(axis=1, labels='Price')
st.dataframe(X)

st.subheader("Y - Price feature only")
Y = df["Price"]
st.dataframe(Y)

st.subheader("Slicing the Dataset")

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=0)

X_train
Y_train

from sklearn.preprocessing import MinMaxScaler, LabelEncoder

combined_data = pd.concat([X_train, X_test], axis=0)

categorical_cols = combined_data.select_dtypes(include=['object']).columns

label_encoder = LabelEncoder()
for col in categorical_cols:
    combined_data[col] = label_encoder.fit_transform(combined_data[col])

X_train = combined_data.iloc[:len(X_train), :]
X_test = combined_data.iloc[len(X_train):, :]

scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X_train)
X_train = scaling.transform(X_train)
X_test = scaling.transform(X_test)
         """)

rf_regressor = RandomForestRegressor (n_estimators=100)
rf_regressor.fit(X_train, Y_train)

Y_pred = rf_regressor.predict(X_test)
from sklearn import metrics


st.subheader("Testing the strength of the Regression model")
st.write("This model has a 99% accuracy in predicting bond prices")
r2_score = metrics.r2_score(Y_test, Y_pred)
st.text("R-squared Score: {}".format(r2_score))


st.subheader("Plotting actual bond prices and predicted bond prices")
import seaborn as sns
sns.regplot(x=Y_test,y=Y_pred,ci=None,color ='red')
st.pyplot(plt)


