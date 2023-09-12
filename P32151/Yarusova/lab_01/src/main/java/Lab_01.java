import entity.MethodData;
import entity.Solution;
import io.ConsoleReader;
import io.FileReader;
import method.GaussSeidelMethod;

public class Lab_01 {
    public static void main(String[] args) {
        MethodData data;
        GaussSeidelMethod method = new GaussSeidelMethod();
        if (args.length == 0) {
            ConsoleReader cm = new ConsoleReader();
            data = cm.read();
        } else {
            FileReader fm = new FileReader(args[0]);
            data = fm.read();
        }
        if (data == null) {
            System.out.println("Invalid input");
            return;
        }
        try {
            Solution solution = method.solve(data);
            System.out.println(solution);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
