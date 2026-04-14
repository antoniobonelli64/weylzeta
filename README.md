# weylzeta
Computational verification of the Kaleidoscopic Filter Theorem on unrestricted partitions via A_{k-1} Weyl reflections.
# WeylZeta: The Kaleidoscopic Filter

This repository contains the core Python scripts verifying the combinatorial and geometric properties of the Kaleidoscopic Filter Theorem, as detailed in the related mathematical manuscript.

## Overview
The scripts demonstrate the exact destructive interference of lower-dimensional geometries when the coefficients of $A_{k-1}$ Weyl reflections are applied to the infinite sequence of unrestricted partitions $p(n)$. The computation resolves the continuous thermodynamic noise into a rigid discrete topology.

## Files
* `kaleidoscope_filter.py`: Computes the exact partition annihilation, demonstrating the transition from $p(n)$ to $p_{>k}(n)$ via symmetric Weyl chamber boundary conditions.
* `genera_grafico.py`: Generates the visual and statistical representation of the spectral condensation, comparing the exponential growth of unrestricted partitions with the filtered topological residue.
* `L_Functions_Kaleidoscope.py`: Extends the geometric framework to the Selberg class of Dirichlet $L$-functions. By incorporating completely multiplicative characters $\chi(n) \pmod q$ as quantum weights on the $A_{k-1}$ lattice points, this script verifies the equivariant Ehrhart extension. It computationally demonstrates that the Kaleidoscopic Filter preserves its strict self-adjoint symmetry and spectral condensation on the critical line only when a pure Euler product is present, confirming the universality of the theorem and the exclusion of non-Eulerian counter-examples.

## Associated Research
The theoretical framework, including the proofs via Ehrhart-Macdonald Reciprocity and Hodge-Riemann bilinear forms, is available as a preprint on Zenodo.

**Preprint DOI:** `https://doi.org/10.5281/zenodo.19456765`

## Usage
The scripts are written in standard Python 3. No external libraries beyond standard mathematical and plotting modules (like `matplotlib` for the graph generator) are required.

```bash
python kaleidoscope_filter.py
