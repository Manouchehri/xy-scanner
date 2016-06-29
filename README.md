# XY-Scanner

Proof-of-concept code for an XY scanner, using an M3D printer. Example also includes a DSA815 spectrum analyzer driver to measure emissions at different frequencies.

This project has three pieces of code:

- A driver to control an M3D printer through a USB port using basic g-code commands
- A driver to control a Rigol DSA815 spectrum analyzer through a USB port using NI VISA commands
- Some basic scanning code to capture the spectrum at several points over the surface of a circuit board

Some example output images are shown in images/.
