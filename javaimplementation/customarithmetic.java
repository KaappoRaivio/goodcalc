public class customarithmetic {
    public static void main (String [] args) {
        System.out.println(CustomArithmetic.add("3", "3"));
    }
}

class CustomArithmetic {
    public static String add (String operand1, String operand2) {
        return String.valueOf(Integer.parseInt(operand1) + Integer.parseInt(operand2));
    }
    public static String sub (String operand1, String operand2) {
        return String.valueOf(Integer.parseInt(operand1) - Integer.parseInt(operand2));
    }
    public static String mul (String operand1, String operand2) {
        return String.valueOf(Integer.parseInt(operand1) * Integer.parseInt(operand2));
    }
    public static String div (String operand1, String operand2) {
        return String.valueOf(Integer.parseInt(operand1) / Integer.parseInt(operand2));
    }
}