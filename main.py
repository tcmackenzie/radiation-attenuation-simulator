import numpy as np
import matplotlib.pyplot as plt

class Radiation:

    def __init__(self, name, mass_attenuation, density, filename):
        self.name = name
        self.mass_attenuation = mass_attenuation
        self.density = density
        self.filename = filename

    def intensity(self, initial_intensity, x):
        return initial_intensity * np.exp(-self.mass_attenuation * self.density * x)
 

        
def main():
    value = 0.1  
    materials = {
        "air": "air_data.txt",
        "water": "water_data.txt",
        "bone": "bone_data.txt",
        "lung tissue": "lung_tissue_data.txt",
        "soft tissue": "soft_tissue_data.txt"
    } 

    answers = []
    for material, filename in materials.items():
        data = np.loadtxt(filename)
        energy = data[:, 0]
        mass_attenuations = data[:, 1]

        position = np.argmin(np.abs(energy - value))

      
        mass_attenuation = mass_attenuations[position]
        answers.append(mass_attenuation)

        print(f"{material}: {mass_attenuation}")

    print(answers) 

    x = np.linspace(0, 100, 1000)  # Distance in cm
    initial_intensity = 100

    materials = [
        Radiation("Air", answers[0], 0.001225, "air_data.txt"),
        Radiation("Water", answers[1], 1.0, "water_data.txt"),
        Radiation("Bone", answers[2], 1.85, "bone_data.txt"),
        Radiation("Lung Tissue", answers[3], 0.4, "lung_tissue_data.txt"),
        Radiation("Soft Tissue", answers[4], 1.0, "soft_tissue_data.txt")
    ]

    layers = [
        (materials[0], 20),  # Air
        (materials[1], 2),  # Water
        (materials[2], 1),  # Bone
        (materials[3], 20),    # Lung Tissue
        (materials[4], 2),     # Soft Tissue
        (materials[1], 2),     #water
        (materials[0], 20)      #air
    ]

    # Simulate the path of the X-ray through the body---------------------------------
    I = initial_intensity
    x_start = 0
    absorbed_doses = []

    for material, thickness in layers:
        x_new = x_start + thickness
        layer = np.linspace(x_start, x_new, 10000)

        distance = layer - x_start

        intensity = material.intensity(I, distance)

        plt.plot(layer, intensity, label=f"{material.name} (μ={material.mass_attenuation})")
        I = intensity[-1]

        absorbed_energy = intensity[0] - intensity[-1]
        mass = material.density * thickness 
        absorbed_dose = absorbed_energy / mass

        absorbed_doses.append(absorbed_dose)

        print(f"{material.name} (μ={material.mass_attenuation}): Absorbed Energy = {absorbed_energy}, Absorbed Dose = {absorbed_dose}")
        x_start = x_new

    plt.title("Beer-Lambert Law for Different Materials for a small dose of X-rays")
    plt.xlabel("Distance (cm)")
    plt.ylabel("Intensity (%)")
    plt.grid()
    plt.legend()
    plt.show()
    #----------------------------------------------------------------
    
    # Plotting the intensity for each material separately------------
    for material in materials:
        final_intensities = material.intensity(initial_intensity, x)
        plt.plot(x, final_intensities, label=f"{material.name} (μ={material.mass_attenuation})")

    #plt.yscale("log")
    plt.title("Beer-Lambert Law for Different Materials for a small dose of X-rays")
    plt.xlabel("Distance (cm)")
    plt.ylabel("Intensity (%)")
    plt.grid()
    plt.legend()
    plt.show()
    #----------------------------------------------------------------
    colors = ["blue"] * len(absorbed_doses)
    colors[3] = "red"
    plt.bar(range(len(absorbed_doses)), absorbed_doses, tick_label=[layer[0].name for layer in layers], color=colors)
    plt.title("Absorbed Dose for Different Materials")
    plt.xlabel("Material Index")
    plt.ylabel("Absorbed Dose (Gy)")
    plt.xticks(range(len(layers)), [layer[0].name for layer in layers], rotation=45)
    plt.show()

if __name__ == "__main__":
    main()
