package kz.aitu.assignment2.logistics;

import kz.aitu.assignment2.transport.Ship;
import kz.aitu.assignment2.transport.Transport;

public class SeaLogistics extends Logistics {

    @Override
    public Transport createTransport() {
        return new Ship();
    }
}
