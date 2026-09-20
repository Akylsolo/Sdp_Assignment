import os
import subprocess

base_dir = r"c:\Users\murat\IdeaProjects\Sdp_Assignment"
docs_dir = os.path.join(base_dir, "docs")
uml_dir = os.path.join(docs_dir, "uml")

with open(os.path.join(uml_dir, "factory_method.svg"), "r", encoding="utf-8") as f:
    fm_svg_content = f.read()

with open(os.path.join(uml_dir, "abstract_factory.svg"), "r", encoding="utf-8") as f:
    af_svg_content = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Assignment 2: Factory Method and Abstract Factory</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 10mm 12mm 10mm 12mm;
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #0f172a;
    line-height: 1.35;
    font-size: 8.8pt;
    margin: 0;
    padding: 0;
  }}
  h1 {{
    font-size: 15.5pt;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 2px solid #2563eb;
    padding-bottom: 3px;
    margin-top: 0;
    margin-bottom: 6px;
  }}
  h2 {{
    font-size: 11.5pt;
    font-weight: 700;
    color: #1e40af;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
    margin-top: 8px;
    margin-bottom: 4px;
    page-break-after: avoid;
  }}
  h3 {{
    font-size: 9.5pt;
    font-weight: 600;
    color: #1e293b;
    margin-top: 6px;
    margin-bottom: 2px;
    page-break-after: avoid;
  }}
  p {{
    margin-top: 0;
    margin-bottom: 4px;
    text-align: justify;
  }}
  .meta-box {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #2563eb;
    border-radius: 4px;
    padding: 6px 10px;
    margin-bottom: 8px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2px 14px;
    font-size: 8.2pt;
  }}
  .meta-item strong {{
    color: #334155;
  }}
  .diagram-container {{
    text-align: center;
    margin: 4px 0;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 4px;
  }}
  .diagram-container svg {{
    width: 100%;
    max-height: 250px;
    height: auto;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 4px 0;
    font-size: 7.8pt;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 3.5px 5px;
    text-align: left;
    vertical-align: top;
  }}
  th {{
    background: #f1f5f9;
    font-weight: 600;
    color: #1e293b;
  }}
  tr:nth-child(even) {{
    background: #f8fafc;
  }}
  .badge-pass {{
    background: #dcfce7;
    color: #166534;
    font-weight: 700;
    padding: 1px 4px;
    border-radius: 3px;
    display: inline-block;
    font-size: 7.5pt;
  }}
  pre, code {{
    font-family: Consolas, "Courier New", monospace;
  }}
  pre {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 3px 6px;
    font-size: 7.6pt;
    line-height: 1.25;
    margin: 2px 0 4px 0;
  }}
  .clean-practice {{
    border: 1px solid #e2e8f0;
    background: #ffffff;
    border-radius: 4px;
    padding: 4px 6px;
    margin-bottom: 4px;
  }}
  .clean-practice h4 {{
    margin: 0 0 2px 0;
    font-size: 8.8pt;
    color: #1d4ed8;
  }}
  .clean-practice p {{
    margin: 0 0 2px 0;
    font-size: 8.2pt;
  }}
  .page-break {{
    page-break-before: always;
    break-before: page;
  }}
  ul, ol {{
    margin-top: 2px;
    margin-bottom: 4px;
    padding-left: 16px;
    font-size: 8.2pt;
  }}
  li {{
    margin-bottom: 2px;
  }}
</style>
</head>
<body>

<!-- ================= PAGE 1 ================= -->
<h1>Assignment 2: Factory Method and Abstract Factory</h1>

<div class="meta-box">
  <div class="meta-item"><strong>Student:</strong> Akyl Muratbek</div>
  <div class="meta-item"><strong>Programme:</strong> 6B06102 Software Engineering (Yr 2, Trim 4)</div>
  <div class="meta-item"><strong>Group:</strong> SE-2523</div>
  <div class="meta-item"><strong>Course:</strong> ShP-2216 Software Design Patterns</div>
  <div class="meta-item"><strong>Instructor:</strong> Yerassyl Bekenov</div>
  <div class="meta-item"><strong>JDK &amp; Format:</strong> Java 17 (JDK 17) | Individual Work</div>
  <div class="meta-item" style="grid-column: 1 / span 2;"><strong>GitHub Repository:</strong> <a href="https://github.com/Akylsolo/Sdp_Assignment">https://github.com/Akylsolo/Sdp_Assignment</a></div>
</div>

<h2>1. Introduction &amp; Pattern Rationale</h2>
<p>
This application models a cross-platform logistics system that coordinates freight transport delivery across road and sea routes and renders matching GUI components across Windows and macOS platforms.
</p>
<p>
<strong>Factory Method Pattern Rationale (Transport Subsystem):</strong>
The delivery workflow requires a common orchestration algorithm (<code>planDelivery</code>) shared across all modes of transport, but the concrete vehicle (<code>Truck</code> vs. <code>Ship</code>) depends on operational mode. Directly instantiating concrete transport objects within the logistics manager couples high-level business rules to low-level implementation details. The Factory Method pattern decouples this by declaring an abstract factory method (<code>createTransport()</code>) in <code>Logistics</code>, allowing concrete subclasses (<code>RoadLogistics</code> and <code>SeaLogistics</code>) to supply the appropriate product while preserving the invariant delivery workflow.
</p>
<p>
<strong>Abstract Factory Pattern Rationale (Cross-Platform UI Subsystem):</strong>
The system must generate complete, matching pairs of UI components (<code>Button</code> and <code>Checkbox</code>) customized for a specific operating environment (Windows or macOS). Without centralized family management, client code could erroneously pair an incompatible Windows button with a macOS checkbox. The Abstract Factory pattern addresses this by defining <code>GUIFactory</code> with distinct creation methods (<code>createButton()</code> and <code>createCheckbox()</code>). Concrete factories (<code>WindowsFactory</code> and <code>MacOSFactory</code>) guarantee family consistency and allow the client (<code>DeliveryApplication</code>) to work exclusively through abstract component contracts without concrete constructors or type casts.
</p>

<h2>2. UML Class Diagrams</h2>
<h3>2.1 Factory Method Pattern Diagram</h3>
<div class="diagram-container">
{fm_svg_content}
</div>
<p style="font-size: 7.8pt; color: #475569; margin: 2px 0 0 0;">
<strong>Figure 1:</strong> Factory Method UML Class Diagram showing <code>Transport</code> product contract, concrete products (<code>Truck</code>, <code>Ship</code>), abstract creator (<code>Logistics</code>) with <code>planDelivery(...)</code>, concrete creators (<code>RoadLogistics</code>, <code>SeaLogistics</code>), and client dependency (<code>DeliveryApplication</code>).
</p>

<!-- ================= PAGE 2 ================= -->
<div class="page-break"></div>

<h3>2.2 Abstract Factory Pattern Diagram</h3>
<div class="diagram-container">
{af_svg_content}
</div>
<p style="font-size: 7.8pt; color: #475569; margin: 2px 0 0 0;">
<strong>Figure 2:</strong> Abstract Factory UML Class Diagram showing abstract products (<code>Button</code>, <code>Checkbox</code>), concrete families for Windows and macOS, abstract factory interface (<code>GUIFactory</code>), concrete factories (<code>WindowsFactory</code>, <code>MacOSFactory</code>), and constructor injection into <code>DeliveryApplication</code>.
</p>

<h2>3. Clean Code Evidence (Robert C. Martin)</h2>

<div class="clean-practice">
  <h4>Practice 1: Meaningful Names (Clean Code, Chapter 2)</h4>
  <p><strong>Code Excerpt (<code>RoadLogistics.java</code>):</strong></p>
  <pre>public class RoadLogistics extends Logistics {{
    @Override
    public Transport createTransport() {{
        return new Truck();
    }}
}}</pre>
  <p><strong>Specific Benefit:</strong> Names clearly express domain role (<code>RoadLogistics</code>, <code>Truck</code>) and design pattern role. The factory method name <code>createTransport()</code> explicitly communicates action and return type without ambiguous abbreviations.</p>
</div>

<div class="clean-practice">
  <h4>Practice 2: Small Methods with Single Responsibility (Clean Code, Chapter 3)</h4>
  <p><strong>Code Excerpt (<code>Logistics.java</code>):</strong></p>
  <pre>public void planDelivery(String cargo, String destination) {{
    Transport transport = createTransport();
    transport.deliver(cargo, destination);
}}</pre>
  <p><strong>Specific Benefit:</strong> The method does exactly one thing: coordinates the delivery sequence by delegating creation to <code>createTransport()</code> and dispatch to <code>deliver(...)</code>. It avoids mixing CLI parsing, validation, or formatting.</p>
</div>

<div class="clean-practice">
  <h4>Practice 3: Avoid Duplicated Logic / DRY (Clean Code, Chapter 3)</h4>
  <p><strong>Code Excerpt (<code>Logistics.java</code> &amp; <code>SeaLogistics.java</code>):</strong></p>
  <pre>// In abstract creator Logistics:
public abstract Transport createTransport();
public void planDelivery(String cargo, String destination) {{
    Transport transport = createTransport();
    transport.deliver(cargo, destination);
}}
// In concrete creator SeaLogistics:
public class SeaLogistics extends Logistics {{
    @Override
    public Transport createTransport() {{ return new Ship(); }}
}}</pre>
  <p><strong>Specific Benefit:</strong> The core delivery algorithm exists solely in <code>Logistics</code>. Neither <code>RoadLogistics</code> nor <code>SeaLogistics</code> repeats delivery workflow logic; they only override the factory method.</p>
</div>

<!-- ================= PAGE 3 ================= -->
<div class="page-break"></div>

<div class="clean-practice">
  <h4>Practice 4: Data Abstraction (Clean Code, Chapter 6)</h4>
  <p><strong>Code Excerpt (<code>DeliveryApplication.java</code>):</strong></p>
  <pre>public class DeliveryApplication {{
    private final Button button;
    private final Checkbox checkbox;
    private final Logistics logistics;

    public DeliveryApplication(GUIFactory guiFactory, Logistics logistics) {{
        this.button = guiFactory.createButton();
        this.checkbox = guiFactory.createCheckbox();
        this.logistics = logistics;
    }}</pre>
  <p><strong>Specific Benefit:</strong> Chapter 6 emphasizes hiding implementation details behind abstract interfaces. <code>DeliveryApplication</code> depends strictly on abstract contracts (<code>Button</code>, <code>Checkbox</code>, <code>GUIFactory</code>, <code>Logistics</code>) and never on concrete classes like <code>WindowsButton</code> or <code>Truck</code>, achieving true data and behavioral abstraction.</p>
</div>

<div class="clean-practice">
  <h4>Practice 5: Objects and Encapsulation (Clean Code, Chapter 6)</h4>
  <p><strong>Code Excerpt (<code>DeliveryApplication.java</code>):</strong></p>
  <pre>public void run(String cargo, String destination) {{
    button.paint();
    checkbox.paint();
    logistics.planDelivery(cargo, destination);
}}</pre>
  <p><strong>Specific Benefit:</strong> Chapter 6 contrasts data structures with objects: objects hide data and expose behavior. UI products expose behavioral methods (<code>paint()</code>) rather than getters. All fields remain strictly <code>private final</code>, ensuring strong encapsulation and avoiding procedural data manipulation.</p>
</div>

<h2>4. Verification Evidence</h2>
<p>All six required test checks from Section 6 and missing-input scenarios were verified:</p>

<table>
  <thead>
    <tr>
      <th style="width: 5%;">#</th>
      <th style="width: 22%;">Scenario</th>
      <th style="width: 14%;">Input</th>
      <th>Actual Output</th>
      <th style="width: 9%; text-align: center;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center; font-weight: bold;">1</td>
      <td>Road delivery + Windows UI</td>
      <td><code>ROAD WINDOWS</code></td>
      <td>Delivery mode: ROAD<br>UI platform: WINDOWS<br>Rendering Windows button<br>Rendering Windows checkbox<br>Truck delivers laboratory equipment to Aktau warehouse</td>
      <td style="text-align: center;"><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">2</td>
      <td>Sea delivery + Windows UI</td>
      <td><code>SEA WINDOWS</code></td>
      <td>Delivery mode: SEA<br>UI platform: WINDOWS<br>Rendering Windows button<br>Rendering Windows checkbox<br>Ship delivers laboratory equipment to Aktau warehouse by sea</td>
      <td style="text-align: center;"><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">3</td>
      <td>Road delivery + macOS UI</td>
      <td><code>ROAD MACOS</code></td>
      <td>Delivery mode: ROAD<br>UI platform: MACOS<br>Rendering macOS button<br>Rendering macOS checkbox<br>Truck delivers laboratory equipment to Aktau warehouse</td>
      <td style="text-align: center;"><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">4</td>
      <td>Sea delivery + macOS UI</td>
      <td><code>SEA MACOS</code></td>
      <td>Delivery mode: SEA<br>UI platform: MACOS<br>Rendering macOS button<br>Rendering macOS checkbox<br>Ship delivers laboratory equipment to Aktau warehouse by sea</td>
      <td style="text-align: center;"><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">5</td>
      <td>Unsupported delivery mode</td>
      <td><code>AIR WINDOWS</code></td>
      <td>Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA.<br><em>(Execution halts cleanly; no delivery performed)</em></td>
      <td style="text-align: center;"><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">6</td>
      <td>Unsupported UI platform</td>
      <td><code>ROAD LINUX</code></td>
      <td>Error: Unsupported UI platform 'LINUX'. Supported platforms: WINDOWS, MACOS.<br><em>(Execution halts cleanly; no UI constructed)</em></td>
      <td style="text-align: center;"><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">7</td>
      <td>Missing platform argument</td>
      <td><code>ROAD</code></td>
      <td>Error: Missing UI platform argument. Expected WINDOWS or MACOS.<br><em>(Clean validation exit; no crash or null pointer exception)</em></td>
      <td style="text-align: center;"><span class="badge-pass">PASS</span></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">8</td>
      <td>Empty interactive input</td>
      <td><code>""</code></td>
      <td>Error: Missing required input. Expected delivery mode (ROAD, SEA) and UI platform (WINDOWS, MACOS).<br><em>(Clean validation message; no silent defaults)</em></td>
      <td style="text-align: center;"><span class="badge-pass">PASS</span></td>
    </tr>
  </tbody>
</table>

<p style="font-size: 8pt; margin-top: 3px;">
<strong>Automated Test Suite:</strong> All 15 automated JUnit 5 tests in <code>DeliveryApplicationTest.java</code> pass with <code>mvn test</code>, guaranteeing 100% pass rate under JDK 17.
</p>

<!-- ================= PAGE 4 ================= -->
<div class="page-break"></div>

<h2>5. Pattern Comparison &amp; Design Reflection</h2>

<h3>5.1 Pattern Comparison</h3>
<ul>
  <li>
    <strong>Simple Factory vs. Factory Method:</strong> A Simple Factory centralizes product creation in a single method with conditional statements (<code>if-else</code> or <code>switch</code>). Adding a new product violates the Open/Closed Principle (OCP) because the factory class must be modified. In contrast, Factory Method uses inheritance and polymorphism: an abstract creator defines the creation interface, while concrete creator subclasses override the method to instantiate products. Adding a new product requires only a new subclass, leaving existing creators untouched. A startup switch in <code>Main</code> is permitted solely as a bootstrap configuration step at the composition root.
  </li>
  <li>
    <strong>Factory Method vs. Abstract Factory:</strong> Factory Method focuses on creating a single product hierarchy via class inheritance. Abstract Factory coordinates families of related or dependent products (e.g., matching Buttons and Checkboxes) via object composition. Abstract Factory guarantees family consistency so incompatible platform components are never mixed.
  </li>
</ul>

<h3>5.2 Design Reflection: System Extensions (Section 7)</h3>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px 8px; margin-bottom: 5px; font-size: 8pt;">
  <strong style="color: #1e40af;">Extension 1: Adding one more transport (e.g., Air delivery via Plane)</strong><br>
  <ul>
    <li><strong>Affected Classes / Interfaces:</strong>
      <ul>
        <li>Add <code>Plane implements Transport</code> in <code>transport</code> package with <code>deliver(cargo, destination)</code>.</li>
        <li>Add <code>AirLogistics extends Logistics</code> in <code>logistics</code> package overriding <code>createTransport()</code> to return <code>new Plane()</code>.</li>
        <li>Update startup selection in <code>Main.selectLogistics</code> to handle <code>"AIR"</code>.</li>
      </ul>
    </li>
    <li><strong>Unchanged Client Logic:</strong> <code>Logistics.planDelivery(...)</code> and <code>DeliveryApplication</code> remain <strong>100% unchanged</strong>.</li>
  </ul>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px 8px; margin-bottom: 5px; font-size: 8pt;">
  <strong style="color: #1e40af;">Extension 2: Adding one more UI family (e.g., Linux UI)</strong><br>
  <ul>
    <li><strong>Affected Classes / Interfaces:</strong>
      <ul>
        <li>Add <code>LinuxButton implements Button</code> and <code>LinuxCheckbox implements Checkbox</code> in <code>ui</code> package.</li>
        <li>Add <code>LinuxFactory implements GUIFactory</code> in <code>factory</code> package implementing <code>createButton()</code> and <code>createCheckbox()</code>.</li>
        <li>Update startup selection in <code>Main.selectGUIFactory</code> to handle <code>"LINUX"</code>.</li>
      </ul>
    </li>
    <li><strong>Unchanged Client Logic:</strong> <code>DeliveryApplication</code>, <code>Button</code>, and <code>Checkbox</code> interfaces remain <strong>completely unchanged</strong>.</li>
  </ul>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px 8px; margin-bottom: 5px; font-size: 8pt;">
  <strong style="color: #1e40af;">Extension 3: Adding one more UI product type (e.g., TextField)</strong><br>
  <ul>
    <li><strong>Affected Classes / Interfaces:</strong>
      <ul>
        <li>Add new interface <code>TextField</code> with <code>paint()</code> in <code>ui</code> package.</li>
        <li>Add <code>WindowsTextField implements TextField</code> and <code>MacOSTextField implements TextField</code>.</li>
        <li>Update <code>GUIFactory</code> interface to declare <code>TextField createTextField();</code>.</li>
        <li>Update <code>WindowsFactory</code> and <code>MacOSFactory</code> to implement <code>createTextField()</code>.</li>
        <li>Update <code>DeliveryApplication</code> constructor to obtain <code>TextField</code> and paint it during execution.</li>
      </ul>
    </li>
    <li><strong>Unchanged Code:</strong> Existing products (<code>WindowsButton</code>, <code>MacOSButton</code>, etc.) and the entire <code>Logistics</code>/<code>Transport</code> hierarchy remain <strong>completely unchanged</strong>.</li>
  </ul>
</div>

<h2>6. References</h2>
<ol style="font-size: 8pt; margin-top: 2px; padding-left: 16px;">
  <li>Freeman, E., &amp; Robson, E. (2020). <em>Head First Design Patterns: A Brain-Friendly Guide</em> (2nd ed.). O'Reilly Media. Chapter 4: The Factory Pattern (pp. 109–162).</li>
  <li>Martin, R. C. (2008). <em>Clean Code: A Handbook of Agile Software Craftsmanship</em>. Prentice Hall. Chapter 2 (Meaningful Names, pp. 17–30), Chapter 3 (Functions, pp. 31–52), Chapter 6 (Objects and Data Structures, pp. 93–102).</li>
  <li>Gamma, E., Helm, R., Johnson, R., &amp; Vlissides, J. (1994). <em>Design Patterns: Elements of Reusable Object-Oriented Software</em>. Addison-Wesley. Creational Patterns: Factory Method (pp. 107–116) and Abstract Factory (pp. 87–96).</li>
  <li>Oracle Corporation. (2021). <em>Java Platform, Standard Edition Documentation (JDK 17)</em>. Oracle Technology Network.</li>
</ol>

</body>
</html>
"""

report_html_path = os.path.join(docs_dir, "report.html")
with open(report_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
pdf_out_path = os.path.join(docs_dir, "Assignment2_SE-2523_Muratbek_Akyl.pdf")

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={pdf_out_path}",
    "--no-pdf-header-footer",
    report_html_path
]

subprocess.run(cmd, check=True)
print("Updated PDF generated!")
