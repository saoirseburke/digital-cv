import streamlit as st  
from scipy.optimize import linprog

st.subheader("**Linear Programming applied to Real World Problem**")
st.markdown("---")

st.text("""
         Mazda Motor Corporation produces three models of its CX series: Mazda CX-3, Mazda CX-5, and Mazda CX-9
         Market projections indicate an expected monthly demand of at least: 3500 cars of the CX-3 model
         5000 cars of the CX-5 model and 2100 cars of the CX-9 model.
        
         Due to insufficient production capacity, no more than 4000 cars can be made of model CX-3 no more than 7000 cars
         can be made of model CX-5, and no more than 2500 cars can be made of model CX-9.
        
         Due to existing contracts with car dealers worldwide, a total of at least 12000 cars must be produced each month.
         Here is the financial result calculated as production costs – selling costs per model: 
         
         CX-3: EUR 3400 profit
         CX-5: EUR 2500 loss
         CX-9: EUR 7200 profit
         
         How many cars of each Mazda CX model should be produced monthly, so to maximize the total net profit?
         """)

st.subheader("This programming problem is linear. It has a linear function that needs to be maximised and the constraints are a mixture of linear and bounded constraints which are inequalities")

st.subheader("The objective is to maximise the total net profit: max [f], f = 3400\*x1 - 2500\*x2 + 7200\*x3")

obj = [-3400, 2500, -7200] #because linprog only works with minimization, we must minimise objective functions negative form

lhs_ineq = [[-1,-1,-1]] #Instead of having the greater than sign, multiply the coefficients the inequality by −1 to get the less than or equal to sign (≤)
rhs_ineq = [-12000]

x1_bound = (3500, 4000)
x2_bound = (5000, 7000)
x3_bound = (2100, 2500)
bnd = (x1_bound, x2_bound, x3_bound)

st.text("""
    obj = [-3400, 2500, -7200] 
    lhs_ineq = [[-1,-1,-1]]
    rhs_ineq = [-12000]
        
    x1_bound = (3500, 4000)
    x2_bound = (5000, 7000)
    x3_bound = (2100, 2500)
    bnd = (x1_bound, x2_bound, x3_bound)
    """)

opt_highs = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="highs")

st.subheader("Results of programmes execution")
st.write(opt_highs)

st.text("""
    x1 = 4000 : 4000 Mazda CX-3 models should be produced monthly to maximise the total
    net profit while satisfying the contraints

    x2 = 5500 : 5500 Mazda CX-5 models should be produced monthly to maximise the total
    net profit while satisfying the contraints

    x3 = 2500 : 2500 Mazda CX-9 models should be produced monthly to maximise the total 
    net profit while satisfying the contraints  
   
    max[f] = -3400(4000)+2500(5500)-7200(2500) = 17850000
    
    €17,850,000 is the total maximum net profit that can be achieved if
    4000 CX-3, 5500 CX-5 and 2500 CX-9 models of Mazda cars are produced monthly
    """)