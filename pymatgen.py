#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pymatgen.core
import pymatgen


# In[10]:


print(pymatgen.core.__version__)


# In[11]:


import sys
print(sys.version)


# In[12]:


#Structure and molecules

#Creating a molecule
from pymatgen.core.structure import Molecule


# In[13]:


Molecule


# In[16]:


oh_minus = Molecule(["O", "H"], [[0.0,0.0,0.0],[0.0,0.0,1.0]], charge = -1)
print(oh_minus)


# In[21]:


# Introducing sites, elements, and species in molecule
# A molecule object has many attribute and properties
print(oh_minus.cart_coords)


# In[22]:


print(oh_minus.center_of_mass)


# In[24]:


# we can change the charge and spin of the molecule later  

oh_minus.set_charge_and_spin(charge = 1)
print(oh_minus)


# In[25]:


#Let's check how many sites are present in the carbon oh minus sites
len(oh_minus)  #number of species


# In[26]:


#print fisrst site 

print(oh_minus[0])


# In[27]:


oh_minus[0] = "H"
oh_minus[0] = "O"
print(oh_minus)


# In[29]:


site0 = oh_minus[0]


# In[30]:


#Let's check it's properties

site0.coords


# In[31]:


site0.specie


# In[32]:


from pymatgen.core.composition import Element, Composition


# In[34]:


from pymatgen.core.periodic_table import Specie


# In[35]:


carbon = Element("C")


# In[36]:


carbon.average_ionic_radius


# In[37]:


o_ion = Specie("O", oxidation_state = -2)
print(o_ion)


# In[39]:


o_ion.atomic_mass


# In[40]:


Specie.from_string("O2-")


# In[41]:


comp = Composition({"Au":0.5, "Cu": 0.5})


# In[42]:


print("formula", comp.alphabetical_formula)
print("chemical system", comp.chemical_system)


# # Hydrogen cynide 
# # Construct the linear HCN Molecule where each bond distance is the sum of the two atomic radai
# 
# H_rad = Element("H").atomic_radius
# C_rad = Element("C").atomic_radius
# N_rad = Element("N").atomic_radius

# In[44]:


HC_bond_dist = H_rad + C_rad 
CN_bond_dist = C_rad + N_rad


# In[46]:


H_pos = 0
C_pos = H_pos + HC_bond_dist
N_pos = C_pos + CN_bond_dist


# In[48]:


hcn = Molecule(["H", "C", "N"], [[H_pos, 0.0, 0.0], [C_pos, 0.0, 0.0], [N_pos, 0.0, 0.0, 0.0]])
print(hcn)


# # Creating structure and lattice 

# In[49]:


from pymatgen.core import Lattice, Structure


# In[50]:


my_lattice = Lattice([[5, 0, 0], [0, 5, 0], [0, 0, 5]])


# In[51]:


print(my_lattice)


# In[52]:


my_lattice_2 = Lattice.from_parameters(5,5,5,90,90,90)


# In[53]:


print(my_lattice_2)


# In[54]:


lattice3 = Lattice.cubic(5)
print(lattice3)


# In[55]:


bcc_fe = Structure(Lattice.cubic(2.8), ["Fe", "Fe"], [[0.0, 0.0,0.0], [0.5,0.5,0.5]])
print(bcc_fe)


# In[61]:


bcc_fe_from_cart = Structure(Lattice.cubic(2.8), ["Fe", "Fe"], [[0, 0,0],[1.4, 1.4, 1.4]], coords_are_cartesian = True)


# In[62]:


print(bcc_fe_from_cart)


# # Creating Structure From space Group

# In[63]:


bcc_fe = Structure.from_spacegroup("Im-3m", Lattice.cubic(2.8), ["Fe"], [[0,0,0]])
print(bcc_fe)


# In[ ]:




