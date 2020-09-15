package maker2代码重敲;

import java.util.Scanner;


public class A03for {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根

		for(int i=0;i<10;i++) {
			System.out.println(i+" ");
		}
		System.out.println("-----");
		
//		案例:输入一个整数,然后打印0到这个整数,最后打印0到这个整数之和
		//5
		//0 1 2 3 4 5
		//15
		
		Scanner scan=new Scanner(System.in);
		System.out.println("请输入一个整数:");
		int a=scan.nextInt();
		int b=0;
		for(int i=0;i<=a;i++) {
			b=b+i;
			System.out.println(i);
		}
		System.out.println(b);
		
//		案例:n的阶乘，从外部键盘输入一个数字n
//		5
//		5*24=120
		
		System.out.println("请输入一个整数:");
		int n=scan.nextInt();
		int c=1;
		for(int i=1;i<=a;i++) {
			c=c*i;
			System.out.println(i);
		}
		System.out.println(c);
		
		
		
		
		
		
		
		
		
		
	}

}
