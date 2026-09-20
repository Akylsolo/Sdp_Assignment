package kz.aitu.assignment2.logistics;

import kz.aitu.assignment2.transport.Transport;
import kz.aitu.assignment2.transport.Truck;

public class RoadLogistics extends Logistics {

    @Override
    public Transport createTransport() {
        return new Truck();
    }
}
