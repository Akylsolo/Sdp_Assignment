package kz.aitu.assignment2;

import kz.aitu.assignment2.app.DeliveryApplication;
import kz.aitu.assignment2.factory.GUIFactory;
import kz.aitu.assignment2.factory.MacOSFactory;
import kz.aitu.assignment2.factory.WindowsFactory;
import kz.aitu.assignment2.logistics.Logistics;
import kz.aitu.assignment2.logistics.RoadLogistics;
import kz.aitu.assignment2.logistics.SeaLogistics;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        String deliveryMode;
        String uiPlatform;

        if (args.length >= 2) {
            deliveryMode = args[0].trim();
            uiPlatform = args[1].trim();
        } else if (args.length == 1) {
            System.err.println("Error: Missing UI platform argument. Expected WINDOWS or MACOS.");
            return;
        } else {
            Scanner scanner = new Scanner(System.in);
            if (System.console() != null) {
                System.out.print("Enter delivery mode (ROAD, SEA): ");
            }
            if (!scanner.hasNextLine()) {
                System.err.println("Error: Missing required input. Expected delivery mode (ROAD, SEA) and UI platform (WINDOWS, MACOS).");
                return;
            }
            deliveryMode = scanner.nextLine().trim();
            if (deliveryMode.isEmpty()) {
                System.err.println("Error: Missing required input. Expected delivery mode (ROAD, SEA) and UI platform (WINDOWS, MACOS).");
                return;
            }

            if (System.console() != null) {
                System.out.print("Enter UI platform (WINDOWS, MACOS): ");
            }
            if (!scanner.hasNextLine()) {
                System.err.println("Error: Missing UI platform input. Expected WINDOWS or MACOS.");
                return;
            }
            uiPlatform = scanner.nextLine().trim();
            if (uiPlatform.isEmpty()) {
                System.err.println("Error: Missing UI platform input. Expected WINDOWS or MACOS.");
                return;
            }
        }

        if (deliveryMode.isEmpty() || uiPlatform.isEmpty()) {
            System.err.println("Error: Inputs cannot be empty. Expected delivery mode (ROAD, SEA) and UI platform (WINDOWS, MACOS).");
            return;
        }

        Logistics logistics = selectLogistics(deliveryMode);
        if (logistics == null) {
            System.err.println("Error: Unsupported delivery mode '" + deliveryMode + "'. Supported modes: ROAD, SEA.");
            return;
        }

        GUIFactory guiFactory = selectGUIFactory(uiPlatform);
        if (guiFactory == null) {
            System.err.println("Error: Unsupported UI platform '" + uiPlatform + "'. Supported platforms: WINDOWS, MACOS.");
            return;
        }

        System.out.println("Delivery mode: " + deliveryMode.toUpperCase());
        System.out.println("UI platform: " + uiPlatform.toUpperCase());

        DeliveryApplication app = new DeliveryApplication(guiFactory, logistics);
        app.run();
    }

    public static Logistics selectLogistics(String mode) {
        if ("ROAD".equalsIgnoreCase(mode)) {
            return new RoadLogistics();
        }
        if ("SEA".equalsIgnoreCase(mode)) {
            return new SeaLogistics();
        }
        return null;
    }

    public static GUIFactory selectGUIFactory(String platform) {
        if ("WINDOWS".equalsIgnoreCase(platform)) {
            return new WindowsFactory();
        }
        if ("MACOS".equalsIgnoreCase(platform)) {
            return new MacOSFactory();
        }
        return null;
    }
}
