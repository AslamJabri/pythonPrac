5 types of inheritance
    1.single Inheritance
    In this only there is a parent class and a child class.
    
    2.Multi-level
    When a class is derived from a class which itself is derived from another class, it is called multilevel inheritance. We can extend the classes to as many levels as we want to.
    A Car IS A Vehicle
    A Hybrid IS A Car

    3.Hierarhical
    In hierarchical inheritance, more than one class extends, as per the requirement of the design, from the same base class. The common attributes of these child classes are implemented inside the base class.
    A Car IS A Vehicle
    A Truck IS A Vehicle

    4.multiple
    When a class is derived from more than one base class, i.e., when a class has more than one immediate parent class, it is called multiple inheritance.
    HybridEngine IS A ElectricEngine.
    HybridEngine IS A CombustionEngine as well.

    5.Hybrid
    A type of inheritance which is a combination of Multiple and Multi-level inheritance is called hybrid inheritance.
    CombustionEngine IS A Engine.
    ElectricEngine IS A Engine.
    HybridEngine IS A ElectricEngine and a CombustionEngine.
