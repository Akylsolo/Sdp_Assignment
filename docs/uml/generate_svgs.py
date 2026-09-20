import os

fm_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 560" width="100%" height="100%" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000000" flood-opacity="0.10"/>
    </filter>
    <marker id="triangle" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="10" markerHeight="10" orient="auto-start-reverse">
      <polygon points="0,0 10,5 0,10" fill="#ffffff" stroke="#333333" stroke-width="1.5"/>
    </marker>
    <marker id="open-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <polyline points="0,1 9,5 0,9" fill="none" stroke="#333333" stroke-width="1.5"/>
    </marker>
    <marker id="green-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <polyline points="0,1 9,5 0,9" fill="none" stroke="#059669" stroke-width="1.5"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="480" y="32" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f172a">Factory Method Pattern — Class Structure &amp; Roles</text>

  <!-- Package kz.aitu.assignment2.transport -->
  <rect x="30" y="60" width="430" height="330" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4" filter="url(#shadow)"/>
  <rect x="30" y="60" width="220" height="24" rx="4" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="40" y="77" font-size="11" font-weight="bold" fill="#334155">kz.aitu.assignment2.transport</text>

  <!-- Interface Transport -->
  <g transform="translate(125, 95)" filter="url(#shadow)">
    <rect width="240" height="75" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <rect width="240" height="38" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
    <text x="120" y="17" text-anchor="middle" font-size="11" fill="#1e40af">&lt;&lt;interface&gt;&gt;  &lt;&lt;Product&gt;&gt;</text>
    <text x="120" y="32" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e3a8a">Transport</text>
    <line x1="0" y1="38" x2="240" y2="38" stroke="#2563eb" stroke-width="1.5"/>
    <text x="10" y="58" font-size="11" fill="#0f172a">+ deliver(cargo: String, dest: String): void</text>
  </g>

  <!-- Class Truck -->
  <g transform="translate(50, 260)" filter="url(#shadow)">
    <rect width="180" height="70" rx="6" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="180" height="35" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="90" y="16" text-anchor="middle" font-size="10" fill="#2563eb">&lt;&lt;ConcreteProduct&gt;&gt;</text>
    <text x="90" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">Truck</text>
    <line x1="0" y1="35" x2="180" y2="35" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="8" y="54" font-size="10.5" fill="#0f172a">+ deliver(cargo, dest): void</text>
  </g>

  <!-- Class Ship -->
  <g transform="translate(260, 260)" filter="url(#shadow)">
    <rect width="180" height="70" rx="6" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="180" height="35" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="90" y="16" text-anchor="middle" font-size="10" fill="#2563eb">&lt;&lt;ConcreteProduct&gt;&gt;</text>
    <text x="90" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">Ship</text>
    <line x1="0" y1="35" x2="180" y2="35" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="8" y="54" font-size="10.5" fill="#0f172a">+ deliver(cargo, dest): void</text>
  </g>

  <!-- Realizations: Truck and Ship ..|> Transport -->
  <path d="M 140,260 L 140,215 L 220,215 L 220,170" fill="none" stroke="#333333" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#triangle)"/>
  <path d="M 350,260 L 350,215 L 270,215 L 270,170" fill="none" stroke="#333333" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#triangle)"/>

  <!-- Package kz.aitu.assignment2.logistics -->
  <rect x="500" y="60" width="430" height="330" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4" filter="url(#shadow)"/>
  <rect x="500" y="60" width="220" height="24" rx="4" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="510" y="77" font-size="11" font-weight="bold" fill="#334155">kz.aitu.assignment2.logistics</text>

  <!-- Abstract Class Logistics -->
  <g transform="translate(575, 95)" filter="url(#shadow)">
    <rect width="280" height="95" rx="6" fill="#fefce8" stroke="#ca8a04" stroke-width="1.5"/>
    <rect width="280" height="38" rx="6" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.5"/>
    <text x="140" y="17" text-anchor="middle" font-size="11" fill="#854d0e">&lt;&lt;abstract&gt;&gt;  &lt;&lt;Creator&gt;&gt;</text>
    <text x="140" y="32" text-anchor="middle" font-size="14" font-weight="bold" font-style="italic" fill="#713f12">Logistics</text>
    <line x1="0" y1="38" x2="280" y2="38" stroke="#ca8a04" stroke-width="1.5"/>
    <text x="10" y="57" font-size="11" font-style="italic" fill="#0f172a">+ {abstract} createTransport(): Transport</text>
    <text x="10" y="77" font-size="11" fill="#0f172a">+ planDelivery(cargo: String, dest: String): void</text>
  </g>

  <!-- Class RoadLogistics -->
  <g transform="translate(520, 260)" filter="url(#shadow)">
    <rect width="180" height="70" rx="6" fill="#ffffff" stroke="#eab308" stroke-width="1.5"/>
    <rect width="180" height="35" rx="6" fill="#fefce8" stroke="#eab308" stroke-width="1.5"/>
    <text x="90" y="16" text-anchor="middle" font-size="10" fill="#854d0e">&lt;&lt;ConcreteCreator&gt;&gt;</text>
    <text x="90" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#713f12">RoadLogistics</text>
    <line x1="0" y1="35" x2="180" y2="35" stroke="#eab308" stroke-width="1.5"/>
    <text x="8" y="54" font-size="10.5" fill="#0f172a">+ createTransport(): Transport</text>
  </g>

  <!-- Class SeaLogistics -->
  <g transform="translate(730, 260)" filter="url(#shadow)">
    <rect width="180" height="70" rx="6" fill="#ffffff" stroke="#eab308" stroke-width="1.5"/>
    <rect width="180" height="35" rx="6" fill="#fefce8" stroke="#eab308" stroke-width="1.5"/>
    <text x="90" y="16" text-anchor="middle" font-size="10" fill="#854d0e">&lt;&lt;ConcreteCreator&gt;&gt;</text>
    <text x="90" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#713f12">SeaLogistics</text>
    <line x1="0" y1="35" x2="180" y2="35" stroke="#eab308" stroke-width="1.5"/>
    <text x="8" y="54" font-size="10.5" fill="#0f172a">+ createTransport(): Transport</text>
  </g>

  <!-- Inheritance: RoadLogistics and SeaLogistics --|> Logistics -->
  <path d="M 610,260 L 610,225 L 685,225 L 685,190" fill="none" stroke="#333333" stroke-width="1.5" marker-end="url(#triangle)"/>
  <path d="M 820,260 L 820,225 L 745,225 L 745,190" fill="none" stroke="#333333" stroke-width="1.5" marker-end="url(#triangle)"/>

  <!-- Creates dependencies (Factory method instantiates concrete product) -->
  <path d="M 520,295 L 230,295" fill="none" stroke="#059669" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#green-arrow)"/>
  <text x="375" y="288" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">&lt;&lt;creates Truck&gt;&gt;</text>

  <path d="M 730,315 L 440,315" fill="none" stroke="#059669" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#green-arrow)"/>
  <text x="585" y="333" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">&lt;&lt;creates Ship&gt;&gt;</text>

  <!-- Creator uses Product contract -->
  <path d="M 575,135 L 365,135" fill="none" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#open-arrow)"/>
  <text x="470" y="128" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">&lt;&lt;uses / calls deliver()&gt;&gt;</text>

  <!-- DeliveryApplication (Client) -->
  <g transform="translate(500, 420)" filter="url(#shadow)">
    <rect width="430" height="105" rx="6" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
    <rect width="430" height="35" rx="6" fill="#e2e8f0" stroke="#475569" stroke-width="1.5"/>
    <text x="215" y="16" text-anchor="middle" font-size="10" fill="#475569">&lt;&lt;Client&gt;&gt;</text>
    <text x="215" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">DeliveryApplication (kz.aitu.assignment2.app)</text>
    <line x1="0" y1="35" x2="430" y2="35" stroke="#475569" stroke-width="1.5"/>
    <text x="10" y="54" font-size="10.5" fill="#334155">- logistics: Logistics;  - button: Button;  - checkbox: Checkbox</text>
    <text x="10" y="72" font-size="10.5" fill="#0f172a">+ DeliveryApplication(guiFactory: GUIFactory, logistics: Logistics)</text>
    <text x="10" y="90" font-size="10.5" fill="#0f172a">+ run(cargo: String, destination: String): void</text>
  </g>

  <!-- Client depends on Logistics -->
  <path d="M 715,420 L 715,390" fill="none" stroke="#333333" stroke-width="1.5" marker-end="url(#open-arrow)"/>
  <text x="725" y="410" font-size="10" fill="#334155">&lt;&lt;delegates workflow&gt;&gt;</text>
</svg>"""

af_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 620" width="100%" height="100%" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000000" flood-opacity="0.10"/>
    </filter>
    <marker id="triangle" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="10" markerHeight="10" orient="auto-start-reverse">
      <polygon points="0,0 10,5 0,10" fill="#ffffff" stroke="#333333" stroke-width="1.5"/>
    </marker>
    <marker id="open-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <polyline points="0,1 9,5 0,9" fill="none" stroke="#333333" stroke-width="1.5"/>
    </marker>
    <marker id="green-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
      <polyline points="0,1 9,5 0,9" fill="none" stroke="#059669" stroke-width="1.5"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="480" y="30" text-anchor="middle" font-size="18" font-weight="bold" fill="#0f172a">Abstract Factory Pattern — UI Component Families &amp; Roles</text>

  <!-- Package kz.aitu.assignment2.ui -->
  <rect x="20" y="55" width="460" height="420" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4" filter="url(#shadow)"/>
  <rect x="20" y="55" width="180" height="24" rx="4" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="30" y="72" font-size="11" font-weight="bold" fill="#334155">kz.aitu.assignment2.ui</text>

  <!-- Interface Button -->
  <g transform="translate(40, 90)" filter="url(#shadow)">
    <rect width="190" height="70" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <rect width="190" height="35" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
    <text x="95" y="16" text-anchor="middle" font-size="10" fill="#1e40af">&lt;&lt;interface&gt;&gt;  &lt;&lt;Product A&gt;&gt;</text>
    <text x="95" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">Button</text>
    <line x1="0" y1="35" x2="190" y2="35" stroke="#2563eb" stroke-width="1.5"/>
    <text x="10" y="54" font-size="11" fill="#0f172a">+ paint(): void</text>
  </g>

  <!-- Interface Checkbox -->
  <g transform="translate(270, 90)" filter="url(#shadow)">
    <rect width="190" height="70" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <rect width="190" height="35" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
    <text x="95" y="16" text-anchor="middle" font-size="10" fill="#1e40af">&lt;&lt;interface&gt;&gt;  &lt;&lt;Product B&gt;&gt;</text>
    <text x="95" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">Checkbox</text>
    <line x1="0" y1="35" x2="190" y2="35" stroke="#2563eb" stroke-width="1.5"/>
    <text x="10" y="54" font-size="11" fill="#0f172a">+ paint(): void</text>
  </g>

  <!-- Windows Family UI -->
  <g transform="translate(40, 220)" filter="url(#shadow)">
    <rect width="190" height="65" rx="6" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="190" height="32" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="95" y="15" text-anchor="middle" font-size="10" fill="#2563eb">&lt;&lt;Windows Family&gt;&gt;</text>
    <text x="95" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">WindowsButton</text>
    <line x1="0" y1="32" x2="190" y2="32" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="8" y="50" font-size="10.5" fill="#0f172a">+ paint(): void</text>
  </g>
  <g transform="translate(270, 220)" filter="url(#shadow)">
    <rect width="190" height="65" rx="6" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="190" height="32" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="95" y="15" text-anchor="middle" font-size="10" fill="#2563eb">&lt;&lt;Windows Family&gt;&gt;</text>
    <text x="95" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e3a8a">WindowsCheckbox</text>
    <line x1="0" y1="32" x2="190" y2="32" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="8" y="50" font-size="10.5" fill="#0f172a">+ paint(): void</text>
  </g>

  <!-- macOS Family UI -->
  <g transform="translate(40, 360)" filter="url(#shadow)">
    <rect width="190" height="65" rx="6" fill="#ffffff" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="190" height="32" rx="6" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="95" y="15" text-anchor="middle" font-size="10" fill="#7c3aed">&lt;&lt;macOS Family&gt;&gt;</text>
    <text x="95" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#4c1d95">MacOSButton</text>
    <line x1="0" y1="32" x2="190" y2="32" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="8" y="50" font-size="10.5" fill="#0f172a">+ paint(): void</text>
  </g>
  <g transform="translate(270, 360)" filter="url(#shadow)">
    <rect width="190" height="65" rx="6" fill="#ffffff" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="190" height="32" rx="6" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="95" y="15" text-anchor="middle" font-size="10" fill="#7c3aed">&lt;&lt;macOS Family&gt;&gt;</text>
    <text x="95" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#4c1d95">MacOSCheckbox</text>
    <line x1="0" y1="32" x2="190" y2="32" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="8" y="50" font-size="10.5" fill="#0f172a">+ paint(): void</text>
  </g>

  <!-- Realizations Button / Checkbox -->
  <path d="M 135,220 L 135,160" fill="none" stroke="#333333" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#triangle)"/>
  <path d="M 365,220 L 365,160" fill="none" stroke="#333333" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#triangle)"/>
  <path d="M 135,360 L 135,285" fill="none" stroke="#333333" stroke-width="1.5" stroke-dasharray="5 4"/>
  <path d="M 365,360 L 365,285" fill="none" stroke="#333333" stroke-width="1.5" stroke-dasharray="5 4"/>

  <!-- Package kz.aitu.assignment2.factory -->
  <rect x="500" y="55" width="440" height="420" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4" filter="url(#shadow)"/>
  <rect x="500" y="55" width="200" height="24" rx="4" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="510" y="72" font-size="11" font-weight="bold" fill="#334155">kz.aitu.assignment2.factory</text>

  <!-- Interface GUIFactory -->
  <g transform="translate(585, 90)" filter="url(#shadow)">
    <rect width="270" height="85" rx="6" fill="#fdf4ff" stroke="#c026d3" stroke-width="1.5"/>
    <rect width="270" height="38" rx="6" fill="#fae8ff" stroke="#c026d3" stroke-width="1.5"/>
    <text x="135" y="17" text-anchor="middle" font-size="11" fill="#a21caf">&lt;&lt;interface&gt;&gt;  &lt;&lt;AbstractFactory&gt;&gt;</text>
    <text x="135" y="32" text-anchor="middle" font-size="14" font-weight="bold" fill="#86198f">GUIFactory</text>
    <line x1="0" y1="38" x2="270" y2="38" stroke="#c026d3" stroke-width="1.5"/>
    <text x="10" y="56" font-size="11" fill="#0f172a">+ createButton(): Button</text>
    <text x="10" y="74" font-size="11" fill="#0f172a">+ createCheckbox(): Checkbox</text>
  </g>

  <!-- WindowsFactory -->
  <g transform="translate(520, 240)" filter="url(#shadow)">
    <rect width="185" height="85" rx="6" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
    <rect width="185" height="35" rx="6" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="92" y="16" text-anchor="middle" font-size="10" fill="#2563eb">&lt;&lt;ConcreteFactory 1&gt;&gt;</text>
    <text x="92" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e3a8a">WindowsFactory</text>
    <line x1="0" y1="35" x2="185" y2="35" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="8" y="54" font-size="10" fill="#0f172a">+ createButton(): Button</text>
    <text x="8" y="72" font-size="10" fill="#0f172a">+ createCheckbox(): Checkbox</text>
  </g>

  <!-- MacOSFactory -->
  <g transform="translate(735, 240)" filter="url(#shadow)">
    <rect width="185" height="85" rx="6" fill="#ffffff" stroke="#8b5cf6" stroke-width="1.5"/>
    <rect width="185" height="35" rx="6" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="92" y="16" text-anchor="middle" font-size="10" fill="#7c3aed">&lt;&lt;ConcreteFactory 2&gt;&gt;</text>
    <text x="92" y="30" text-anchor="middle" font-size="13" font-weight="bold" fill="#4c1d95">MacOSFactory</text>
    <line x1="0" y1="35" x2="185" y2="35" stroke="#8b5cf6" stroke-width="1.5"/>
    <text x="8" y="54" font-size="10" fill="#0f172a">+ createButton(): Button</text>
    <text x="8" y="72" font-size="10" fill="#0f172a">+ createCheckbox(): Checkbox</text>
  </g>

  <!-- Realizations GUIFactory -->
  <path d="M 610,240 L 610,205 L 685,205 L 685,175" fill="none" stroke="#333333" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#triangle)"/>
  <path d="M 825,240 L 825,205 L 755,205 L 755,175" fill="none" stroke="#333333" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#triangle)"/>

  <!-- Factory creation links -->
  <path d="M 520,270 L 460,250" fill="none" stroke="#059669" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#green-arrow)"/>
  <text x="490" y="240" font-size="9" font-weight="bold" fill="#059669">&lt;&lt;creates Windows family&gt;&gt;</text>

  <path d="M 735,310 L 460,390" fill="none" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#green-arrow)"/>
  <text x="590" y="380" font-size="9" font-weight="bold" fill="#7c3aed">&lt;&lt;creates macOS family&gt;&gt;</text>

  <!-- DeliveryApplication (Client) -->
  <g transform="translate(180, 500)" filter="url(#shadow)">
    <rect width="600" height="90" rx="6" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
    <rect width="600" height="32" rx="6" fill="#e2e8f0" stroke="#475569" stroke-width="1.5"/>
    <text x="300" y="15" text-anchor="middle" font-size="10" fill="#475569">&lt;&lt;Client&gt;&gt;</text>
    <text x="300" y="27" text-anchor="middle" font-size="13" font-weight="bold" fill="#0f172a">DeliveryApplication (kz.aitu.assignment2.app)</text>
    <line x1="0" y1="32" x2="600" y2="32" stroke="#475569" stroke-width="1.5"/>
    <text x="15" y="49" font-size="10.5" fill="#334155">- button: Button;  - checkbox: Checkbox;  - logistics: Logistics</text>
    <text x="15" y="67" font-size="10.5" fill="#0f172a">+ DeliveryApplication(guiFactory: GUIFactory, logistics: Logistics)</text>
    <text x="15" y="83" font-size="10.5" fill="#0f172a">+ run(cargo: String, destination: String): void</text>
  </g>

  <!-- Client depends on Abstract Factory & Products -->
  <path d="M 680,500 L 720,175" fill="none" stroke="#a21caf" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#open-arrow)"/>
  <text x="735" y="470" font-size="10" font-weight="bold" fill="#a21caf">&lt;&lt;injects GUIFactory&gt;&gt;</text>

  <path d="M 280,500 L 170,160" fill="none" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#open-arrow)"/>
  <text x="210" y="320" font-size="10" font-weight="bold" fill="#2563eb">&lt;&lt;uses Button&gt;&gt;</text>

  <path d="M 370,500 L 365,160" fill="none" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#open-arrow)"/>
  <text x="375" y="320" font-size="10" font-weight="bold" fill="#2563eb">&lt;&lt;uses Checkbox&gt;&gt;</text>
</svg>"""

out_dir = r"c:\Users\murat\IdeaProjects\Sdp_Assignment\docs\uml"
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "factory_method.svg"), "w", encoding="utf-8") as f:
    f.write(fm_svg)

with open(os.path.join(out_dir, "abstract_factory.svg"), "w", encoding="utf-8") as f:
    f.write(af_svg)

print("SVGs successfully generated!")
