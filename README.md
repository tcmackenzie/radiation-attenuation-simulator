# X-ray Attenuation Through Biological Materials

## Overview

A Python-based computational physics project modelling the attenuation of X-ray radiation as it travels through different materials, including biological tissues.

The simulation uses tabulated mass attenuation coefficients and material densities to investigate the transmission of X-rays through individual materials and layered representations of biological tissue.

The project explores the application of the Beer–Lambert law to radiation physics, with potential applications in medical imaging and radiation dosimetry.

## Physics Background

The attenuation of a narrow beam of X-rays through matter can be described using the Beer–Lambert law:

\[
I(x) = I_0 e^{-(\mu/\rho)\rho x}
\]

Where:

- \(I(x)\) is the transmitted intensity
- \(I_0\) is the initial intensity
- \(\mu/\rho\) is the mass attenuation coefficient
- \(\rho\) is the material density
- \(x\) is the distance travelled through the material

The mass attenuation coefficient describes the interaction of X-rays with a material, while density determines how much material is encountered along a given path length.

## Materials Investigated

The simulation currently considers five materials:

- Air
- Water
- Bone
- Lung tissue
- Soft tissue

Mass attenuation coefficients are extracted from tabulated material data at an incident photon energy of 0.1 MeV (100 keV), using the nearest available energy value.

## Methodology

The simulation is developed in Python using NumPy and Matplotlib.

The main stages are:

1. Import tabulated mass attenuation coefficients for each material.
2. Extract attenuation coefficients at the selected photon energy.
3. Model X-ray transmission through individual materials.
4. Simulate transmission through a sequence of material layers.
5. Calculate the reduction in primary beam intensity across each layer.
6. Visualise attenuation and preliminary energy-loss estimates.

## Results

### Attenuation Through Layered Materials

Plots of transmitted intensity as a function of depth are used to investigate the attenuation of X-rays through a simplified layered material model.

### Comparison Between Materials

Individual attenuation curves allow the influence of material density and mass attenuation coefficients to be compared.

### Energy Loss Estimates

The reduction in primary beam intensity across each material layer is calculated and compared.

**Note:** The current energy-loss-per-unit-mass calculation is a preliminary estimate and is not yet a validated absorbed dose calculation in Gray.

## Technologies

- Python
- NumPy
- Matplotlib

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/radiation-attenuation-simulator.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python main.py
```

## Future Development

- Investigate the energy dependence of X-ray attenuation.
- Introduce interpolation between tabulated attenuation coefficients.
- Expand the range of biological materials.
- Improve the energy deposition and absorbed dose calculations.
- Investigate the effects of different tissue compositions.
- Explore applications to medical imaging and radiation treatment planning.

## Author

Physics undergraduate interested in computational physics, medical physics and scientific modelling.
