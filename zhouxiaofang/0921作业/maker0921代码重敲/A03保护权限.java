package maker0921代码重敲;

import maker.BB02Son;
import maker.BB02保护;
import maker0921代码重敲.BM04;

public class A03保护权限 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根

		//1.调用本文件的保护成员
		test();
		System.out.println(a);
		
		//2.调用本包中其他文件中类里的保护成员
		B02保护 m=new B02保护();
		m.test02();
		System.out.println(m.b);
		
		//3.调用另一个包中的类里的保护成员		
		BB02保护 m2=new BB02保护();
		
		//不能直接访问另一个包中类的保护成员
		//m2.test03(); 
		//System.out.println(m2.myb);
		  //1.在那个含有保护成员的类中,创建一个公有方法,可以间接的调用该类的公有成员来调用保护成员
		m2.test003();
		System.out.println(m2.getMyb());
//		  //2.创建一个子类,该类继承的是另一个包中含有保护成员,然后在该子类中写一个调用保护成员的公有方法,
//		      //再在本文件调用该子类的公有方法
		   BB02Son m3=new BB02Son();
		   m3.test022();
		   
		//4.跨包创建一个子类,该类继承的是另一个包中含有保护成员,然后在该子类中写一个调用保护成员的公有方法,
		 //再在本文件调用该子类的公有方法
		   BM04 m4=new BM04();
		   m4.BMtest();
	}
	
	protected static void test() {
		System.out.println("我是有保护权限的test");
	
	}
	
	protected static int a=10;

}
