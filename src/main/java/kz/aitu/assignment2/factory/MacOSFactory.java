package kz.aitu.assignment2.factory;

import kz.aitu.assignment2.ui.Button;
import kz.aitu.assignment2.ui.Checkbox;
import kz.aitu.assignment2.ui.MacOSButton;
import kz.aitu.assignment2.ui.MacOSCheckbox;

public class MacOSFactory implements GUIFactory {

    @Override
    public Button createButton() {
        return new MacOSButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacOSCheckbox();
    }
}
