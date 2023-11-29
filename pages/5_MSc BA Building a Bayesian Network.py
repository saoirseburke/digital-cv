import streamlit as st
from pgmpy.estimators import ParameterEstimator
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.estimators import ParameterEstimator
from pgmpy.estimators import BayesianEstimator
from pgmpy.estimators import K2Score
from pgmpy.inference import VariableElimination
from pgmpy.sampling import BayesianModelSampling
import pandas as pd
import numpy as np
from pgmpy.models import BayesianModel
import matplotlib.pyplot as plt
import networkx as nx

st.subheader("Building a Bayesian Network on a Real-Life Scenario", divider="rainbow")

st.text("""Let’s suppose that a UL student is taking the CS6501 module “Machine Learning and Applications”
        The student’s grade for this module will depend on their intelligence (low or high),
        module difficulty (easy, hard), and their health status (sick or healthy).
        Our student asks their professor for a recommendation letter.
        To come up with the idea of the quality of that recommendation letter (weak or strong),
        the professor can only look at the student’s grade (A, B or C) and the student’s forum activity
        (not active, active). Hence, the actual quality of the letter depends stochastically on the grade
        and on the forum activity
        """)

st.subheader("Random Variables and their Domains and the Dependancies between these Random Variables")

st.text("""Random Variables and Domains:
        
Intelligence (I): Domain: {low, high}

Module Difficulty (D): Domain: {easy, hard}

Health Status (H): Domain: {sick, healthy}

Grade (G): Domain: {A, B, C}
Forum Activity (F): Domain: {not active, active}

Recommendation Letter Quality (R): Domain: {weak, strong}
 """)

st.write("---")
st.text("""
Intelligence and Module Difficulty:
Both influence the Grade.
No direct dependency between Intelligence and Module Difficulty.

Health Status:
Influences both Grade and Forum Activity.

Grade:
Influenced by both Intelligence, Module Difficulty, and Health Status.

Forum Activity:
Influenced by Health Status.

Recommendation Letter Quality:
Depends on Grade and Forum Activity.
        """)



# Define the structure of the Bayesian network
model = BayesianModel([('Intelligence', 'Grade'),
                       ('Module Difficulty', 'Grade'),
                       ('Health Status', 'Grade'),
                       ('Health Status', 'Forum Activity'),
                       ('Grade', 'Recommendation Letter Quality'),
                       ('Forum Activity', 'Recommendation Letter Quality')])

# Plot the DAG
pos = nx.circular_layout(model.nodes())
fig, ax = plt.subplots()
nx.draw(model, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", arrows=False)
plt.title("Bayesian Network DAG")
st.pyplot(fig)


data = pd.DataFrame({
    'Intelligence': ['low', 'high', 'low', 'high'],
    'Module Difficulty': ['easy', 'easy', 'hard', 'hard'],
    'Health Status': ['sick', 'healthy', 'sick', 'healthy'],
    'Grade': ['A', 'B', 'C', 'D'],
    'Forum Activity': ['not active', 'active', 'not active', 'active'],
    'Recommendation Letter Quality': ['weak', 'strong', 'weak', 'strong']
})

