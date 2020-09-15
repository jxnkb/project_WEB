package maker2;

import java.util.Scanner;

public class A03for {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		for(int i=0;i<10;i++) {
			System.out.print(i+" ");
		}
		System.out.println("-------------");
//		案例:输入一个整数,然后打印0到这个整数,最后打印0到这个整数之和
		//5
		//0 1 2 3 4 5
		//15
		Scanner scanner=new Scanner(System.in);
		System.out.println("请输入一 数字");
		int a=scanner.nextInt();
		int s=0;
		for(int i=0;i<=a;i++) {
			System.out.println(i);
			s+=i;
		}
		System.out.println(s);
		System.out.println("-------");
//		案例:n的阶乘，从外部键盘输入一个数字n
//		5
//		5*24=120
		int a1=scanner.nextInt();
		int s1=1;
		for(int i=1;i<=a1;i++) {
			s1*=i;
		}
		System.out.println(s1);

	}


}
