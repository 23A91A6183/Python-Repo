import java.util.Scanner;
public class Rajesh{
    public static void main(String args[]){
        Scanner scanner=new Scanner(System.in);
        int sum=0;
        int n=scanner.nextInt();
        int[] arr=new int[n];
        for (int i = 0;i<n;i++){
            arr[i]=scanner.nextInt();
        }
        for (int i = 0;i<n;i++){
            if (arr[i]%2==0){
                sum+=arr[i];
            }
        }
        System.out.println(sum);
    }
}