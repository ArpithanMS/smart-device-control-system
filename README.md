# Smart Device Control System

## Overview

This project implements a simple, extensible **Smart Device Control System** in Python. The goal is not just to make the code work, but to demonstrate a clear understanding of **Object-Oriented Programming (OOP)** principles such as abstraction, encapsulation, inheritance, and polymorphism.

The system currently supports two devices:

* **Motor**
* **Light**

The design intentionally allows new device types to be added in the future without modifying existing controller logic.

---

## Problem Objective

* Design a system where multiple device types can be controlled uniformly
* Each device maintains its own ON/OFF state
* External code must not directly modify device state
* A generic controller should be able to operate any device
* The system should be easy to extend and safe to use

---

## Project Structure

```
smart_device_system/
│
├── device.py       # Abstract base class for all devices
├── motor.py        # Motor implementation
├── light.py        # Light implementation
├── controller.py   # Generic device controller
├── main.py         # Driver / test code
└── README.md       # Design explanation
```

Each file has a single, well-defined responsibility.

---

## Design Approach

### 1. Abstraction

A base `Device` class defines the common interface (`start`, `stop`) and shared behavior for all devices. This ensures that all concrete devices behave consistently from the controller's perspective.

The base class is implemented as an **abstract base class (ABC)** to enforce implementation of required methods in subclasses.

---

### 2. Encapsulation

* Each device maintains an internal `_is_on` state
* The state is **protected** and cannot be modified directly by external code
* A read-only `is_on` property allows external code to check device status safely

This prevents invalid or accidental state changes.

---

### 3. Inheritance

Concrete devices such as `Motor` and `Light` inherit from the `Device` base class.

This avoids code duplication and ensures all devices follow the same contract.

---

### 4. Polymorphism

The controller interacts with devices using the same method calls (`start`, `stop`), while each device provides its own implementation.

This allows different behavior without conditional logic or type checking.

---

### 5. Loose Coupling

The `Controller` class depends only on the abstract `Device` interface, not on concrete device implementations.

As a result:

* New device types can be added without changing controller code
* The system follows the Open–Closed Principle

---

## Controller Design

The controller performs a generic operation:

1. Turn the device ON
2. Turn the device OFF

The controller does not:

* Check device type
* Contain device-specific logic
* Import concrete device classes

This makes the controller reusable and future-proof.

---

## Extensibility

To add a new device (e.g., `Fan`):

1. Create a new class inheriting from `Device`
2. Implement `start()` and `stop()` methods
3. Use the existing controller without modification

This validates the scalability of the design.

---

## Running the Project

From the project root directory:

```bash
python main.py
```

Expected output:

```
Motor has started
Motor has stopped
Light switched on
Light switched off
```

---

## Key Takeaways

* Emphasis is placed on **design clarity** over over-engineering
* The system demonstrates core OOP principles clearly
* The structure reflects real-world, maintainable Python code

This project is intentionally simple, but architected to scale.
