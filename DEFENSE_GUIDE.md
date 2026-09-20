# Individual Defense Preparation Guide (50 / 50 Points)

This guide prepares you for the individual oral defense with instructor Yerassyl Bekenov. The defense is worth **50 points** (50% of the grade). It directly maps each rubric criterion (D1 to D6) to the code, definitions, and exact answers.

---

## D1: Factory Method Roles (10 Points)

You must explain each role conceptually and show the exact file and lines of code.

### 1. Product (`Transport.java`)
- **Definition:** An interface or abstract class defining the contract for objects created by the factory method.
- **In our code:** [Transport.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/transport/Transport.java)
  ```java
  public interface Transport {
      void deliver(String cargo, String destination);
  }
  ```
- **Explanation:** All transports must satisfy this delivery contract.

### 2. Concrete Products (`Truck.java`, `Ship.java`)
- **Definition:** Implementations of the Product interface with distinct behaviors.
- **In our code:**
  - [Truck.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/transport/Truck.java): prints `"Truck delivers " + cargo + " to " + destination`
  - [Ship.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/transport/Ship.java): prints `"Ship delivers " + cargo + " to " + destination + " by sea"`

### 3. Creator (`Logistics.java`)
- **Definition:** An abstract class declaring the factory method `createTransport()` returning `Transport`, and providing a shared template method `planDelivery(...)` that contains core business logic.
- **In our code:** [Logistics.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/logistics/Logistics.java)
  ```java
  public abstract class Logistics {
      public abstract Transport createTransport();

      public void planDelivery(String cargo, String destination) {
          Transport transport = createTransport();
          transport.deliver(cargo, destination);
      }
  }
  ```

### 4. Concrete Creators (`RoadLogistics.java`, `SeaLogistics.java`)
- **Definition:** Subclasses that override the factory method to return a specific concrete product.
- **In our code:**
  - [RoadLogistics.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/logistics/RoadLogistics.java): overrides `createTransport()` to return `new Truck()`
  - [SeaLogistics.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/logistics/SeaLogistics.java): overrides `createTransport()` to return `new Ship()`

### 5. Runtime Path from `planDelivery(...)` to Delivery
- **Trace the call:**
  1. Caller invokes `logistics.planDelivery(cargo, destination)`.
  2. Inside `planDelivery`, Java polymorphically calls `createTransport()`.
  3. If runtime instance is `RoadLogistics`, it instantiates and returns `Truck`. If `SeaLogistics`, it returns `Ship`.
  4. `planDelivery` then invokes `transport.deliver(cargo, destination)` through the `Transport` interface.
  5. The concrete `deliver` method executes and prints the delivery confirmation.

---

## D2: Abstract Factory Roles (10 Points)

### 1. Abstract Products (`Button.java`, `Checkbox.java`)
- **Definition:** Interfaces for distinct families of related products.
- **In our code:**
  - [Button.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/ui/Button.java): declares `void paint();`
  - [Checkbox.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/ui/Checkbox.java): declares `void paint();`

### 2. Concrete Products Grouped into Families
- **Definition:** Concrete implementations grouped by platform variant.
- **Windows Family:**
  - [WindowsButton.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/ui/WindowsButton.java) (prints `"Rendering Windows button"`)
  - [WindowsCheckbox.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/ui/WindowsCheckbox.java) (prints `"Rendering Windows checkbox"`)
- **macOS Family:**
  - [MacOSButton.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/ui/MacOSButton.java) (prints `"Rendering macOS button"`)
  - [MacOSCheckbox.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/ui/MacOSCheckbox.java) (prints `"Rendering macOS checkbox"`)

### 3. Abstract Factory (`GUIFactory.java`)
- **Definition:** An interface declaring creation methods for each abstract product.
- **In our code:** [GUIFactory.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/factory/GUIFactory.java)
  ```java
  public interface GUIFactory {
      Button createButton();
      Checkbox createCheckbox();
  }
  ```

### 4. Concrete Factories (`WindowsFactory.java`, `MacOSFactory.java`)
- **Definition:** Concrete classes implementing creation operations to produce a full family of matching products.
- **In our code:**
  - [WindowsFactory.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/factory/WindowsFactory.java): creates `WindowsButton` and `WindowsCheckbox`.
  - [MacOSFactory.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/factory/MacOSFactory.java): creates `MacOSButton` and `MacOSCheckbox`.

### 5. Client (`DeliveryApplication.java`)
- **Definition:** Receives the abstract factory and creator via constructor injection. Interacts solely through interfaces without using concrete constructors (`new WindowsButton()`) or type casts (`(WindowsButton) button`).
- **In our code:** [DeliveryApplication.java](file:///c:/Users/murat/IdeaProjects/Sdp_Assignment/src/main/java/kz/aitu/assignment2/app/DeliveryApplication.java)

---

## D3: Comparison and Extension Decisions (15 Points)

### 1. Simple Factory vs. Factory Method
- **Simple Factory:** Has a single method containing `if/else` or `switch` to instantiate classes based on an argument. Violates the Open/Closed Principle (OCP) because adding a product modifies existing source code.
- **Factory Method:** Defer object instantiation to subclasses via inheritance and overriding. Adding a product requires only adding a new subclass without modifying existing creator code.
- **Why startup selection in `Main` is allowed:** Startup selection in `Main.java` is the **Composition Root** (bootstrap configuration). It chooses the creators/factories at launch from CLI arguments. Downstream business logic contains zero conditional branching.

### 2. Factory Method vs. Abstract Factory
- **Hierarchy vs. Family:** Factory Method creates a single product hierarchy (`Transport`). Abstract Factory creates a whole family of related products (`Button` + `Checkbox`).
- **Inheritance vs. Composition:** Factory Method relies on class inheritance (subclass overrides `createTransport()`). Abstract Factory relies on object composition (client holds a reference to `GUIFactory` and delegates calls).
- **Family Consistency:** Abstract Factory guarantees that components from incompatible families (e.g., Windows and macOS) are never accidentally mixed together.

### 3. System Extensions (Section 7)
- **Extension 1: Adding one more transport (e.g., Plane / AirLogistics):**
  - Create `Plane implements Transport`
  - Create `AirLogistics extends Logistics`
  - Add `"AIR"` branch to startup helper `Main.selectLogistics`
  - **Unchanged:** `Logistics.planDelivery` and `DeliveryApplication` remain 100% untouched.
- **Extension 2: Adding one more UI family (e.g., Linux UI):**
  - Create `LinuxButton implements Button` and `LinuxCheckbox implements Checkbox`
  - Create `LinuxFactory implements GUIFactory`
  - Add `"LINUX"` branch to startup helper `Main.selectGUIFactory`
  - **Unchanged:** `DeliveryApplication`, `Button`, and `Checkbox` remain 100% untouched.
- **Extension 3: Adding one more UI product type (e.g., TextField):**
  - Create `TextField` interface with `paint()`
  - Create `WindowsTextField` and `MacOSTextField`
  - Add `TextField createTextField();` to `GUIFactory`
  - Implement `createTextField()` in `WindowsFactory` and `MacOSFactory`
  - Update `DeliveryApplication` to call `guiFactory.createTextField()` and `textField.paint()`
  - **Unchanged:** Existing button and checkbox classes, and all logistics/transport classes remain 100% untouched.

---

## D4: Live Demonstration (5 Points)

Have these commands ready in your terminal:

```bash
# Check 1: ROAD + WINDOWS
java -cp target/classes kz.aitu.assignment2.Main ROAD WINDOWS

# Check 2: SEA + WINDOWS
java -cp target/classes kz.aitu.assignment2.Main SEA WINDOWS

# Check 3: ROAD + MACOS
java -cp target/classes kz.aitu.assignment2.Main ROAD MACOS

# Check 4: SEA + MACOS
java -cp target/classes kz.aitu.assignment2.Main SEA MACOS

# Check 5: Unsupported delivery mode
java -cp target/classes kz.aitu.assignment2.Main AIR WINDOWS

# Check 6: Unsupported UI platform
java -cp target/classes kz.aitu.assignment2.Main ROAD LINUX

# Check 7: Missing argument
java -cp target/classes kz.aitu.assignment2.Main ROAD
```

---

## D5: Code Explanation Questions (5 Points)

The instructor may pick any method (e.g., `Logistics.planDelivery` or `Main.main` or `DeliveryApplication.run`) and ask:
- **Purpose:** "What is the role of this method?"
- **Inputs & Output:** "What arguments does it take and what does it return?"
- **Control Flow:** "Walk me line-by-line through what happens."
- **Collaborating Objects:** "What interfaces/classes does this method talk to?"
- **Hypothetical Change:** "What would happen if we changed X?"
  - *Example:* "What happens if `createTransport()` returns null?" -> `NullPointerException` on `transport.deliver()`. That's why factory methods must return a valid instance or throw an exception.

---

## D6: Clean Code Justification (5 Points)

You must explain 5 Clean Code practices, including 2 from Chapter 6:
1. **Meaningful Names (Chapter 2):** Domain and pattern roles in class/method names (`RoadLogistics`, `Truck`, `createTransport`).
2. **Small Methods (Chapter 3):** Methods do one thing (`planDelivery` is 3 lines).
3. **Avoid Duplicated Logic / DRY (Chapter 3):** Shared delivery algorithm is in `Logistics`, not duplicated in subclasses.
4. **Data Abstraction (Chapter 6):** `DeliveryApplication` interacts exclusively through abstract interfaces (`Button`, `Checkbox`, `GUIFactory`, `Logistics`) without exposing concrete data structures.
5. **Objects and Encapsulation (Chapter 6):** Objects hide internal data and expose behavior (`paint()`, `deliver()`). Fields are `private final`. No unnecessary getters or procedural data manipulation.
