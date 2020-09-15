package test3;

public class A5运算符 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
    //算术运算符
		int a=10;
		int b=20;
		int c=a+b;
		int c1=a-b;
		int c2=a*b;
		int c3=a/b;
		int c4=a%b;
		c4++;
		--c4;
		System.out.println(c);
		System.out.println(c1);
		System.out.println(c2);
		System.out.println(c3);
		System.out.println(c4);
		
		//赋值运算符
		int x=10;
		x+=1;
		x-=2;
		x*=10;
		x/=2;
		x%=2;
		System.out.println(x);
		
		//比较运算符
		int y=20;
		int z=10;
		System.out.println(y==z);
		System.out.println(y>z);
		System.out.println(y<z);
		System.out.println(y!=z);
		System.out.println(y>=z);
		System.out.println(y<=z);
		System.out.println("hello" instanceof String);
	
		System.out.println("---------------");
	  //逻辑运算符
		boolean k=true;
		boolean kk=false;
		System.out.println(k&&kk);
		System.out.println(k&kk);
		System.out.println(k||kk);
		System.out.println(k|kk);
		System.out.println(k^kk);
		System.out.println(k!=kk);
		 int a1=10;
		 int b1=8;
		 int d1=a1&b1;
		 System.out.println(d1);
	}

}
