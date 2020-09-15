package test3;
import java.util.Scanner;
public class A11switch {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
    int a=2;
    switch(a) {
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
    	 break;
    }
    boolean b=true;
    float f=20.22f;
    double d=20.22;
    switch (a) {
//    1.()里面要填数字变量或返回的结果是数字的表达式
	case 20://2.case 后面必须是常量表达式
		System.out.println("a>10 && a<20");
		break;
	
	default:
		break;
	}
    	  
//	案例:定义两个整型变量,然后从控制台获取一个字符,如果是+那么这两个变量就相加,输入什么符号就对应运算什么
//	//从控制台获取一个字符
//    char d=Scan.next().charAt(0);
    int a1=10;
    int b1=20;
    Scanner scanner=new Scanner(System.in);
    char d1=scanner.next().charAt(0);
//	System.out.println(d1);
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
		System.out.println("你输入的符号不正确");
		break;
	}
        
        
    }
		
	}


