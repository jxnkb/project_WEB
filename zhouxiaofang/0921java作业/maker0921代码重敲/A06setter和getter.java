package maker0921代码重敲;

public class A06setter和getter {
	
	
	public static class Maker{
		private int age=10;
		
		int getAge() {
			return age;
		}
		
		void setAge(int age1) {
			if(age1>0 && age1<140) {
				age=age1;
			}else {
				System.out.println("输入的年龄不合法");
			}
			
		}
	}

	public static void main(String[] args) {
		// TODO 自动生成的方法存根

		Maker m=new Maker();
		int a=m.getAge();
		System.out.println(a); //10
		m.setAge(18);
		a=m.getAge();
		System.out.println(a); //18
		
		
		Users n=new Users();
		n.setName("maker");
		System.out.println(n.getName());
		
		n.setIpthon("12345678901");
		System.out.println(n.getIpthon());
		
		n.setPasswd("1234567","1234567891");
		System.out.println(n.getPasswd());
		
//案例:设计一个用户类,类里有私有成员姓名和密码,电话号码.设计这三个私有属性的setter和getter函数
//其中修改密码需要验证电话号码		
	}
	
	public static class Users{
		private String name="mmm";
		private String passwd="123456";
		private String ipthon="15770835722";
		
		//设置姓名
		void setName(String name1) {
			name=name1;
		}
		//获取姓名
		String getName() {
			return name;
		}
		
		//设置电话号码
		void setIpthon(String ipthon1) {
			ipthon=ipthon1;
		}
		//获取电话号码
		String getIpthon() {
			return ipthon;
		}
				
		//设置密码
		void setPasswd(String passwd1,String ipthon2) {
			if(ipthon2==ipthon) {
				passwd=passwd1;
			}else {
				System.out.println("输入的电话号码不正确");
			}
			
		}
		//获取密码
		String getPasswd() {
			return passwd;
		}
		
	}
	
	
	
	
	

}
