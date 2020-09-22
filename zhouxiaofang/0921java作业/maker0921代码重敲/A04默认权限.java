package maker0921代码重敲;

import maker.BB03默认;
import maker.BB03Son;
import maker0921代码重敲.BM04;
public class A04默认权限 {

	//默认权限
	static int a=10;
	static void test() {
		System.out.println("默认方法的权限");
	}
	
	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		//1.调用本文件中的默认权限成员
		test();
		System.out.println(a);
		
		//2.调用本包中的其他文件中的类里的默认权限
		B03默认 m=new B03默认();
	    m.test();
	    System.out.println(m.mya);
		
		//3.调用别的包中的文件中的类里的默认成员
	    
	    BB03默认 m2=new BB03默认();
	    //不能直接调用另一个包中的类里的默认成员
//	    m2.test04();
//	    System.out.println(m2.bb);
	      //1.在那个含有保护成员的类中,创建一个公有方法,可以间接的调用该类的公有成员来调用保护成员
	      m2.ptest04();
	      //2.创建一个子类,该类继承的是另一个包中含有保护成员,然后在该子类中写一个调用保护成员的公有方法,
	      //再在本文件调用该子类的公有方法
	      BB03Son m3=new BB03Son();
	      m3.Stest04();
	    
	    //4.跨包创建一个子类,该类继承的是另一个包中含有保护成员,然后在该子类中写一个调用保护成员的公有方法,
			 //再在本文件调用该子类的公有方法
//	      BM04 m4=new BM04();
//		   m4.BMtest();
		  //跨包不可以访问父类的默认成员
		
	}
	
	
	
	
	

}
