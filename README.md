# EvoSIM
An application which simulates a multitude of observed behaviours in nature, including genetic evolution, pred vs prey dynamics.

# Evolution Simulation

## 🧬 Description  
Describe the purpose of your simulation (e.g. natural selection, trait adaptation, predator-prey dynamics, etc.), key features (e.g. real-time visualisation, trait mutation, generational statistics), and what makes it unique or interesting.
The purpose of my EvoSIM application is to have three functioning simulations which allow for the user to interact with and watch predator vs prey dynamics, the lotka voltera mathematical model, in conjunction with how genetic traits evolve over time to increase surival chances in a specific environment. 

---

## ⚙️ Installation Instructions  
Step-by-step setup guide for running the project locally.

1. **Download the Repository**  
   Download the ZIP file from the GitHub repository and extract it to any location on your computer.

2. **Install Required Dependencies**  
   If the simulation uses external libraries (e.g., `pygame`, `matplotlib`), install them by running:

   ```bash
   pip install -r requirements.txt
   ```

   If there is no `requirements.txt`, install them manually:

   ```bash
   pip install pygame matplotlib
   ```

3. **Run the Simulation**  
   Double-click `FinalVersion.py` to start the simulation, or run it from the command line:

   ```bash
   python FinalVersion.py
   ```

4. **Optional:** Modify Parameters  
   You can adjust simulation settings (e.g. number of creatures, food respawn rate) using the GUI input boxes or by editing values in the source files.

---

## 🚀 How to Use  
_How users interact with the simulation._  

- Launch the simulation from your terminal.
- Use the input boxes to define:
  - Number of starting creatures
  - Maximum population
  - Respawn rate of food
- Click **Start** to begin the simulation.
- Observe real-time updates in the simulation window and the graph tracking average traits (e.g. speed, size, vision).
- Click **Stop** or **Reset** as needed.

---

## 📄 License  
_This project is licensed under the:_  
**[Your License Name Here]**  
e.g., MIT License, Apache 2.0, GPLv3.  
See `LICENSE` file for full details.

---

## 🖼️ Visuals  
_Add screenshots or gifs of your simulation here._  

<p align="center">
  <img src="assets/screenshot1.png" width="600" alt="Simulation Screenshot">
  <br>
  <em>Main simulation window with real-time trait graph.</em>
</p>

---

## 🙏 Acknowledgements  
_Give credit where it's due._  

- Inspired by [Simulation Theory / Nature of Code / etc.]
- Special thanks to [Mentors, Contributors, Libraries, Tools]

---

## 👤 Author  
**Name:** [Your Full Name]  
**Email:** [your.email@example.com]  
**GitHub:** [https://github.com/yourusername](https://github.com/yourusername)  
**Website/Portfolio:** [yourwebsite.com]

---

## 📁 Directory Structure  

```
evo-sim/
├── assets/              # Images, fonts, icons
├── src/                 # Main simulation code
│   ├── creatures.py     
│   ├── environment.py   
│   └── simulation.py    
├── docs/                # Optional documentation
├── LICENSE              
├── README.md            
├── main.py              
└── requirements.txt     
```

---

## 📌 Additional Details  
_Use this section for complex setup, optional config files, arguments, or advanced usage._  

- Configurable parameters: (e.g., mutation rate, food spawn rate)
- Supports saving/loading simulation states.
- May require Python ≥ 3.10
- GPU acceleration supported with [library] (optional)

---
