import java.rmi.*;
import java.rmi.server.*;

public class ServerImpl extends UnicastRemoteObject implements ServerIntf{
    public ServerImpl() throws RemoteException{

    }

    public double Add(double num1, double num2) throws RemoteException{
        return num1+num2;
    }
    public double Sub(double num1, double num2) throws RemoteException{
        return num1-num2;
    }
    public double Mul(double num1, double num2) throws RemoteException{
        return num1*num2;
    }
    public double Div(double num1, double num2) throws RemoteException{
        if(num2!=0){
            return num1/num2;
        }
        else{
            System.out.println("Cannot be divided");
        }
        return 0.00;
    }
}