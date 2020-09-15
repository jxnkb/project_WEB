package test3;
import java.util.Scanner;
public class A10ifelseif {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
    int a=10;
    int b=20;
    if(a>b)
    {
    	System.out.println("a>b"); 	
    }
    if(a++>b++);
    System.out.println("a="+a);
    System.out.println("b="+b);
    if(a>b)
    {
    	System.out.println("a>b");
    }else if (a<b){
    	System.out.println("a<b");
    }else {
    	System.out.println("a==b");
	}
//    	案例:输入月份，输出对应的季节：
//		1~3--春季
//		4~6--夏季
//		7~9--秋季
//		10~12--冬季
		
    	Scanner scanner=new Scanner(System.in);
    	System.out.println("请输入一个月份");
    	int a1=scanner.nextInt();
    	 
    	if(a1>=1 && a1<=3) {
    	System.out.println("春季");	
    	}else if(a1>=4&&a1<=6){
        System.out.println("夏季");	
        }else if(a1>=10&&a1<=12){
        System.out.println("秋季");	
        }else if(a1>=10&&a1<=12){
        System.out.println("冬季");	
        }else {
        	System.out.println("输入错误");
        }
    }
	}



