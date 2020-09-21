package joe_prac;

public class jiabfjsb {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//案例:设计一个用户类,类里有私有成员姓名和密码,电话号码.设计这三个私有属性的setter和getter函数
		//其中修改密码需要验证电话号码
		usr u1=new usr();
		u1.setName("biqiang");
		u1.setPhone("12212121");
		u1.setPwd("12212121","123456");
				
		String a=u1.getName();
		System.out.println(a);
		
		prac9_21_main.pub1();
		prac9_21_main.def1();
//		prac9_21_main.pri1() 私有在不同的类文件看不到
		prac9_21_main.pro1();
		
	}

}
