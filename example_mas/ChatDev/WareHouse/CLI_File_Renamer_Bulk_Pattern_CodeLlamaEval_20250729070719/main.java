import java.util.Scanner;
import java.io.File;
import java.io.IOException;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the pattern: ");
        String pattern = scanner.nextLine();
        System.out.print("Enter the directory: ");
        String directory = scanner.nextLine();
        scanner.close();
        Renamer renamer = new Renamer(pattern, directory);
        renamer.renameFiles();
    }
}