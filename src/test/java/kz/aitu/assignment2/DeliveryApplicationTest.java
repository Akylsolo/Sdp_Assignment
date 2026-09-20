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
import org.junit.jupiter.api.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class DeliveryApplicationTest {
    private final ByteArrayOutputStream out = new ByteArrayOutputStream();
    private final ByteArrayOutputStream err = new ByteArrayOutputStream();
    private final PrintStream originalOut = System.out;
    private final PrintStream originalErr = System.err;

    @BeforeEach
    void setUp() {
        System.setOut(new PrintStream(out));
        System.setErr(new PrintStream(err));
    }

    @AfterEach
    void tearDown() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }

    @Test
    void testRoadLogistics() {
        Logistics logistics = new RoadLogistics();
        Transport transport = logistics.createTransport();
        assertNotNull(transport);
        assertTrue(transport instanceof Truck);
    }

    @Test
    void testSeaLogistics() {
        Logistics logistics = new SeaLogistics();
        Transport transport = logistics.createTransport();
        assertNotNull(transport);
        assertTrue(transport instanceof Ship);
    }

    @Test
    void testWindowsFactory() {
        GUIFactory factory = new WindowsFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();
        assertTrue(button instanceof WindowsButton);
        assertTrue(checkbox instanceof WindowsCheckbox);
    }

    @Test
    void testMacOSFactory() {
        GUIFactory factory = new MacOSFactory();
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();
        assertTrue(button instanceof MacOSButton);
        assertTrue(checkbox instanceof MacOSCheckbox);
    }

    @Test
    void testDeliveryApplication() {
        GUIFactory factory = new WindowsFactory();
        Logistics logistics = new RoadLogistics();
        DeliveryApplication app = new DeliveryApplication(factory, logistics);
        app.run();
        assertTrue(out.toString().contains("Rendering Windows button"));
        assertTrue(out.toString().contains("Truck delivers"));
    }

    @Test
    void testMainRoadWindows() {
        Main.main(new String[]{"ROAD", "WINDOWS"});
        String output = out.toString();
        assertTrue(output.contains("Rendering Windows button"));
        assertTrue(output.contains("Rendering Windows checkbox"));
        assertTrue(output.contains("Truck delivers"));
    }

    @Test
    void testMainSeaWindows() {
        Main.main(new String[]{"SEA", "WINDOWS"});
        String output = out.toString();
        assertTrue(output.contains("Rendering Windows button"));
        assertTrue(output.contains("Ship delivers"));
    }

    @Test
    void testMainRoadMacOS() {
        Main.main(new String[]{"ROAD", "MACOS"});
        String output = out.toString();
        assertTrue(output.contains("Rendering macOS button"));
        assertTrue(output.contains("Truck delivers"));
    }

    @Test
    void testMainSeaMacOS() {
        Main.main(new String[]{"SEA", "MACOS"});
        String output = out.toString();
        assertTrue(output.contains("Rendering macOS button"));
        assertTrue(output.contains("Ship delivers"));
    }

    @Test
    void testMainInvalidMode() {
        Main.main(new String[]{"AIR", "WINDOWS"});
        assertTrue(err.toString().contains("Error: Unsupported delivery mode 'AIR'"));
    }

    @Test
    void testMainInvalidPlatform() {
        Main.main(new String[]{"ROAD", "LINUX"});
        assertTrue(err.toString().contains("Error: Unsupported UI platform 'LINUX'"));
    }

    @Test
    void testMainMissingPlatform() {
        Main.main(new String[]{"ROAD"});
        assertTrue(err.toString().contains("Error: Missing UI platform argument"));
    }

    @Test
    void testSelectLogistics() {
        assertTrue(Main.selectLogistics("ROAD") instanceof RoadLogistics);
        assertTrue(Main.selectLogistics("SEA") instanceof SeaLogistics);
        assertNull(Main.selectLogistics("AIR"));
    }

    @Test
    void testSelectGUIFactory() {
        assertTrue(Main.selectGUIFactory("WINDOWS") instanceof WindowsFactory);
        assertTrue(Main.selectGUIFactory("MACOS") instanceof MacOSFactory);
        assertNull(Main.selectGUIFactory("LINUX"));
    }
}
