package kz.aitu.assignment2;

import kz.aitu.assignment2.app.DeliveryApplication;
import kz.aitu.assignment2.factory.GUIFactory;
import kz.aitu.assignment2.factory.MacOSFactory;
import kz.aitu.assignment2.factory.WindowsFactory;
import kz.aitu.assignment2.logistics.Logistics;
import kz.aitu.assignment2.logistics.RoadLogistics;
import kz.aitu.assignment2.logistics.SeaLogistics;
import kz.aitu.assignment2.transport.Ship;
import kz.aitu.assignment2.transport.Transport;
import kz.aitu.assignment2.transport.Truck;
import kz.aitu.assignment2.ui.Button;
import kz.aitu.assignment2.ui.Checkbox;
import kz.aitu.assignment2.ui.MacOSButton;
import kz.aitu.assignment2.ui.MacOSCheckbox;
import kz.aitu.assignment2.ui.WindowsButton;
import kz.aitu.assignment2.ui.WindowsCheckbox;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertInstanceOf;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class DeliveryApplicationTest {
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();
    private final ByteArrayOutputStream errContent = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    private final PrintStream originalErr = System.err;
    private final InputStream originalIn = System.in;

    @BeforeEach
    void setUp() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @AfterEach
    void tearDown() {
        System.setOut(originalOut);
        System.setErr(originalErr);
        System.setIn(originalIn);
    }

    @Test
    @DisplayName("Factory Method: RoadLogistics instantiates Truck")
    void testRoadLogisticsCreatesTruck() {
        Logistics logistics = new RoadLogistics();
        Transport transport = logistics.createTransport();
        assertNotNull(transport);
        assertInstanceOf(Truck.class, transport);
    }

    @Test
    @DisplayName("Factory Method: SeaLogistics instantiates Ship")
    void testSeaLogisticsCreatesShip() {
        Logistics logistics = new SeaLogistics();
        Transport transport = logistics.createTransport();
        assertNotNull(transport);
        assertInstanceOf(Ship.class, transport);
    }

    @Test
    @DisplayName("Abstract Factory: WindowsFactory creates matching Windows Button and Checkbox")
    void testWindowsFactoryCreatesWindowsComponents() {
        GUIFactory factory = new WindowsFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();
        assertNotNull(button);
        assertNotNull(checkbox);
        assertInstanceOf(WindowsButton.class, button);
        assertInstanceOf(WindowsCheckbox.class, checkbox);
    }

    @Test
    @DisplayName("Abstract Factory: MacOSFactory creates matching macOS Button and Checkbox")
    void testMacOSFactoryCreatesMacOSComponents() {
        GUIFactory factory = new MacOSFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();
        assertNotNull(button);
        assertNotNull(checkbox);
        assertInstanceOf(MacOSButton.class, button);
        assertInstanceOf(MacOSCheckbox.class, checkbox);
    }

    @Test
    @DisplayName("Check 1: ROAD + WINDOWS -> Truck delivery, Windows button and checkbox")
    void testCheck1RoadAndWindows() {
        Main.main(new String[]{"ROAD", "WINDOWS"});
        String output = outContent.toString();

        assertTrue(output.contains("Delivery mode: ROAD"));
        assertTrue(output.contains("UI platform: WINDOWS"));
        assertTrue(output.contains("Rendering Windows button"));
        assertTrue(output.contains("Rendering Windows checkbox"));
        assertTrue(output.contains("Truck delivers laboratory equipment to Aktau warehouse"));
    }

    @Test
    @DisplayName("Check 2: SEA + WINDOWS -> Ship delivery, Windows button and checkbox")
    void testCheck2SeaAndWindows() {
        Main.main(new String[]{"SEA", "WINDOWS"});
        String output = outContent.toString();

        assertTrue(output.contains("Delivery mode: SEA"));
        assertTrue(output.contains("UI platform: WINDOWS"));
        assertTrue(output.contains("Rendering Windows button"));
        assertTrue(output.contains("Rendering Windows checkbox"));
        assertTrue(output.contains("Ship delivers laboratory equipment to Aktau warehouse by sea"));
    }

    @Test
    @DisplayName("Check 3: ROAD + MACOS -> Truck delivery, macOS button and checkbox")
    void testCheck3RoadAndMacOS() {
        Main.main(new String[]{"ROAD", "MACOS"});
        String output = outContent.toString();

        assertTrue(output.contains("Delivery mode: ROAD"));
        assertTrue(output.contains("UI platform: MACOS"));
        assertTrue(output.contains("Rendering macOS button"));
        assertTrue(output.contains("Rendering macOS checkbox"));
        assertTrue(output.contains("Truck delivers laboratory equipment to Aktau warehouse"));
    }

    @Test
    @DisplayName("Check 4: SEA + MACOS -> Ship delivery, macOS button and checkbox")
    void testCheck4SeaAndMacOS() {
        Main.main(new String[]{"SEA", "MACOS"});
        String output = outContent.toString();

        assertTrue(output.contains("Delivery mode: SEA"));
        assertTrue(output.contains("UI platform: MACOS"));
        assertTrue(output.contains("Rendering macOS button"));
        assertTrue(output.contains("Rendering macOS checkbox"));
        assertTrue(output.contains("Ship delivers laboratory equipment to Aktau warehouse by sea"));
    }

    @Test
    @DisplayName("Check 5: Unsupported delivery mode with valid platform -> Clear validation message, no delivery")
    void testCheck5UnsupportedDeliveryModeWithValidPlatform() {
        Main.main(new String[]{"AIR", "WINDOWS"});
        String errorOutput = errContent.toString();
        String standardOutput = outContent.toString();

        assertTrue(errorOutput.contains("Error: Unsupported delivery mode 'AIR'. Supported modes: ROAD, SEA."));
        assertEquals("", standardOutput);
    }

    @Test
    @DisplayName("Check 6: Unsupported platform with valid delivery mode -> Clear validation message, no UI construction")
    void testCheck6UnsupportedPlatformWithValidDeliveryMode() {
        Main.main(new String[]{"ROAD", "LINUX"});
        String errorOutput = errContent.toString();
        String standardOutput = outContent.toString();

        assertTrue(errorOutput.contains("Error: Unsupported UI platform 'LINUX'. Supported platforms: WINDOWS, MACOS."));
        assertEquals("", standardOutput);
    }

    @Test
    @DisplayName("Check 7: Missing second argument -> Clear validation error")
    void testMissingPlatformArgument() {
        Main.main(new String[]{"ROAD"});
        String errorOutput = errContent.toString();
        String standardOutput = outContent.toString();

        assertTrue(errorOutput.contains("Error: Missing UI platform argument. Expected WINDOWS or MACOS."));
        assertEquals("", standardOutput);
    }

    @Test
    @DisplayName("Check 8: Empty interactive console input -> Clear validation error")
    void testMissingArgumentsConsoleInputEmpty() {
        System.setIn(new ByteArrayInputStream("".getBytes()));
        Main.main(new String[0]);
        String errorOutput = errContent.toString();

        assertTrue(errorOutput.contains("Error: Missing required input"));
        assertEquals("", outContent.toString());
    }

    @Test
    @DisplayName("Interactive mode: Valid road and windows input via console")
    void testInteractiveConsoleInputSuccess() {
        String simulatedInput = "ROAD" + System.lineSeparator() + "WINDOWS" + System.lineSeparator();
        System.setIn(new ByteArrayInputStream(simulatedInput.getBytes()));
        Main.main(new String[0]);
        String output = outContent.toString();

        assertTrue(output.contains("Delivery mode: ROAD"));
        assertTrue(output.contains("UI platform: WINDOWS"));
        assertTrue(output.contains("Rendering Windows button"));
        assertTrue(output.contains("Rendering Windows checkbox"));
        assertTrue(output.contains("Truck delivers laboratory equipment to Aktau warehouse"));
    }

    @Test
    @DisplayName("Custom cargo and destination execution through DeliveryApplication")
    void testDeliveryApplicationExecution() {
        GUIFactory factory = new WindowsFactory();
        Logistics logistics = new RoadLogistics();
        DeliveryApplication app = new DeliveryApplication(factory, logistics);

        app.run("medical equipment", "Astana hospital");
        String output = outContent.toString();

        assertTrue(output.contains("Rendering Windows button"));
        assertTrue(output.contains("Rendering Windows checkbox"));
        assertTrue(output.contains("Truck delivers medical equipment to Astana hospital"));
    }

    @Test
    @DisplayName("Startup helper tests")
    void testStartupHelpers() {
        assertInstanceOf(RoadLogistics.class, Main.selectLogistics("road"));
        assertInstanceOf(SeaLogistics.class, Main.selectLogistics("sea"));
        assertNull(Main.selectLogistics("air"));

        assertInstanceOf(WindowsFactory.class, Main.selectGUIFactory("windows"));
        assertInstanceOf(MacOSFactory.class, Main.selectGUIFactory("macos"));
        assertNull(Main.selectGUIFactory("android"));
    }
}
