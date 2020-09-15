package test3;
import java.util.Scanner;
public class A7三目运算符 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
    int a=10;
    int b=20;
    int c=a>b?a:b;
    System.out.println(c);
    
//	案例:从控制台输入三次整数,然后打印出最大的数值
    Scanner scanner=new Scanner(System.in);
    System.out.println("请输入第一个整数");
    int a1=scanner.nextInt();
    System.out.println("请输入第二个整数");
    int a2=scanner.nextInt();
    System.out.println("请输入第三个整数");
    int a3=scanner.nextInt();
    int b2=a1>a2?(a1>a3?a1:a3):(a2>a3?a2:a3);
    System.out.println(b2);
	}

}
