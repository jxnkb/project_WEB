package joe_prac;

import java.awt.List;
import java.util.PrimitiveIterator;
import java.util.Scanner;

import javax.xml.ws.AsyncHandler;

public class bq9_14zy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner=new Scanner(System.in);
		

//		二.独立安装eclipse
//		三.写出main函数的四要素
//	访问修饰符:public，返回类型:void，函数名:main，函数体:大括号内的所有内容；
//		四.请写出int,float,double,char,long分别占内存的大小
//			int 4字节，float4字节，double8字节，char2字节，long8字节
//		五.强制类型转换怎么转换
//		数据类型 变量=（数据类型）变量
//		六.编程题
		
//		System.out.println("请猜一个数字：");
//		int a=scanner.nextInt();
//		int b=100;
//		if(a<b) {
//			System.out.println("小了");
//		}else if (a>b) {
//			System.out.println("大了");
//		}else {
//			System.out.println("恭喜你猜对了");
//		}
		
//		一.今天的代码重写一遍
//		System.out.println("hi");
//		int a1=1,b1=2,c1=3;
//		System.out.printf("a1=%d,b2=%d,c1=%d",a1,b1,c1);
		
		byte a2=100;
		int b2=a2;
		System.out.println(a2);
		
		int c2=1111;
		byte d2=(byte)c2;
		System.out.println(d2);
		
		char e2=']';
		String e3="]";
		System.out.println(e3+1);
		System.out.println(e2+1);
//		Scanner ax =new Scanner(System.in);
//		int ax1=ax.nextInt();
		
//		案例:从控制台输入三次整数,然后打印出最大的数值
//		System.out.println("请输入三个数：");
//		int a4=scanner.nextInt();
//		int b4=scanner.nextInt();
//		int c4=scanner.nextInt();
//		if(a4>b4 &a4>c4) {
//			System.out.println(a4);
//		}else if(b4>a4&b4>c4) {
//			System.out.println(b4);
//		}else {
//			System.out.println(c4);
//		}
		
//		if (a4>b4) {
//			if(a4>c4) {
//				System.out.println(a4);
//			}else {
//				System.out.println(c4);
//			}
//		}else {//a4<=b4
//			if(b4>c4) {
//				System.out.println(b4);
//			}else {
//				System.out.println(c4);
//			}
//		}
		
		
//		案例:从控制台输入一个数据,用变量a接收,如这个变量大于10,就打印"输入的数据大于10"
//		int a5=scanner.nextInt();
//		if(a5>10) {
//			System.out.println("输入的数值大于10");
//		}
		
////		案例:输入月份，输出对应的季节：
//		System.out.println("输入月份：");
//		int a6=scanner.nextInt();
//		if(a6>=1&a6<=3) {
//			System.out.println("春天");
//		}else if(a6>=4&a6<=6) {
//			System.out.println("夏天");
//		}else if (a6>=7&a6<=9) {
//			System.out.println("秋天");
//		}else if (a6>=10&a6<=12) {
//			System.out.println("冬天");
//		}else {
//			System.out.println("输入错误");
//		}
		

//		案例:定义两个整型变量,然后从控制台获取一个字符,如果是+那么这两个变量就相加,输入什么符号就对应运算什么
//		//从控制台获取一个字符
		int b7=12,c7=123;
		System.out.println("输入运算符");
		char a7=scanner.next().charAt(0);
		switch (a7) {
		case '+':
			System.out.println(b7+c7);
			break;
		case '-':
			System.out.println(b7-c7);
			break;
		case '*':
			System.out.println(b7*c7);
			break;
		case '/':
			System.out.println(b7/c7);
			break;

		default:
			System.out.println("输入错误");
			break;
		}
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	}

}
