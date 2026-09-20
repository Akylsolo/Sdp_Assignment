# Assignment 2: Factory Method and Abstract Factory

**Course:** ShP-2216 Software Design Patterns  
**Programme:** 6B06102 Software Engineering | Year 2, Trimester 4  
**Institution:** Astana IT University | School of Software Engineering  
**Instructor:** Yerassyl Bekenov  
**Student:** Akyl Muratbek (Group: SE-2523)  
**Target Environment:** Java 17 (JDK 17), Maven  

---

## 1. Project Purpose

This project demonstrates the practical application and synergy of two foundational Gang of Four (GoF) creational design patterns in a unified logistics console application:

1. **Factory Method Pattern (Part A):** Manages transport selection and logistics delivery workflows. An abstract creator (`Logistics`) defines a template algorithm (`planDelivery`), delegating concrete transport instantiation (`Truck` vs `Ship`) to creator subclasses (`RoadLogistics` vs `SeaLogistics`).
2. **Abstract Factory Pattern (Part B):** Manages multi-component user interface families. An abstract factory interface (`GUIFactory`) guarantees that related UI controls (`Button` and `Checkbox`) are created consistently for a target operating system platform (`WindowsFactory` creates Windows controls, `MacOSFactory` creates macOS controls) without the client ever depending on concrete classes.

Both patterns operate concurrently in the same runtime application (`DeliveryApplication`).

---

## 2. Package & Directory Structure

```
Sdp_Assignment/
├── pom.xml                                   # Maven project configuration (JDK 17, JUnit 5)
├── README.md                                 # Comprehensive build, run, and usage instructions
├── DEFENSE_GUIDE.md                          # Defense preparation cheat sheet for full 50/50 score
├── docs/
│   ├── REPORT.md                             # Complete markdown report matching grading rubric
│   ├── Assignment2_SE-2523_Muratbek_Akyl.pdf # Official generated submission PDF
│   └── uml/
│       ├── factory_method.puml               # PlantUML source for Factory Method
│       ├── factory_method.svg                # Scalable vector diagram for Factory Method
│       ├── abstract_factory.puml              # PlantUML source for Abstract Factory
│       └── abstract_factory.svg               # Scalable vector diagram for Abstract Factory
└── src/
    ├── main/java/kz/aitu/assignment2/
    │   ├── Main.java                         # Application entry point, CLI & interactive runner
    │   ├── transport/
    │   │   ├── Transport.java                # [Product] Interface for transport delivery
    │   │   ├── Truck.java                    # [ConcreteProduct] Road delivery
    │   │   └── Ship.java                     # [ConcreteProduct] Sea delivery
    │   ├── logistics/
    │   │   ├── Logistics.java                # [Creator] Abstract class with planDelivery()
    │   │   ├── RoadLogistics.java            # [ConcreteCreator] Creates Truck
    │   │   └── SeaLogistics.java             # [ConcreteCreator] Creates Ship
    │   ├── ui/
    │   │   ├── Button.java                   # [AbstractProduct A] UI Button contract
    │   │   ├── Checkbox.java                 # [AbstractProduct B] UI Checkbox contract
    │   │   ├── WindowsButton.java            # [ConcreteProduct A1] Windows button
    │   │   ├── WindowsCheckbox.java          # [ConcreteProduct B1] Windows checkbox
    │   │   ├── MacOSButton.java              # [ConcreteProduct A2] macOS button
    │   │   └── MacOSCheckbox.java            # [ConcreteProduct B2] macOS checkbox
    │   ├── factory/
    │   │   ├── GUIFactory.java               # [AbstractFactory] Declares UI creation methods
    │   │   ├── WindowsFactory.java           # [ConcreteFactory 1] Produces Windows family
    │   │   └── MacOSFactory.java             # [ConcreteFactory 2] Produces macOS family
    │   └── app/
    │       └── DeliveryApplication.java      # [Client] Coordinates UI rendering & delivery
    └── test/java/kz/aitu/assignment2/
        └── DeliveryApplicationTest.java      # JUnit 5 suite testing all 6 rubric checks & edge cases
```

---

## 3. Prerequisites

- **Java Development Kit:** JDK 17 or higher (configured for release 17 compatibility).
- **Build Tool:** Apache Maven 3.8+ (or IntelliJ IDEA Maven wrapper).
- **Operating System:** Platform independent (Windows, macOS, Linux). Note: running macOS components does **not** require a physical macOS machine.

---

## 4. Build Instructions

To clean, compile, and run all 15 automated JUnit 5 tests:

```bash
mvn clean test
```

To package the application into an executable JAR:

```bash
mvn clean package
```
The compiled JAR will be placed at `target/sdp-assignment2-1.0-SNAPSHOT.jar`.

---

## 5. Exact Run Instructions

The application supports both **command-line arguments** and **interactive console input**.

### Option A: Running via Maven Exec Plugin
```bash
# General syntax: mvn exec:java -Dexec.args="<MODE> <PLATFORM>"
mvn exec:java -Dexec.args="ROAD WINDOWS"
mvn exec:java -Dexec.args="SEA MACOS"
```

### Option B: Running the Packaged JAR
```bash
# Syntax: java -jar target/sdp-assignment2-1.0-SNAPSHOT.jar <MODE> <PLATFORM>
java -jar target/sdp-assignment2-1.0-SNAPSHOT.jar ROAD WINDOWS
java -jar target/sdp-assignment2-1.0-SNAPSHOT.jar SEA WINDOWS
java -jar target/sdp-assignment2-1.0-SNAPSHOT.jar ROAD MACOS
java -jar target/sdp-assignment2-1.0-SNAPSHOT.jar SEA MACOS
```

### Option C: Running via Compiled Classes
```bash
java -cp target/classes kz.aitu.assignment2.Main ROAD WINDOWS
```

### Option D: Interactive Console Fallback
If run without command-line arguments, the application prompts interactively:
```bash
java -cp target/classes kz.aitu.assignment2.Main
# Prompts:
# Enter delivery mode (ROAD, SEA): ROAD
# Enter UI platform (WINDOWS, MACOS): WINDOWS
```

---

## 6. Supported Input Values & Validation

| Parameter | Supported Values (Case-Insensitive) | Validation Behavior on Invalid/Missing Input |
| :--- | :--- | :--- |
| **Delivery Mode** | `ROAD`, `SEA` | Rejects unsupported values with `Error: Unsupported delivery mode '<mode>'. Supported modes: ROAD, SEA.` No delivery workflow executed. |
| **UI Platform** | `WINDOWS`, `MACOS` | Rejects unsupported values with `Error: Unsupported UI platform '<platform>'. Supported platforms: WINDOWS, MACOS.` No UI components constructed. |
| **Missing Inputs** | `ROAD` (missing platform) or empty string | Prints clear error message and halts cleanly without silent fallback or null pointer exceptions. |

---

## 7. Sample Runs

### Valid Execution (ROAD + WINDOWS)
```
$ java -cp target/classes kz.aitu.assignment2.Main ROAD WINDOWS
Delivery mode: ROAD
UI platform: WINDOWS
Rendering Windows button
Rendering Windows checkbox
Truck delivers laboratory equipment to Aktau warehouse
```

### Valid Execution (SEA + MACOS)
```
$ java -cp target/classes kz.aitu.assignment2.Main SEA MACOS
Delivery mode: SEA
UI platform: MACOS
Rendering macOS button
Rendering macOS checkbox
Ship delivers laboratory equipment to Aktau warehouse by sea
```

### Invalid Delivery Mode (AIR + WINDOWS)
```
$ java -cp target/classes kz.aitu.assignment2.Main AIR WINDOWS
Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA.
```

### Invalid UI Platform (ROAD + LINUX)
```
$ java -cp target/classes kz.aitu.assignment2.Main ROAD LINUX
Error: Unsupported UI platform 'LINUX'. Supported platforms: WINDOWS, MACOS.
```

---

## 8. Verification Results (Section 6 Checks)

| Check | Input | Expected Result | Actual Result | Status |
| :---: | :--- | :--- | :--- | :---: |
| **1** | `ROAD WINDOWS` | Truck delivery; Windows button and checkbox | Matches expected console output | **PASS** |
| **2** | `SEA WINDOWS` | Ship delivery; Windows button and checkbox | Matches expected console output | **PASS** |
| **3** | `ROAD MACOS` | Truck delivery; macOS button and checkbox | Matches expected console output | **PASS** |
| **4** | `SEA MACOS` | Ship delivery; macOS button and checkbox | Matches expected console output | **PASS** |
| **5** | `AIR WINDOWS` | Clear validation error; no delivery | Clean error on stderr, no delivery | **PASS** |
| **6** | `ROAD LINUX` | Clear validation error; no UI construction | Clean error on stderr, no UI created | **PASS** |
| **7** | `ROAD` (missing) | Clear validation error for missing platform | Clean error message, exit 0 | **PASS** |
| **8** | Empty input `""` | Clear validation error for missing inputs | Clean error message, exit 0 | **PASS** |
