// В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки 
// и возвращает сумму с учетом скидки. 
// Ваша задача - проверить этот метод с использованием библиотеки AssertJ. 
// Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException. 
// Не забудьте написать тесты для проверки этого поведения.
public class Calculator {
    public static int calculation(int firstOperand, int secondOperand, char operator) {
        int result;

        switch (operator) {
            case '+':
                result = firstOperand + secondOperand;
                break;
            case '-':
                result = firstOperand - secondOperand;
                break;
            case '*':
                result = firstOperand * secondOperand;
                break;
            case '/':
                if (secondOperand != 0) {
                    result = firstOperand / secondOperand;
                    break;
                } else {
                    throw new ArithmeticException("Division by zero is not possible");
                }
            default:
                throw new IllegalStateException("Unexpected value operator: " + operator);
        }
        return result;
    }

    // Домашнее задание - 1
    public static double calculateDiscount(double purchaseAmount, int discountAmount) {
        if (discountAmount < 0 || discountAmount > 100) {
            throw new ArithmeticException("Недопустимое значение процента скидки: " + discountAmount);
        }
        if (purchaseAmount <= 0) {
            throw new ArithmeticException("Сумма покупки должна быть положительной: " + purchaseAmount);
        }
        double discount = (double) discountAmount / 100; // Преобразование процента скидки в десятичное значение
        double discountedAmount = purchaseAmount - (purchaseAmount * discount);
        return discountedAmount;
    }

    public static void main(String[] args) {
        // Пример использования метода calculateDiscount:
        try {
            double purchaseAmount = -100.0; // Сумма покупки (недопустимое значение)
            int discountAmount = 10; // Процент скидки
            double discountedAmount = calculateDiscount(purchaseAmount, discountAmount);
            System.out.println("Сумма с учетом скидки: " + discountedAmount);
        } catch (ArithmeticException e) {
            System.err.println("Ошибка: " + e.getMessage());
        }
    }
}