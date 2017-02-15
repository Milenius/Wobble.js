#Simples NeuroNet (Sigmoid; kein Eta/Alpha System; Minimaler Gradient Descend Ansatz)

import numpy as np 
from IPython import get_ipython
import scipy
import matplotlib
import matplotlib.pyplot as plt

#Sigmoid und Sigmoid Ableitungsfunktionen werden Deklariert 
def nonlin(x, deriv=False):  
    if(deriv==True):
        return (x*(1-x))
        #return (1/(1+np.exp(-x)))*(-np.exp(-x)/(1+np.exp(-x)))
        #return (1/(1+np.exp(-x)))*(1-(1/(1+np.exp(-x))))
    
    return 1/(1+np.exp(-x))  

def func(x):
  return 2*x


#AND-GATE Wahrheitstabelle
# Input Daten. Letzte Spalte für BIAS Neuronen!                BIAS       
X = np.array([[0,0,0                                           ,1],
              [0,0,1                                           ,1],
              [0,1,0                                           ,1],
              [0,1,1                                           ,1],
              [1,0,0                                           ,1],
              [1,0,1                                           ,1],
              [1,1,0                                           ,1],
              [1,1,1                                           ,1]])

#Output Daten
y = np.array([[0,0],
              [0,0],
              [0,0],
              [0,1],
              [1,0],
              [1,1],
              [1,1],
              [1,1]])
              

#Der Zufalls-Seed für die erste Generierung der Synapsen
np.random.seed(123467)

#Erstellen der 2 Synapsen Matrizen.              
syn0 = 2*np.random.random((4,7)) - 1 #syn0 ((Menge der Input Neuronen einschließlich BIAS,Anzahl der Hidden-Layer Neuronen))
syn1 = 2*np.random.random((7,2)) - 1 #syn1 ((Anzahl der Hidden-Layer Neuronen, Anzahl der Output Neuronen)) 

#Variablen für Statistiken und Debugging
first_output_print = True
durchgänge=0
accuracy = 0
x_axis = []
y_axis = []
l2_delta_list = []
l1_delta_list = []
l2_error_list = []
l1_error_list = []

print("Am Lernen...")

#Lernschleife (Unterbrochen bei bestimmtem Fehlerquotienten)
while True:  
    
    #Statistik und Debug Zähler
    durchgänge = durchgänge+1

    #Output der Layer wird berechnet. l0 = Input. l1 = Hidden 1. l2 = Output.
    l0 = X                          
    l1 = nonlin(np.dot(l0, syn0))   
    l2 = nonlin(np.dot(l1, syn1))   

    #Fehler wird berechnet
    l2_error = y - l2

    

    if durchgänge % 100000 == 0:
      print("Derzeitiger Fehler in Runde "+str(durchgänge)+" :       (Durchscnitt) :"+str(round(np.mean(np.abs(l2_error)),9)))
      print(l2_error)
      pass
    
    #Back-Prop Modul fängt an
    #Delta- und weitere Fehler-Werte werden vom Output aus in richtung Input Berechnet.      
    l2_delta = l2_error*nonlin(l2, deriv=True)
    
    l1_error = l2_delta.dot(syn1.T)
    
    l1_delta = l1_error * nonlin(l1,deriv=True)
    
    #Synapsen werden mit den Delta-Werten korrigiert
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

    #Lernschleife wird Unterbrochen bei einem bestimmten Fehlerquotienten 
    if (np.mean(np.abs(l2_error))) <= 0.005:
      break

    #Debugging/Statikstik
    accuracy = round(100*(1 - (np.mean(np.abs(l2_error)))),3)

    if first_output_print == False:   

        print ("Erster Output:")
        print(l2)

        first_output_print = True

    l2_delta_list.append(1000*np.mean(l2_delta))
    l1_delta_list.append(1000*np.mean(l1_delta))
    l2_error_list.append(1000*np.mean(l2_error))
    l1_error_list.append(1000*np.mean(l1_error))

    x_axis.append(durchgänge)
    y_axis.append(accuracy)

print("Lernen Beendet nach "+str(durchgänge)+" Runden!")
print("")

while True:
  in_gate = input("Gatter [AND/OR]: ")
  if in_gate == "AND":
    in_gate = 0
  elif in_gate == "OR":
    in_gate = 1
  elif in_gate == "STATS":
    plt.plot(x_axis,l2_delta_list,label='Output Layer Delta (*10^3)')
    plt.plot(x_axis,l1_delta_list,label='Hidden Layer Delta (*10^3)')
    plt.plot(x_axis,l2_error_list,label='Output Layer Error (*10^3)')
    plt.plot(x_axis,l1_error_list,label='Hidden Layer Error (*10^3)')
    plt.plot(x_axis,y_axis,label='Genauigkeit')
    plt.xlabel('Durchgang')
    plt.ylabel('Stats')
    plt.title('NeuroNet01 Statistiken')
    plt.legend()
    plt.show()
  
  in_logic1 = int(input("Wert 1: "))
  in_logic2 = int(input("Wert 2: "))

  l0 = np.array([[ in_gate , in_logic1 , in_logic2 ,1]])                          
  l1 = nonlin(np.dot(l0, syn0))   
  l2 = nonlin(np.dot(l1, syn1))

  print("Ist die richtige Antwort? ")
  print("Output: "+str((np.round(l2[0][1]).astype(int)))) 


