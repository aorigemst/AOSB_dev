import javax.swing.*;

public class MyClass extends JFrame {
    
    private static JLabel outpuJLabel = new JLabel();
    
    public static void main(String[] args) {

        MyClass window = new MyClass();
            
            window.setSize(500,500);
            
            window.setVisible(true);

            window.setTitle("Minha Classe");
                
            window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

                
        
        System.out.println ("Explicando esse método : main");

        

        System.out.println ("Se a Classe é uma classe executável, realizando uma inicialização dentro do projeto, pro exemplo, ela precisa de um método especial, um método principal, método `main`. sendo criado como : `public static void main (String[] args)`");

        

        System.out.println ("void -> apenas executa sem retornar nada; espera um parâmetro especial do tipo String; parâmetro de array args; corpo representado por {}");

        

        System.out.println ("Em todas as classes, as primeiras letras de cada palava e subpalavra deverão ser maúsculas: Sample - MyClass.java");

      

        System.out.println ("Toda Classe precisa existir dentro do diretório src do projeto");
    }
    
}
