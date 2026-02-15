
# Scientific Python Starter Quest
# Name: Chhimi Dorji  
# Course: M.Sc Physics  

# This notebook contains beginner-level scientific Python tools including plasma classification, material lookup, and particle energy calculator.

## PART B - Core Python Coding Challenges 
#--------------------------------------------
# Task 1 – Plasma Temperature Classifier
#--------------------------------------------
def classify_plasma_temp(temp):
    if temp < 1e4:
        return "Cold plasma"
    elif 1e4 <= temp <= 1e6:
        return "Warm plasma"
    else:
        return "Hot plasma"
    
results = []
for i in range(5):
    try:
        temp = float(input("Enter plasma temperature in Kelvin: "))
        category = classify_plasma_temp(temp)
        results.append((temp, category))
    except:
        print("Invalid input. Please enter a number.")

print("\nPlasma Temperature Classification")
print("----------------------------------")

for temp, category in results:
    print(f"{temp} K --> {category}")
    
# Temperature classification is important in plasma physics because different temperature ranges behave differently. Cold plasma is used in medical and surface applications, while hot plasma appears in stars and fusion experiments.

#----------------------------------------
# Task 2 – Material Properties Lookup
#----------------------------------------
materials = {
    "Aluminum": {"density_g_cm3": 2.7, "conductivity": 3.5e7, "youngs_modulus_GPa": 70},
    "Copper": {"density_g_cm3": 8.96, "conductivity": 5.96e7, "youngs_modulus_GPa": 110},
    "Silicon": {"density_g_cm3": 2.33, "conductivity": 1e-3, "youngs_modulus_GPa": 130},
    "Graphene": {"density_g_cm3": 2.2, "conductivity": 1e8, "youngs_modulus_GPa": 1000}
}

def add_material(name, density, conductivity, youngs):
    materials[name] = {
        "density_g_cm3": density,
        "conductivity": conductivity,
        "youngs_modulus_GPa": youngs
    }
add_material("Iron", 7.87, 1e7, 200)

def highest_conductivity():
    max_material = max(materials, key=lambda x: materials[x]["conductivity"])
    return max_material

print("Highest conductivity:", highest_conductivity())
density_list = [materials[m]["density_g_cm3"] for m in materials]
print("Densities:", density_list)

# Dictionaries help organize experimental data because each material can store multiple properties in one structured format. This makes data easy to update and search.

#----------------------------------------
# Task 3 – Particle Energy Calculator using OOP
#----------------------------------------
class Particle:
    def __init__(self, name, mass_kg, velocity_m_s):
        self.name = name
        self.mass = mass_kg
        self.velocity = velocity_m_s
    
    def kinetic_energy(self):
        return 0.5 * self.mass * self.velocity**2


electron = Particle("Electron", 9.11e-31, 2e6)
proton = Particle("Proton", 1.67e-27, 1e5)
alpha = Particle("Alpha Particle", 6.64e-27, 5e4)

particles = [electron, proton, alpha]

for p in particles:
    energy_joule = p.kinetic_energy()
    energy_ev = energy_joule / 1.6e-19
    print(f"{p.name} Energy = {energy_ev} eV")

class Particle:
    def __init__(self, name, mass_kg, velocity_m_s, charge):
        self.name = name
        self.mass = mass_kg
        self.velocity = velocity_m_s
        self.charge = charge
    
    def kinetic_energy(self):
        return 0.5 * self.mass * self.velocity**2
    
    def potential_energy(self, voltage):
        return self.charge * voltage
    
#-----------------------    
# Plot
#----------------------
import matplotlib.pyplot as plt

names = []
energies = []

for p in particles:
    names.append(p.name)
    energies.append(p.kinetic_energy() / 1.6e-19)

plt.bar(names, energies)
plt.xlabel("Particle")
plt.ylabel("Energy (eV)")
plt.title("Particle Energy Comparison")
plt.show()

#----------------------------------------
#PART C - REFLECTION AND INTEGRATION.
#----------------------------------------
## Reflection (Mini-essay)
#--------------------------
#Python plays an important role in plasma physics research. Scientists use Python to simulate plasma behavior, analyze temperature data, and visualize particle motion. Many laboratory experiments produce large amounts of data, and Python helps process and classify this information efficiently.
#For example, in this assignment, I created a function to classify plasma temperatures into cold, warm, and hot categories. This kind of tool can help researchers quickly identify plasma conditions during experiments. I also used object-oriented programming to calculate particle energy, which is important in understanding plasma interactions.
#Overall, Python makes complex physical calculations easier, faster, and more organized.

## Quick reflection — 
#----------------------
## What was easiest / hardest?
# Easiest Part: Creating simple functions and using loops was easy.
# Hardest Part: Understanding classes and object-oriented programming was slightly challenging at first.

## How might Anaconda environments help in real research?
# Anaconda helps manage different Python libraries and environments, which is important in research to avoid software conflicts.

## One thing you want to learn next (e.g. NumPy, matplotlib, pandas)
# I want to learn NumPy and Matplotlib for scientific plotting and numerical simulations.

