import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            
            String[] data = line.split(";");
            int N = Integer.valueOf(data[0]);
            
            String[] values = data[1].split(" ");
            if (values.length < N){
                System.out.println(0);
                continue;
            }
            
            int[] numbers = new int[values.length];
            for(int i=0; i < values.length; i++)
                numbers[i] = Integer.parseInt(values[i]);
                
            int current_sum = 0;
            for(int i =0; i < N; i++) 
                current_sum += numbers[i];
            
            int best_sum = current_sum;
            if (best_sum<0) best_sum = 0;

            
            for(int i=N; i < numbers.length; i++){
                current_sum += numbers[i] - numbers[i-N];
                if (current_sum>best_sum) 
                    best_sum = current_sum;
            }
            
            System.out.println(best_sum);
        }
    }
}


        
