package maker0921代码重敲;

import maker.BB02公有;


public class A02公有权限 {

	

		//有公有权限的方法
		public static void test() {
			System.out.println("test");
		}
		
		public static int a=20;
		public static void main(String[] args) {
			
			//1.调用本文件的类中的公有成员
			test();
			System.out.println(a);
			
			//2.调用同一个包中其他文件中类里的公有成员
			B02公有  pp=new B02公有();
			pp.test02();
			System.out.println(pp.mya);
			
			//3.调用别的包中的类里的公有成员
			
			BB02公有 pu2=new BB02公有();
			pu2.test03();
			System.out.println(pu2.myb);
			
			
			System.out.println(add(10,20));
			
			A排序 aa=new A排序();
			int arr[]= {1,23,45,65,76,34};
			int[] bb=aa.msort(arr);
			for(int i:bb) {
				System.out.print(i+" ");
			}
//	案例:在本文件内写一个函数,函数的权限是公有的,然后在main中使用这个函数,这个函数的功能是加法功能		
//	案例:在别的文件写一个类,类里有一个方法,可以排序的,然后在本文件调用使用		
			
			
			
		}
		
		public static int add(int a,int b) {
			return a+b;
		}
		
		
		
	

}
