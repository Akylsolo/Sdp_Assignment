package kz.aitu.assignment2.logistics;

import kz.aitu.assignment2.transport.Transport;

public abstract class Logistics {

    public abstract Transport createTransport();

    public void planDelivery(String cargo, String destination) {
        Transport transport = createTransport();
        transport.deliver(cargo, destination);
    }
}
