package kz.aitu.assignment2.factory;

import kz.aitu.assignment2.ui.Button;
import kz.aitu.assignment2.ui.Checkbox;

public interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}
