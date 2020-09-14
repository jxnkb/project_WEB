package Testmaker代码重敲;

import java.util.Scanner;

public class A11Testswitch {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		int a=2;
		switch (a) {
		case 1:
		   System.out.println("1");
		   break;
		case 2:
		   System.out.println("2");
		   break;  
		case 3:
		   System.out.println("3");
		   break;  
		default:
		   System.out.println("其他");
		   break;
		  
		}
	
		
		char c='a';
		switch (c) {
		case 'a':
			System.out.println("a");
		    break;
		case 'b':
			System.out.println("b");
		    break;
		case 'c':
			System.out.println("c");
		    break;	
		default:
			break;
			
		}
		
		boolean b=true;
		float f=20.33f;
		double d=20.44;
		switch (a) { //1.()里面要填数字变量或返回的结果是数字的表达式
		case 20:  //2.case 后面必须是常量表达式
			System.out.println("a>10 && a<20");
		    break;
		default:
		    break;
		
		}

//		案例:定义两个整型变量,然后从控制台获取一个字符,如果是+那么这两个变量就相加,输入什么符号就对应运算什么
//		//从控制台获取一个字符
//		char d=scan.next().charAt(0);
		int a1=10;
		int b1=20;
		Scanner scan=new Scanner(System.in);
		char d1=scan.next().charAt(0);
		System.out.println(d1);
		switch (d1) {
		case '+':
			System.out.println(a1+b1);
		    break;
		case '-':
			System.out.println(a1-b1);
		    break;
		case '*':
			System.out.println(a1*b1);
		    break;		    
		case '/':
			System.out.println(a1/b1);
		    break;
		    	    
		default:
			System.out.println("输入有误");
			break;
		}
		
		
		
		
		
		
		
	}

}
