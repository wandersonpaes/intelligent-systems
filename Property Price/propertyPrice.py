"""
Property Price Problem has two inputs, location and lenght.
Location is how close the property is to the center in meters (0 à 10.000) (near,medium,far).
Lenght is how big the property is in square meters (0 à 1.000) (small,medium,big).
The output is the property price in Reais (Brazilian Real) (0 à 1 million).
For price, is used five qualifiers (vey low, low, medium, high, very high).
"""

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#New Antecedent/Consequent objects hold universe variables and membership functions.
location = ctrl.Antecedent(np.arange(0, 10000, 1), 'location')
length = ctrl.Antecedent(np.arange(0, 1000, 1), 'length')
price = ctrl.Consequent(np.arange(0, 1000000, 1), 'price')

#Customizing the triangular function of the location.
location['near'] = fuzz.trimf(location.universe, [0, 0, 4000])
location['medium'] = fuzz.trimf(location.universe, [2500, 5000, 7500])
location['far'] = fuzz.trimf(location.universe, [6000, 10000, 10000])

#Customizing the triangular function of the length.
length['small'] = fuzz.trimf(length.universe, [0, 0, 400])
length['medium'] = fuzz.trimf(length.universe, [250, 500, 750])
length['big'] = fuzz.trimf(length.universe, [600, 1000, 1000])

#Customizing the triangular function of the price.
price['very low'] = fuzz.trimf(price.universe, [0, 0, 50000])
price['low'] = fuzz.trimf(price.universe, [0, 0, 400000])
price['medium'] = fuzz.trimf(price.universe, [250000, 500000, 750000])
price['high'] = fuzz.trimf(price.universe, [600000, 1000000, 1000000])
price['very high'] = fuzz.trimf(price.universe, [900000, 1000000, 1000000])

#Generating the graph of Antecedent/Consequent objects.
#location.view()
#length.view()
#price.view()

#Create the rules to make a relationship between inputs and output.
#For these exemple, consider nine simples rules.
rule1 = ctrl.Rule(location['near'] & length['small'], price['medium'])
rule2 = ctrl.Rule(location['near'] & length['medium'], price['high'])
rule3 = ctrl.Rule(location['near'] & length['big'], price['very high'])
rule4 = ctrl.Rule(location['medium'] & length['small'], price['low'])
rule5 = ctrl.Rule(location['medium'] & length['medium'], price['medium'])
rule6 = ctrl.Rule(location['medium'] & length['big'], price['high'])
rule7 = ctrl.Rule(location['far'] & length['small'], price['very low'])
rule8 = ctrl.Rule(location['far'] & length['medium'], price['low'])
rule9 = ctrl.Rule(location['far'] & length['big'], price['medium'])

#rule1.view()

"""
Control System Creation and Simulation.
------------------------------------------------------------
"""
#Create a control system.
propertyPrice_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

#Create a control system simulation that a object representing our 
#controller applied to a specific set of circumstances.
propertyPrice = ctrl.ControlSystemSimulation(propertyPrice_ctrl)

"""
To simulate the control system by simply specifying the inputs
and calling the compute method.
"""

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data).
propertyPrice.input['location'] = 50
propertyPrice.input['length'] = 500

# Crunch the numbers.
propertyPrice.compute()

#Once computed, we can view the result as well as visualize it.
print(propertyPrice.output['price'])
price.view(sim=propertyPrice)
plt.show()
