package maker0921代码重敲;

public class A01类与对象的案例 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		//定义点对象
		B01Point aa=new B01Point();
		aa.setX(10);
		aa.setY(20);
		
		//定义圆对象
		B01Circle bb=new B01Circle();
//		bb.setMx(20);
//		bb.setMy(30);
//		bb.setR(5);
//		
//		bb.pd(aa);
		
		
		//定义圆心
		B01Point p1=new B01Point();//p1(xx3,xx3);
		//把点赋值给圆心
		bb.setH(p1);
		
		bb.pd(aa);

	}

}
