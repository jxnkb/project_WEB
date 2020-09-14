package Testmaker代码重敲;

import java.util.Scanner;

public class A08Testif {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根

//		int a=10;
	//	if(a) { //不能填非布尔类型的变量
			
//			System.out.println("我是if里面的语句");
//		}
		
		
		boolean b=true;
		if(b) {
			
			System.out.println("我是if里面的语句");
		}
		
		
		int a1=30;
		int b1=20;
		if(a1>b1) {
			System.out.println("我是a1>b1里面的语句");
		}
		
		if(100>20) {
			System.out.println("我是100>20里面的语句");
		}
		
//		案例:从控制台输入一个数据,用变量a接收,如这个变量大于10,就打印"输入的数据大于10"	
		
		Scanner scan=new Scanner(System.in);
		int a2=scan.nextInt();
		if(a2>10) {
			System.out.println("输入的数据大于10");
		}
		
			
		
	}

}
