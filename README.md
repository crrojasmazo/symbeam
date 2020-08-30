<p align="center">
  <a href=""><img alt="symbeam" src="img/symbeam_logo.svg" width="60%"></a>
  <p align="center">A pedagogical package for beam beanding.</p>
</p>

`symbeam` is a pedagogical software package, written in Python, targeted at Mechanical, Civil and Industrial Engineering students learning the fundamentals of bending of beams, namely, bending diagrams and beam deflections.

The modular object-oriented-based design of `symbeam` combined with the excelent symbolic engine [SymPy](https://www.sympy.org/pt/index.html), on which `symbeam` relies heavily, provides an unique computational learning environemnt for student grasping these concepts for the first time.
`symbeam` can be exploited to quickly assess the solutions of exercises for a wide variety of bending loadings and supports while allowing to easily modify the parameters of the problem fostering physical intuition and improving the students' understanding of the phenomena.

Conversely, `symbeam` can also be used by teachers to create and validate new problems for classes and exams, faccilitating this sometimes cumbersome task.

## Installation

### Installing from source
Clone this reposityory into your system
```
git clone git@github.com:amcc1996/symbeam.git
```
and install the Python package with `pip3`, running the following command inside `symbeam` root directory, where the `setup.py` is located
```
pip3 install .
```
At this point, `symbeam` can be imported into your Python scripts and modules the usual Python-way
```python
import symbeam
```

## Usage
Virtually all useful features of `symbeam` can be accessed through the `beam` class. `beam` objects, this is, concrete instances of the `beam` class, are initially defined by the starting point (0 by default) and the beam length. The beam supports, material and section properties and loadings are set by calling a specific set of methods on the beam object.

In the following sections, a thorough description of an exemplar application of `symbeam` is given. It should be noted beforehand that most (if not all) values characterising the problem can se set either using numerical input (e.g. 100) or a literal expression (100 * x + 100). In any case, this input is `sympified` using `SymPy` facilities, allowing to handle input of distinct types out-of-the-box.

### Creating a beam
The fundamental tool for a bending analysis with `symbeam` is a `beam` object, as emphasised above. To create a new beam, import the `beam` class from the `symbeam` package. Then, simply call the `beam` constructor by passing the length of the beam and, if needed, a starting point. For instance, a beam with length equal to 1 and starting at 0 can be created by

```python
from symbeam import beam

new_beam = beam(1, x0=0)
```

As claimed before, one can create a beam with both numeric and symbolic input. A list of the distinct alternatives for instantiating a beam follows (the optional initial position `x0` is omitted here, for simplicity). Note that these alternatives also apply to any input data that can be given to `beam` methods, for instance, for specifying supports, loads and properties.

1. Numeric input
```python
from symbeam import beam

new_beam = beam(1)
```

2. Numeric input from string
```python
from symbeam import beam

new_beam = beam("1")
```

3. Symbolic input from string

```python
from symbeam import beam

new_beam = beam("L")
```

4. Symbolic input from a symbolic variable created with SymPy
```python
from symbeam import beam
import sympy

L = sympy.symbols("L")
new_beam = beam(L)
```

5. Symbolic input from a symbolic variable provided by SymPy
```python
from symbeam import beam
from sympy.abc import L

new_beam = beam(L)
```

### Setting beam properties: Young modulus and second moment of area
A beam must be associated with some distribution of material propertiy and section geometry along its length, namely, the Young modulus of the material and the second moment of area of the section. While these are not required for finding the bending diagramas, as these results simply from equilibirum considerations, they are mandatory for computing the deflections of the beam.

In `symbeam`, these properties can be set in individual segments along the beam, such that the set of segments for each property must encompass all the beam span and not be overlapping at any region. For example, considering a beam of length `L`, the Young modulus and second moment of area are set by passing the stating and ending coordinate and the value as follows
```python
from symbeam import beam
from sympy.abc import L, E, I

new_beam = beam(L)

# new_beam.set_young(x_start, x_end, value)
new_beam.set_young(0, L/2, E)
new_beam.set_young(L/2, L, E/100)

# new_beam.set_inertia(x_start, x_end, value)
new_beam.set_inertia(0, L/2, I)
new_beam.set_inertia(L/2, L, I/10)
```

> :warning: **Our beloved symbols E and I**: Be careful when specifying symbolic Young modulus and second moment of area via a string, for instance, with "E" and "I". SymPy parses the string in the expression and will interpret "E" as the Nepper number and "I" as the imaginary operator. Prioritise using the variables directly imported from `sympy.abc` or create the variables explicitely with `sympy.symbols()`.
