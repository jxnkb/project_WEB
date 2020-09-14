package Testmaker代码重敲;

public class A05Test运算符 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		//1.算术运算符
		int a=10;
		int b=20;
		int c1=a+b;
		int c2=a-b;
		int c3=a*b;
		int c4=a/b;
		int c5=a%b;
		c5++;
		--c5;
		System.out.println(c1); //30
		System.out.println(c2); //-10
		System.out.println(c3); //200
		System.out.println(c4); //0
		System.out.println(c5); //10
		
		//2.赋值运算符
		int x=10;
		x+=1; //11
		x-=2; //9
		x*=10; //90
		x/=2;  //45
		x%=2;  //1
		System.out.println(x);  //1
		
		
		//3.比较运算符
		int y=20;
		int z=10; 
		System.out.println(y==z); //false
		System.out.println(y!=z); //true
		System.out.println(y>z);  //true
		System.out.println(y<z);  //false
		System.out.println(y>=z); //true
		System.out.println(y<=z); //false
		//instanceof用来判断一个实例是否是哪个对象生成的
		System.out.println("hello" instanceof String);
		System.out.println("--------");
		
		
		
		//4.逻辑运算符
		boolean k=true;
		boolean kk=false;
		System.out.println(k&kk); //false
		System.out.println(k&&kk);  //false
		System.out.println(k|kk);  //true
		System.out.println(k||kk); //true
		System.out.println(k^kk);  //true
		System.out.println(!kk);   //true
		
		
		//5.位运算
		int a1=10;
		int b1=8;
		/*
		 * 0000 1010
		 * 0000 1000
		 * 0000 1000-->8
		 * 
		 */
		int d1=a1&b1;
		System.out.println(d1);
		
		
	}

}
