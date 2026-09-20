# Assignment 2 Report: Factory Method and Abstract Factory

**Course:** ShP-2216 Software Design Patterns  
**Programme:** 6B06102 Software Engineering | Year 2, Trimester 4  
**Institution:** Astana IT University | School of Software Engineering  
**Instructor:** Yerassyl Bekenov  
**Format:** Individual work | Java, JDK 17 | Report in English  
**Submission Deadline:** 20.09.2026, 23:59  

---

## 1. Identification

- **Full Assignment Title:** Assignment 2 — Factory Method and Abstract Factory
- **Full Name:** Akyl Muratbek
- **Group:** SE-2523
- **Email:** muratbekakyl9@gmail.com
- **GitHub Repository Link:** https://github.com/Akylsolo/Sdp_Assignment
- **Submitted Commit Hash:** *(Refer to latest commit hash on branch `master`)*

---

## 2. Introduction

This project implements an enterprise logistics execution system that coordinates freight transport and cross-platform graphical user interface rendering. The system integrates two foundational Gang of Four (GoF) creational design patterns into a single cohesive runtime application:

1. **Factory Method Pattern (Freight Transport Subsystem):**
   - **Problem:** Logistics workflows require a unified dispatch algorithm (`planDelivery`), but the concrete vehicle used to perform delivery (`Truck` for road transport, `Ship` for sea transport) depends on the chosen delivery mode. Direct instantiation inside the core workflow would couple high-level business logic to specific vehicle classes.
   - **Solution:** `Logistics` declares an abstract factory method `createTransport()` and implements the invariant delivery orchestration algorithm in `planDelivery(cargo, destination)`. Concrete creator subclasses (`RoadLogistics`, `SeaLogistics`) override the factory method to instantiate their corresponding transport products.

2. **Abstract Factory Pattern (Cross-Platform UI Subsystem):**
   - **Problem:** Graphical clients require complete sets of complementary UI controls (Buttons and Checkboxes) styled specifically for the operating environment (Windows or macOS). If client code assembled controls independently, incompatible UI components could accidentally be mixed (e.g., Windows button with macOS checkbox).
   - **Solution:** `GUIFactory` defines an interface declaring creation methods for all members of the UI product family (`createButton()` and `createCheckbox()`). Concrete factories (`WindowsFactory`, `MacOSFactory`) guarantee platform consistency by producing strictly matching component pairs. The client (`DeliveryApplication`) interacts solely through abstract interfaces.

---

## 3. UML Class Diagrams

### 3.1 Factory Method Pattern Diagram

```
+-----------------------------------------------------------------------------------+
|                           kz.aitu.assignment2.transport                           |
|                                                                                   |
|         <<interface>>                                                             |
|           Transport                                                               |
|   + deliver(cargo: String, destination: String): void                             |
|              ^                                    ^                               |
|              | realizes                           | realizes                      |
|      +-------+--------+                   +-------+--------+                      |
|      |     Truck      |                   |      Ship      |                      |
|      +----------------+                   +----------------+                      |
|      |+deliver(...):v |                   |+deliver(...):v |                      |
+-----------------------------------------------------------------------------------+
       ^                                    ^
       | <<creates>>                        | <<creates>>
+-----------------------------------------------------------------------------------+
|                           kz.aitu.assignment2.logistics                           |
|                                                                                   |
|         <<abstract>>                                                              |
|          Logistics                                                                |
|   + {abstract} createTransport(): Transport                                       |
|   + planDelivery(cargo: String, destination: String): void                        |
|              ^                                    ^                               |
|              | extends                            | extends                       |
|      +-------+--------+                   +-------+--------+                      |
|      | RoadLogistics  |                   |  SeaLogistics  |                      |
|      +----------------+                   +----------------+                      |
|      |+createTransport|                   |+createTransport|                      |
+-----------------------------------------------------------------------------------+
       ^
       | delegates workflow
+------+--------------------------+
|      kz.aitu.assignment2.app    |
|        DeliveryApplication      |
|  - logistics: Logistics         |
|  - button: Button               |
|  - checkbox: Checkbox           |
|  + run(cargo, dest): void       |
+---------------------------------+
```

#### Detailed Element Mapping:
- **Product Interface:** `kz.aitu.assignment2.transport.Transport` declaring `deliver(String cargo, String destination)`.
- **Concrete Products:** `Truck` (road delivery) and `Ship` (sea delivery) implementing `Transport`.
- **Abstract Creator:** `kz.aitu.assignment2.logistics.Logistics` declaring abstract `createTransport()` and concrete template method `planDelivery(...)`.
- **Concrete Creators:** `RoadLogistics` (returns `Truck`) and `SeaLogistics` (returns `Ship`).
- **Shared Runtime Flow:** `planDelivery(...)` invokes `createTransport()` polymorphically and dispatches `transport.deliver(cargo, destination)`.
- **Client Dependency:** `DeliveryApplication` holds a `Logistics` reference without knowing concrete transport classes.

---

### 3.2 Abstract Factory Pattern Diagram

```
+-----------------------------------------------------------------------------------+
|                               kz.aitu.assignment2.ui                              |
|                                                                                   |
|       <<interface>>                                       <<interface>>           |
|          Button                                             Checkbox              |
|   + paint(): void                                     + paint(): void             |
|       ^              ^                                    ^              ^        |
|       | realizes     | realizes                           | realizes     | rel.   |
|   +---+----+     +---+----+                           +---+----+     +---+----+   |
|   |Windows |     | MacOS  |                           |Windows |     | MacOS  |   |
|   | Button |     | Button |                           |Checkbox|     |Checkbox|   |
|   +--------+     +--------+                           +--------+     +--------+   |
+-----------------------------------------------------------------------------------+
        ^              ^                                    ^              ^
        | creates      | creates                            | creates      | creates
+-----------------------------------------------------------------------------------+
|                            kz.aitu.assignment2.factory                            |
|                                                                                   |
|                               <<interface>>                                       |
|                                GUIFactory                                         |
|                       + createButton(): Button                                    |
|                       + createCheckbox(): Checkbox                                |
|                               ^                  ^                                |
|                               | realizes         | realizes                       |
|                    +----------+-----+      +-----+----------+                     |
|                    | WindowsFactory |      |  MacOSFactory  |                     |
|                    +----------------+      +----------------+                     |
|                    |+createButton() |      |+createButton() |                     |
|                    |+createCheckbox |      |+createCheckbox |                     |
+-----------------------------------------------------------------------------------+
                                         ^
                                         | injected via constructor
                     +-------------------+-------------------+
                     |              kz.aitu.assignment2.app  |
                     |                DeliveryApplication    |
                     |  - button: Button                     |
                     |  - checkbox: Checkbox                 |
                     |  - logistics: Logistics               |
                     |  + DeliveryApplication(GUIFactory, ..)|
                     |  + run(): void                        |
                     +---------------------------------------+
```

#### Detailed Element Mapping:
- **Abstract Products:** `Button` and `Checkbox` interfaces in `kz.aitu.assignment2.ui`.
- **Concrete Product Families:**
  - *Windows Family:* `WindowsButton`, `WindowsCheckbox`.
  - *macOS Family:* `MacOSButton`, `MacOSCheckbox`.
- **Abstract Factory:** `GUIFactory` in `kz.aitu.assignment2.factory` declaring `createButton()` and `createCheckbox()`.
- **Concrete Factories:** `WindowsFactory` (instantiates Windows family) and `MacOSFactory` (instantiates macOS family).
- **Client Dependency:** `DeliveryApplication` receives `GUIFactory` via constructor injection, calls `createButton()` and `createCheckbox()`, and invokes `paint()` without concrete references or type casts.

---

## 4. Clean Code Evidence

Five key practices from Robert C. Martin's *Clean Code* were applied across the implementation:

### Practice 1: Meaningful Names (Clean Code, Chapter 2)
- **Code Excerpt (`RoadLogistics.java`):**
  ```java
  public class RoadLogistics extends Logistics {
      @Override
      public Transport createTransport() {
          return new Truck();
      }
  }
  ```
- **Explanation & Specific Benefit:** Class names (`RoadLogistics`, `Truck`, `Logistics`) explicitly convey their domain purpose and pattern role. The factory method name `createTransport()` unambiguously states its action and return type. Developers reading this code instantly understand the class's intent without needing additional comments or examining bytecode.

### Practice 2: Small Methods with Single Responsibility (Clean Code, Chapter 3)
- **Code Excerpt (`Logistics.java`):**
  ```java
  public void planDelivery(String cargo, String destination) {
      Transport transport = createTransport();
      transport.deliver(cargo, destination);
  }
  ```
- **Explanation & Specific Benefit:** The method performs exactly one distinct operation: it orchestrates the delivery sequence by delegating creation to `createTransport()` and execution to `deliver(...)`. It does not parse user input, validate credentials, or format UI strings. This adherence to the Single Responsibility Principle (SRP) keeps the method concise (3 lines), readable, and easily verifiable.

### Practice 3: Avoid Duplicated Logic / DRY (Clean Code, Chapter 3)
- **Code Excerpt (`Logistics.java` & `SeaLogistics.java`):**
  ```java
  // In abstract creator Logistics:
  public abstract Transport createTransport();

  public void planDelivery(String cargo, String destination) {
      Transport transport = createTransport();
      transport.deliver(cargo, destination);
  }

  // In concrete creator SeaLogistics:
  public class SeaLogistics extends Logistics {
      @Override
      public Transport createTransport() {
          return new Ship();
      }
  }
  ```
- **Explanation & Specific Benefit:** The delivery orchestration algorithm resides solely in the abstract creator `Logistics`. Neither `RoadLogistics` nor `SeaLogistics` duplicates the dispatch logic. If the delivery sequence is extended in the future (e.g., adding shipment logging or GPS tracking), the change is made in exactly one place.

### Practice 4: Data Abstraction (Clean Code, Chapter 6)
- **Code Excerpt (`DeliveryApplication.java`):**
  ```java
  public class DeliveryApplication {
      private final Button button;
      private final Checkbox checkbox;
      private final Logistics logistics;

      public DeliveryApplication(GUIFactory guiFactory, Logistics logistics) {
          this.button = guiFactory.createButton();
          this.checkbox = guiFactory.createCheckbox();
          this.logistics = logistics;
      }
  ```
- **Explanation & Specific Benefit:** Chapter 6 stresses hiding implementation behind abstract interfaces. `DeliveryApplication` interacts exclusively through high-level abstractions (`Button`, `Checkbox`, `Logistics`, `GUIFactory`). It has zero direct dependencies on concrete classes (`WindowsButton`, `Truck`, etc.) and does not inspect or expose concrete internal properties, achieving true data and behavioral abstraction.

### Practice 5: Objects and Encapsulation (Clean Code, Chapter 6)
- **Code Excerpt (`DeliveryApplication.java`):**
  ```java
  public void run(String cargo, String destination) {
      button.paint();
      checkbox.paint();
      logistics.planDelivery(cargo, destination);
  }
  ```
- **Explanation & Specific Benefit:** As Robert C. Martin distinguishes in Chapter 6, objects hide their data behind abstractions and expose behavior. `button` and `checkbox` do not provide getters to expose their label, coordinates, or internal buffers; instead, they expose the behavioral command `paint()`. All instance fields remain strictly `private final`, ensuring strong encapsulation and avoiding procedural data manipulation.

---

## 5. Verification Evidence

All six required checks from Section 6 of the assignment specification, along with missing-input scenarios, were tested and validated.

| Check | Scenario | Input Arguments | Actual Console Output | Result |
| :---: | :--- | :--- | :--- | :---: |
| **1** | Road delivery + Windows UI | `ROAD WINDOWS` | `Delivery mode: ROAD`<br>`UI platform: WINDOWS`<br>`Rendering Windows button`<br>`Rendering Windows checkbox`<br>`Truck delivers laboratory equipment to Aktau warehouse` | **PASS** |
| **2** | Sea delivery + Windows UI | `SEA WINDOWS` | `Delivery mode: SEA`<br>`UI platform: WINDOWS`<br>`Rendering Windows button`<br>`Rendering Windows checkbox`<br>`Ship delivers laboratory equipment to Aktau warehouse by sea` | **PASS** |
| **3** | Road delivery + macOS UI | `ROAD MACOS` | `Delivery mode: ROAD`<br>`UI platform: MACOS`<br>`Rendering macOS button`<br>`Rendering macOS checkbox`<br>`Truck delivers laboratory equipment to Aktau warehouse` | **PASS** |
| **4** | Sea delivery + macOS UI | `SEA MACOS` | `Delivery mode: SEA`<br>`UI platform: MACOS`<br>`Rendering macOS button`<br>`Rendering macOS checkbox`<br>`Ship delivers laboratory equipment to Aktau warehouse by sea` | **PASS** |
| **5** | Unsupported delivery mode with valid platform | `AIR WINDOWS` | `Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA.`<br>*(No delivery workflow constructed or executed)* | **PASS** |
| **6** | Unsupported platform with valid delivery mode | `ROAD LINUX` | `Error: Unsupported UI platform 'LINUX'. Supported platforms: WINDOWS, MACOS.`<br>*(No UI components constructed)* | **PASS** |
| **7** | Missing platform argument | `ROAD` | `Error: Missing UI platform argument. Expected WINDOWS or MACOS.`<br>*(Clean error message, exit status 0)* | **PASS** |
| **8** | Empty input on interactive console | `""` | `Error: Missing required input. Expected delivery mode (ROAD, SEA) and UI platform (WINDOWS, MACOS).`<br>*(No crash or silent fallback)* | **PASS** |

### Automated Test Coverage
All 15 automated test cases in `kz.aitu.assignment2.DeliveryApplicationTest` passed successfully under JDK 17:
```
[INFO] Running kz.aitu.assignment2.DeliveryApplicationTest
[INFO] Tests run: 15, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.162 s
[INFO] BUILD SUCCESS
```

---

## 6. Pattern Comparison & Design Reflection

### 6.1 Pattern Comparison

#### Simple Factory vs. Factory Method
- **Conditional Creation vs. Inheritance:** A Simple Factory consolidates object creation within a single method containing `if-else` or `switch` branches. Adding a new product requires modifying this centralized method, violating the Open/Closed Principle (OCP). Factory Method uses subclassing and inheritance: object creation is deferred to specialized creator subclasses (`RoadLogistics`, `SeaLogistics`), allowing new products to be added simply by creating new subclasses without modifying existing creators.
- **Why Startup Selection is Allowed:** A small `if` or `switch` at startup (in `Main.java`) is necessary to parse runtime arguments and bootstrap the application. This is acceptable because configuration occurs exclusively at the composition root; downstream business logic in `DeliveryApplication` and `Logistics` contains zero conditional type branching.

#### Factory Method vs. Abstract Factory
- **Product Hierarchy vs. Product Family:** Factory Method focuses on creating a single product type (`Transport`) along an inheritance hierarchy. Abstract Factory coordinates families of multiple related or dependent products (`Button` and `Checkbox`).
- **Composition vs. Inheritance:** Factory Method relies on class inheritance (subclasses override a method). Abstract Factory relies on object composition (the client receives a factory object whose interface provides creation operations).
- **Family Consistency:** Abstract Factory guarantees that components from incompatible environments (e.g., Windows and macOS) cannot be accidentally mixed during execution.

---

### 6.2 Design Reflection: System Extensions (Section 7)

#### Extension 1: Adding one more transport (e.g., Air delivery via Plane)
- **New / Modified Classes and Interfaces:**
  1. Create `Plane implements Transport` in `kz.aitu.assignment2.transport` implementing `deliver(String cargo, String destination)`.
  2. Create `AirLogistics extends Logistics` in `kz.aitu.assignment2.logistics` overriding `createTransport()` to return `new Plane()`.
  3. Update startup helper `Main.selectLogistics` to recognize `"AIR"` and instantiate `AirLogistics`.
- **Unchanged Client Logic:** `Logistics.planDelivery(...)` and `DeliveryApplication` remain **100% unchanged**. They continue to consume `Transport` polymorphically.

#### Extension 2: Adding one more UI family (e.g., Linux UI)
- **New / Modified Classes and Interfaces:**
  1. Create `LinuxButton implements Button` in `kz.aitu.assignment2.ui`.
  2. Create `LinuxCheckbox implements Checkbox` in `kz.aitu.assignment2.ui`.
  3. Create `LinuxFactory implements GUIFactory` in `kz.aitu.assignment2.factory` implementing `createButton()` and `createCheckbox()`.
  4. Update startup helper `Main.selectGUIFactory` to recognize `"LINUX"` and instantiate `LinuxFactory`.
- **Unchanged Client Logic:** `DeliveryApplication`, `Button`, and `Checkbox` interfaces remain **100% unchanged**.

#### Extension 3: Adding one more UI product type (e.g., TextField)
- **New / Modified Classes and Interfaces:**
  1. Create new abstract product interface `TextField` with `paint()` in `kz.aitu.assignment2.ui`.
  2. Create concrete products `WindowsTextField implements TextField` and `MacOSTextField implements TextField`.
  3. Modify `GUIFactory` interface to declare `TextField createTextField();`.
  4. Modify `WindowsFactory` and `MacOSFactory` to implement `createTextField()`.
  5. Modify `DeliveryApplication` to call `guiFactory.createTextField()` and render the text field in `run()`.
- **Unchanged Code:** Existing product classes (`WindowsButton`, `MacOSButton`, `WindowsCheckbox`, `MacOSCheckbox`) and the entire `Logistics`/`Transport` hierarchy remain **completely unchanged**.

---

## 7. References

1. Freeman, E., & Robson, E. (2020). *Head First Design Patterns: A Brain-Friendly Guide* (2nd ed.). O'Reilly Media. Chapter 4: The Factory Pattern: Baking with OO Goodness (pp. 109–162).
2. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. Chapter 2 (Meaningful Names, pp. 17–30), Chapter 3 (Functions, pp. 31–52), and Chapter 6 (Objects and Data Structures, pp. 93–102).
3. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley Professional. Creational Patterns: Factory Method (pp. 107–116) and Abstract Factory (pp. 87–96).
4. Oracle Corporation. (2021). *Java Platform, Standard Edition Documentation (JDK 17)*. Oracle Technology Network. https://docs.oracle.com/en/java/javase/17/
