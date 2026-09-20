package kz.aitu.assignment2.app;

import kz.aitu.assignment2.factory.GUIFactory;
import kz.aitu.assignment2.logistics.Logistics;
import kz.aitu.assignment2.ui.Button;
import kz.aitu.assignment2.ui.Checkbox;

public class DeliveryApplication {
    private final Button button;
    private final Checkbox checkbox;
    private final Logistics logistics;

    public DeliveryApplication(GUIFactory guiFactory, Logistics logistics) {
        this.button = guiFactory.createButton();
        this.checkbox = guiFactory.createCheckbox();
        this.logistics = logistics;
    }

    public void run(String cargo, String destination) {
        button.paint();
        checkbox.paint();
        logistics.planDelivery(cargo, destination);
    }

    public void run() {
        run("laboratory equipment", "Aktau warehouse");
    }
}
