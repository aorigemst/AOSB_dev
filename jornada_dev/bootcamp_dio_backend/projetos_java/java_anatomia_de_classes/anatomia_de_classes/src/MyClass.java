import javax.swing.*;

public class MyClass extends JFrame {
    
    private static JLabel outpuJLabel = new JLabel();
    
    public static void main(String[] args) {

        MyClass window = new MyClass();
            
            window.setSize(500,500);
            
            window.setVisible(true);

            window.setTitle("Minha Classe");
                
            window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

             
              

    }
    
}
