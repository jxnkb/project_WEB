package Testmaker代码重敲;

import java.util.Scanner;


public class A07Test三目运算符 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		int a=10;
		int b=20;
		int c=a>b?a:b;
		System.out.println(c);
		
//		案例:从控制台输入三次整数,然后打印出最大的数值
		Scanner scan=new Scanner(System.in);
		System.out.println("请输入第一个数字:");
		int a1=scan.nextInt();
		System.out.println("请输入第二个数字:");
		int a2=scan.nextInt();
		System.out.println("请输入第三个数字:");
		int a3=scan.nextInt();
		
		int b2=a1>a2?(a1>a3?a1:a3):(a2>a3?a2:a3);
		System.out.println(b2);
		
		

	}

}
