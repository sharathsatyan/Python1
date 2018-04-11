"""
Our problem today is to create a simple object model of a hierarchical digital circuit design,
and implement a few functions that can provide us some data about its content.

Running py.test <this_file>, or running this file as a stand-alone python script,
will exercise all of the code you write, and the unit-tests provided below.
The tests should initially fail.  Your code should make them pass!

Feel free to modify the classes if it makes your solution easier to implement or more robust.  You
can update the unit tests if it is required in order to perform the test with the updated class
definitions, but do not change the scope of the tests or the answers.  Of course, you may add
your own unit tests as you see fit.

First we'll do a few warm-up exercises.
"""
import pytest

'''
# ----------------------------------------
# Warm-Up 1: Dictionary Inversion
#
# Write a function to invert the keys and values in a python dictionary
#  You can assume the values are unique.
# ----------------------------------------
def invert_dict(d):
    # Invert the keys and values of dict <d>
    return {v: k for k, v in d.items() }

def test_invert_dict():
    assert invert_dict({1: 'small', 2: 'big'}) == { 'big': 2, 'small': 1}
'''

# ----------------------------------------
# Warm-Up 2: Geometric Shapes
#
# Implement a small Python class-hierarchy
#  to represent a few geometric shapes and calculate their areas.
#  Make sure your initializer functions use the arguments in the unit test "test_shape_areas".
# ----------------------------------------
class Shape:
    """ Base class for all instances of a hierarchical electronic design.
        """

    def __init__(self, side):
        self.side = side

    area = 0
#    def __repr__(self):
#       return f"{self.__class__.__name__}({self.name})"



class Square(side):
    area = 36

class Rectangle(side):
    area = 25

class RightTriangle(side):
    area = 15


def area(instance,side):
    area = 0
    return instance.area

square = Square(s = 6)
print (area(square))
'''


def area(instance):
        # Return the area of the shape
    area = 0
    return instance.area
        #raise NotImplementedError

#def test_shape_areas():
    # Implement the Shape, Square, RightTriangle, and Rectangle classes above
    #  And un-comment the list of shapes below

    #shapes = []
    #shapes = [Square(s=6), Rectangle(x=9, y=4), RightTriangle(a=9, b=8) ]

#    for s in shapes:
#       assert s.area() == 36
#   #assert len(shapes)

square = Square(s = 6)
print (area(square))
'''
'''
# ----------------------------------------
# OK, that's enough warm-up.
#  On to circuit-representation objects.
# ----------------------------------------

class Block:
    """ Base class for all instances of a hierarchical electronic design.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"


class Primitive(Block):
    """
    The Primitives class is used to represent standard cells and are the leaf cells of a design hierarchy.
    Specific cells will subclass from this class and provide an area class attribute.
    """
    area = 0


# Some example primitives:
class NAND2(Primitive):
    area = 4


class NOR2(Primitive):
    area = 5


class DLAT(Primitive):
    """A simple D latch.
    """
    area = 10


class DFFx1(Primitive):
    """ A small D flip flop.
    """
    area = 20


class DFFx2(Primitive):
    """ A strong D flip flop with twice the drive strength (and area) of the x2 version.
    """
    area = 40


class Module(Block):
    """Modules are used to represent the upper levels of the design hierarchy.
    The design is assumed to be a gate level netlist consisting of instances of Primitives or other Modules.

    The instances are stored in an *instances* dictionary that maps the instance name to the instance.
    """

    def __init__(self, name):
        super().__init__(name=name)
        self.instances = {}

    def add_instance(self, module_or_prim, name):
        inst = module_or_prim(name=name)
        self.instances[name] = inst


# Some example hierarchical designs
class Counter(Module):
    def __init__(self, name):
        """ Four bit counter.
        """
        super().__init__(name=name)
        self.add_instance(DFFx1, name='q0')
        self.add_instance(DFFx2, name='q1')
        self.add_instance(DFFx1, name='q2')
        self.add_instance(DFFx2, name='q3')


class FrequencyComparator(Module):
    """A block that uses two counters to compute the frequency ratio of
    two clock inputs.
    """

    def __init__(self, name):
        super().__init__(name=name)

        self.add_instance(Counter, name="cnt1")
        self.add_instance(Counter, name="cnt2")
        self.add_instance(NAND2, name="i0")
        self.add_instance(NAND2, name="i1")
        self.add_instance(NOR2, name="i2")
        self.add_instance(NOR2, name="i3")
        self.add_instance(DLAT, name="l0")
        self.add_instance(DLAT, name="l1")


# ----------------------------------------
# Problem one:  Implement a function to calculate Block area
#
# This <get_area> function should take a Block (either Primitive or Module)
#  as its sole argument.
#
# The tests below will exercise this function,
#  checking a few of the already-defined blocks.
# ----------------------------------------
def get_area(instance):
    return -1


# ----------------------------------------
# Problem two: Find all of the flip flops in the design.
#
# This function should return all of the instances in a sequence.
# Assume that the flip flops are Primitives whose class names begins with 'DFF'.
# ----------------------------------------
def get_flops(instance):
    # Return a list of flip-flop instances
    return []


# ----------------------------------------
# Problem three:
# Can you implement a method for the Block class
# that will produce the hierarchical path to this instance
#
# The path should be stored in the *path* attribute of the Module and Primitve instances.
# See the 'test_paths' unit test for examples.
# ----------------------------------------


# ----------------------------------------
# Problem four:
# Create a function that when given a top level instance, can determine
# the order the modules would need to be compiled, assuming the instances
# contained withing a module need to be compiled before that module can be compiled.
#
# For example, the Counter block instantiates a few DFFx1 modules
# and a few DFFx2 modules.  Those are primitives that have no instances.
# Therefore, the two solutions would be [DFFx1, DFFx2, Counter] and
# [DFFx2, DFFx1, Counter]
# ----------------------------------------
def get_compilation_order(instance):
    return []


# ----------------------------------------
# Unit Tests
# ----------------------------------------
def test_area():
    # Tests for your get_area() function

    latch = DLAT(name='xlat')
    assert get_area(latch) == 10

    dff = DFFx1(name='dff')
    assert get_area(dff) == 20

    ctr = Counter(name='top')
    assert get_area(ctr) == 120

    comp = FrequencyComparator(name="duv")
    assert get_area(comp) == 278


def test_flops():
    # Tests for your get_flops() function

    comp = FrequencyComparator(name="duv")
    flops = get_flops(comp)
    assert len(flops) == 8
    assert all([f.name.startswith('q') for f in flops])

    ctr = Counter(name='top')
    flops = get_flops(ctr)
    assert len(flops) == 4
    assert all([f.name.startswith('q') for f in flops])


def test_paths():
    # Problem three:  Update the <Block> class and its sub-classes to produce a hierarchical path for the instances

    comp = FrequencyComparator(name="duv")
    flops = get_flops(comp)

    print("Paths to all of the flip flops")
    paths = [ff.path for ff in flops]
    assert "duv.cnt1.q0" in paths
    assert "duv.cnt1.q1" in paths
    assert "duv.cnt2.q0" in paths
    assert "duv.cnt2.q1" in paths


def test_compilation_order():
    top = Counter(name='top')
    counter_order = get_compilation_order(top)

    # Lets try out a simple test case first.
    # This one only has two solutions
    solution1 = [DFFx1, DFFx2, Counter]
    solution2 = [DFFx2, DFFx1, Counter]
    assert counter_order == solution1 or counter_order == solution2

    # This one is more complex.  We'll just print out the results and look at it.
    comp = FrequencyComparator(name='duv')
    freq_comp_order = get_compilation_order(comp)
    print(freq_comp_order)


if __name__ == '__main__':
    pytest.main([__file__])
'''
