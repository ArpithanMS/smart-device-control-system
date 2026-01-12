# Smart Device Control System

## Overview

This project implements a simple, extensible **Smart Device Control System** in Python. The objective is to demonstrate a clear understanding of **Object-Oriented Programming (OOP)** principles such as abstraction, encapsulation, inheritance, and polymorphism.

The system currently supports the following devices:

* **Motor**
* **Light**
* **Fan**

The design allows new device types to be added easily without modifying existing controller logic.

---

## Problem Objective

* Design a system where multiple device types can be controlled uniformly
* Each device maintains its own ON/OFF state
* External code must not directly modify device state
* A generic controller should be able to operate any device
* The system should be easy to extend and safe to use

---

## Project Structure
<!-- SMART_DEVICE_SYSTEM/
│
├── Devices/
│ ├── motor.py # Motor implementation
│ ├── light.py # Light implementation
│ └── fan.py # Fan implementation
│
├── device.py # Abstract base class for all devices
├── controller.py # Generic device controller
├── main.py # Driver / test code
└── README.md # Design explanation -->


Each file has a single, well-defined responsibility.

---

## Design Approach

### 1. Abstraction

A base `Device` class defines the common interface (`start`, `stop`) for all devices.  
The base class is implemented as an **abstract base class (ABC)** to enforce consistent behavior across all device types.

---

### 2. Encapsulation

* Each device maintains a **private internal state**
* The ON/OFF state is stored inside the base class and cannot be modified directly by external code
* A read-only `is_on` property allows safe state inspection

State changes are performed only through controlled internal methods, preventing invalid operations.

---

### 3. Inheritance

Concrete devices such as `Motor`, `Light`, and `Fan` inherit from the `Device` base class.

This avoids code duplication and ensures all devices follow the same contract.

---

### 4. Polymorphism

The controller interacts with all devices using the same method calls (`start`, `stop`), while each device provides its own behavior.

No conditional logic or type checks are required.

---

### 5. Loose Coupling

The `Controller` class depends only on the abstract `Device` interface, not on concrete implementations.

This follows the **Open–Closed Principle**:
* Open for extension
* Closed for modification

---

## Controller Design

The controller performs a generic operation:

1. Turn the device ON
2. Turn the device OFF

The controller does not:
* Check device types
* Contain device-specific logic
* Import concrete device classes

---

## Extensibility

To add a new device:

1. Create a new class inheriting from `Device`
2. Implement `start()` and `stop()`
3. Use the existing controller without modification

No changes are required elsewhere in the system.

---

Expected output:
Motor has started
Motor has stopped
Light switched on
Light switched off
Fan has started
Fan has stopped