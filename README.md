### PLC Connection with Python

## List of versions used

- **Python** v3.9.2
- **Virtualenv** v20.7.1
- **PyModbus** v2.5.2

This does not mean it wouldn't work on higher/lower version of Python

## Usage

Create a "main.py" file and paste the following code below and run it:

```Python
import logging

from plcQue import GetSetPlcData

# Change this to the configuration you want
logging.basicConfig(
  filename="sample log.logs",
  filemode="a",
  format="%(asctime)s :: %(levelname)s \n - %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S",
  level=logging.INFO
  )
logger = logging.getLogger("logs")

# See that value changes
r100 = GetSetPlcData("10.10.10.1", "302", logger).get_register("r100")
print(r100)
GetSetPlcData("10.10.10.1", "302", logger).set_register("r100", "15")
r100 = GetSetPlcData("10.10.10.1", "302", logger).get_register("r100")
print(r100)

# coils registered are x, m, and y
x0 = GetSetPlcData("10.10.10.1", "302", logger).get_coil("x0")
print(x0)
GetSetPlcData("10.10.10.1", "302", logger).set_coil("x0", "1")
x0 = GetSetPlcData("10.10.10.1", "302", logger).get_coil("x0")
print(x0)

```

## Libraries from Different Plc Brands

![alt text](https://github.com/nellartsa/Plc-with-Python/blob/main/List%20of%20Libraries.png?raw=true)

## Video Reference

- https://www.youtube.com/watch?v=EMkWRlbpJsk&t=1593s
