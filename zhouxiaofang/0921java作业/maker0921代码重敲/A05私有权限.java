package maker0921代码重敲;

import maker.BB04私有;

public class A05私有权限 {
	
	private static int mya=20;
	private static void test() {
		System.out.println("我还私有成员方法");
	}

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		//1.在本文件中的类内访问私有成员
		test();
		System.out.println(mya);
		
		//2.调用本包中其他文件中的类里的私有成员
		B04私有 m=new B04私有();
		//不能访问本包中其他文件中的类中的私有成员
//		m.test05();
//		System.out.println(m.myB05);
		
		//3.访问别的包中的文件中的类里的私有成员
		BB04私有 m2=new BB04私有();
		//不能访问另一包中文件中的类中的私有成员
//		m2.testBB04();
		

	}

}
