package kz.aitu.assignment2.factory;

import kz.aitu.assignment2.ui.Button;
import kz.aitu.assignment2.ui.Checkbox;
import kz.aitu.assignment2.ui.WindowsButton;
import kz.aitu.assignment2.ui.WindowsCheckbox;

public class WindowsFactory implements GUIFactory {

    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}
