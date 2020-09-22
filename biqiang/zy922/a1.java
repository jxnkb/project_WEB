package zy922;
//1.今天的代码重写一遍
//2.构造方法是谁调用的
//系统
//3.子类的构造函数默认调用父类的什么构造函数
//无参
//4.如果子类的构造函数要调用父类的有参构造,要用什么调用
//super关键字
//5.This的作用是什么
//代表本函数内的
//6.继承的关键字是什么
//extends
//7.继承可以继承父类的私有变量吗?
//可以，要用super


public class a1 {
	//8.写一个汽车的多态案例,如汽车类是父类,宝马的子类,操作打印各自子类的品牌
	//创建父类
	public static class car{
		String brand;
		protected car(String brand){
			this.brand=brand;
		}
		void getbrand(){
			
		}
	}
	//创建子类1
	public static class BMW extends car{
		BMW(String brand) {
			super(brand);
			// TODO Auto-generated constructor stub
		}
		void getbrand(){
			System.out.println(brand);
		}
	}
	//创建子类2
	public static class Benz extends car{
		Benz(String brand) {
			super(brand);
			// TODO Auto-generated constructor stub
		}
		void getbrand(){
			System.out.println(brand);
		}
	}
	//创建子类3
	public static class Bentley extends car{
		Bentley(String brand) {
			super(brand);
			// TODO Auto-generated constructor stub
		}
		void getbrand(){
			System.out.println(brand);
		}
	}
	//创建动作
	static void printBrand(car a){
		a.getbrand();
	}
	
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//创建对象
		Benz b1=new Benz("奔驰");
		Bentley b2=new Bentley("宾利");
		BMW b3=new BMW("宝马");
		//执行动作
		printBrand(b1);
		printBrand(b2);
		printBrand(b3);
		
		
	}

}
