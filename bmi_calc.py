import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def show_graph(height, weight): 
    fig, ax=plt.subplots()
    x=np.array([1.0, 2.1])
    
    upper_limit=np.array([60*1**2, 60*2.1**2])
    
    y_adipositas3=np.array([40*1**2, 40*2.1**2]) # BMI=40
    ax.plot(x, y_adipositas3, label="Adipositas III", color="darkred")
    
    ax.fill_between(x, upper_limit, y_adipositas3, color="darkred", alpha=0.5)
    
    y_adipositas2=np.array([35*1**2, 35*2.1**2]) # BMI=35
    ax.plot(x, y_adipositas2, label="Adipositas II", color="red")
    
    ax.fill_between(x, y_adipositas3, y_adipositas2, color="red", alpha=0.5)
    
    y_adipositas1=np.array([30*1**2, 30*2.1**2]) # BMI=30
    ax.plot(x, y_adipositas1, label="Adipositas I", color="orange")
    
    ax.fill_between(x, y_adipositas2, y_adipositas1, color="orange", alpha=0.5)
    
    y_uebergewicht=np.array([25*1**2, 25*2.1**2]) # BMI=25
    ax.plot(x, y_uebergewicht, label="Übergewicht", color="yellow")
    
    ax.fill_between(x, y_adipositas1, y_uebergewicht, color="yellow", alpha=0.5)
    
    y_normalgewicht=np.array([18.5*1**2, 18.5*2.1**2]) # BMI=18.5
    ax.plot(x, y_normalgewicht, label="Normalgewicht", color="lime")
    
    ax.fill_between(x, y_uebergewicht, y_normalgewicht, color="lime", alpha=0.5)
    
    y_untergewicht1=np.array([17*1**2, 17*2.1**2]) # BMI=17
    ax.plot(x, y_untergewicht1, label="Untergewicht I", color="aqua")
    
    ax.fill_between(x, y_normalgewicht, y_untergewicht1, color="aqua", alpha=0.5)
    
    y_untergewicht2=np.array([16*1**2, 16*2.1**2]) # BMI=16
    ax.plot(x, y_untergewicht2, label="Untergewicht II", color="cornflowerblue")
    
    ax.fill_between(x, y_untergewicht1, y_untergewicht2, color="cornflowerblue", alpha=0.5)
    
    y_untergewicht3=np.array([0,0]) # BMI=0
    ax.plot(x, y_untergewicht3, label="Untergewicht III", color="darkblue")
    
    ax.fill_between(x, y_untergewicht2, y_untergewicht3, color="darkblue", alpha=0.5)
    plt.grid()
    plt.ylabel("Gewicht in kg")                                          
    plt.xlabel("Größe in m")
    plt.legend()  
    ax.plot(height, weight, marker="o", color="black", markersize=3, label="Du")
    st.pyplot(fig)
    
borders={"Adipositas III": 40, "Adipositas II": 35, "Adipositas I": 30, 
         "Übergewicht": 25, "Normalgewicht": 18.5, "Untergewicht I": 
         17, "Untergewicht II": 16, "Untergewicht III": 0}

st.header("BMI Calculator")
weight=st.slider("Wähle dein Gewicht (kg)", 1, 160)
height=st.slider("Wähle deine Größe (cm)", 100, 210)
if (st.button("Berechne BMI")):
    st.subheader("BMI Ergebnis")
    show_graph(height/100, weight)
    bmi=weight/(height/100)**2
    lower_weight=18.5*(height/100)**2
    upper_weight=24.9*(height/100)**2
    for k, v in borders.items():
        if bmi>v:
            state=k
            break
    st.write(f"Dein BMI ist {round(bmi, 2)}.")
    st.write(f"Du bist damit im folgendem Bereich: {state}.")
    st.write(f"Das Normalgewicht für deine Größe ist {round(lower_weight, 2)}kg - {round(upper_weight, 2)}kg.")
