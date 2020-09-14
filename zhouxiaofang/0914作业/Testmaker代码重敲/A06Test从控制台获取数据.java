package Testmaker代码重敲;

//1.要引入控制台输入的包
import java.util.Scanner;

public class A06Test从控制台获取数据 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		//2.生成一个对象
		Scanner scan=new Scanner(System.in);
		
		int i=scan.nextInt();
		System.out.println(i);
		
		float f=scan.nextFloat();
		System.out.println(f);
		
		String str=scan.next();
		System.out.println(str);
		
		String str1=scan.next(); //不管回车
		System.out.println(str1);
		
		String str2=scan.nextLine(); //回车会被收入
		System.out.println(str2);
		
		System.out.println("函数结束");

	}

}
