import java.rmi.*;

public interface ServerIntf extends Remote{
    public double Add(double num1, double num2) throws RemoteException;
    public double Sub(double num1, double num2) throws RemoteException;
    public double Mul(double num1, double num2) throws RemoteException;
    public double Div(double num1, double num2) throws RemoteException;
}
