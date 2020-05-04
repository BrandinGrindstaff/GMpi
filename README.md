## GMpi: A Growth Chamber Monitoring System Using the Raspberry Pi as a Platform

The GMpi is a cost-effective solution for monitoring the conditions of a growth chamber,
greenhouse, or any other facility for which specific conditions (temperature, light, humidity, etc.)
need to be maintained.

Please see our preprint for more information:

> Grindstaff, G., M. E. Mabry, P. D. Blischak, M. Quinn, and J. C. Pires.
> Affordable remote monitoring of plant growth and facilities using Raspberry Pi computers.
> *Applications in Plant Sciences* 7:e11280 [https://doi.org/10.1002/aps3.11280](https://doi.org/10.1002/aps3.11280).

The paper has a detailed protocol for setting up the Raspberry Pi and associated sensors.
Our sotware package, `GMPi_Pack`, provides the tools needed to take sensor readings and photos,
as well as synchronizing files with cloud storage services (e.g., Google Drive).

### Dependencies
 - Python 3
 - python-tsl2591 (Python package)
 - Adafruit\_Python\_DHT (Python Package)
 - rclone (may be pre-installed on the Raspberry Pi)

### Getting Started

The best way to get the `GMPi_Pack` software is to clone this repository:

```
git clone https://github.com/BrandinGrindstaff/GMpi.git
```

After obtaining the software, change into the `GMpi` repo and run the `configuration.py`
script, being sure to include which pins were used for the DHT and data sensors.

```
cd GMpi
python3 configuration.py <dht-pin> <data-pin>
```

This will create a configuration file (`config.txt`) where all of the needed file paths and sensor thresholds
can be set for monitoring. Several of the values in the configuration file will be automatically set and
values that need to be added by the user will be listed as `<REPLACE>`.

### Plotting Sensor Output

We also have a simple script for plotting sensor output. The script depends on the following Python packages:
`pandas`, `seaborn`, and `matplotlib`, which can all be installed using `pip`.
To run the script you will need to move it into the folder where you are storing
the `sensorOutput*` files and then simply type `./plot_sensorOutput.py`.